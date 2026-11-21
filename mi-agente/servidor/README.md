# 🧠 El cerebro en la nube (con tu suscripción de Claude)

Este servidor hace que tu iPhone hable con **tu** agente (el de `mi-agente/`, con tus tareas y
memoria), usando tu **suscripción de Claude** a través de Claude Code. **No necesita API key.**

```
iPhone (atajo/Siri)  ──►  este servidor  ──►  Claude Code (tu suscripción)  ──►  tus datos
        ◄───────────────── respuesta hablada ─────────────────
```

> ⚖️ **Nota honesta:** esto usa tu suscripción personal de forma automatizada. Está pensado para
> **tu uso personal y de bajo volumen** (tú hablando con tu asistente). Un uso intensivo o de
> servicio podría chocar con los términos de tu plan — revísalos. Y necesita **una máquina tuya
> siempre encendida**; si se apaga, el iPhone no obtiene respuesta.

## Qué necesitas
- Una máquina **siempre encendida**: tu Mac, una **Raspberry Pi**, o un **VPS** barato (Linux).
- Suscripción **Claude Pro o Max**.
- Python 3.10+ y Node.js (para instalar Claude Code).

## Paso 1 — Instalar Claude Code e iniciar sesión con tu suscripción
```bash
npm install -g @anthropic-ai/claude-code      # o sigue la guía oficial de instalación
claude            # la primera vez te pide login: elige tu cuenta (suscripción), NO API key
```
En una máquina sin navegador (Raspberry/VPS), usa el flujo de código de dispositivo que te ofrece
el propio `claude` al iniciar sesión.

## Paso 2 — Clonar tu repo en la máquina
```bash
git clone https://github.com/Cyllyan/system_prompts_leaks.git
cd system_prompts_leaks/mi-agente/servidor
```

## Paso 3 — Instalar y configurar el servidor
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edita .env y pon un AGENTE_TOKEN secreto:  openssl rand -hex 24
```

## Paso 4 — Arrancar
```bash
source .venv/bin/activate
uvicorn app:app --host 0.0.0.0 --port 8787
```
Prueba local:
```bash
curl -s http://localhost:8787/health
curl -s -X POST http://localhost:8787/agente \
  -H "x-agent-token: TU_SECRETO" -H "content-type: application/json" \
  -d '{"text":"¿qué tengo hoy?"}'
```

## Paso 5 — Que el iPhone llegue a la máquina (recomendado: Tailscale)
**Tailscale** crea una red privada entre tu iPhone y la máquina, sin abrir puertos al exterior:
1. Instala Tailscale en la máquina y en el iPhone, con **la misma cuenta**.
2. Mira la IP `100.x.x.x` de la máquina (`tailscale ip -4`).
3. El endpoint para el iPhone será: `http://100.x.x.x:8787/agente`

Alternativa con URL pública: **Cloudflare Tunnel** (`cloudflared tunnel --url http://localhost:8787`).

## Paso 6 — Dejarlo corriendo siempre
- **Mac:** crea un servicio `launchd` (archivo .plist en `~/Library/LaunchAgents`).
- **Linux (Raspberry/VPS):** crea un servicio `systemd` que ejecute el `uvicorn` anterior.
Dime tu máquina y te doy el archivo de servicio listo para copiar.

## Paso 7 — Apuntar el atajo del iPhone a tu servidor
En el atajo (ver `../iphone/atajo-siri.md`), cambia la acción "Obtener contenido de URL":
- **URL:** `http://100.x.x.x:8787/agente` (tu IP de Tailscale)
- **Método:** `POST`
- **Cabeceras:** `x-agent-token` = *(tu AGENTE_TOKEN)*, `content-type` = `application/json`
- **Cuerpo JSON:** `{ "text": "TEXTO_DICTADO" }` (inserta ahí la variable del dictado)
- Luego un solo **"Obtener valor del diccionario"** con la clave **`reply`** → **"Reproducir texto"**.

Mucho más simple de leer que la API directa: la respuesta es `{ "reply": "..." }`.

## Memoria conversacional (opcional)
Si quieres que recuerde el hilo de lo último que hablasteis, envía en el cuerpo
`{ "text": "...", "continue_session": true }`. Sin eso, cada petición es independiente (pero tus
datos en `mi-agente/datos/` siempre persisten como memoria a largo plazo).
