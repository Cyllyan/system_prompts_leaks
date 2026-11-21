"""
Mi Agente — servidor "cerebro".

Recibe texto (p. ej. desde el atajo del iPhone), se lo pasa a Claude Code
ejecutándose DENTRO de tu repo (con AGENTE.md y tus datos), y devuelve la
respuesta. Usa tu SUSCRIPCIÓN de Claude vía Claude Code: no necesita API key.

Arranque:
    uvicorn app:app --host 0.0.0.0 --port 8787

Config (archivo .env en esta carpeta, ver .env.example):
    AGENTE_TOKEN        secreto que el iPhone debe enviar en la cabecera x-agent-token
    AGENTE_PROJECT_DIR  (opcional) ruta del repo; por defecto se detecta sola
    CLAUDE_BIN          (opcional) ruta del binario claude; por defecto "claude"
"""
import json
import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

BASE = Path(__file__).resolve().parent              # .../mi-agente/servidor
load_dotenv(BASE / ".env")

# Raíz del repo (dos niveles por encima de servidor/). Ahí están las rutas
# relativas que usa AGENTE.md, como mi-agente/datos/tareas.md
PROJECT_DIR = Path(os.environ.get("AGENTE_PROJECT_DIR", BASE.parent.parent))
AGENTE_MD = BASE.parent / "AGENTE.md"               # .../mi-agente/AGENTE.md
TOKEN = os.environ.get("AGENTE_TOKEN", "")
CLAUDE_BIN = os.environ.get("CLAUDE_BIN", "claude")

app = FastAPI(title="Mi Agente")


class Msg(BaseModel):
    text: str
    continue_session: bool = False  # True = mantiene el hilo de la última conversación


def system_prompt() -> str:
    try:
        return AGENTE_MD.read_text(encoding="utf-8")
    except OSError:
        return "Eres Mi Agente, asistente personal. Hablas español, breve y claro."


@app.get("/health")
def health():
    return {"ok": True, "project_dir": str(PROJECT_DIR)}


@app.post("/agente")
def agente(msg: Msg, x_agent_token: str = Header(default="")):
    if not TOKEN or x_agent_token != TOKEN:
        raise HTTPException(status_code=401, detail="token inválido")

    cmd = [
        CLAUDE_BIN, "-p", msg.text,
        "--append-system-prompt", system_prompt(),
        "--permission-mode", "acceptEdits",
        "--allowedTools", "Read Edit Write Glob Grep",
        "--output-format", "json",
    ]
    if msg.continue_session:
        cmd.append("--continue")

    try:
        out = subprocess.run(
            cmd, cwd=str(PROJECT_DIR),
            capture_output=True, text=True, timeout=180,
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="el agente tardó demasiado")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail=f"no encuentro el binario '{CLAUDE_BIN}'")

    if out.returncode != 0:
        raise HTTPException(status_code=500, detail=(out.stderr or "error del agente")[-500:])

    reply = out.stdout.strip()
    try:
        data = json.loads(out.stdout)
        reply = data.get("result", reply)
    except json.JSONDecodeError:
        pass
    return {"reply": reply}
