# Roadmap — Mi Agente

La visión: un agente personal que gestiones tú y que te gestione a ti — correo, reservas,
llamadas, proyectos, ideas, apps… — y que **controles desde el iPhone (Siri / un toque)**. Lo
construimos por fases, ampliando y mejorando cada día. Lo hecho se anota en `datos/registro.md`.

## Leyenda de dificultad
✅ Fácil y gratis · 💶 Requiere cuenta/servicio o cuesta dinero · 🧪 Frontera (hoy nadie lo hace
redondo de forma 100% autónoma)

---

## Fase 0 — Base ✅ (hecho)
- [x] Tareas, recordatorios, notas y resumen del día.
- [x] Comando `/agente` para usarlo dentro de Claude.
- [x] Datos persistentes en git.

## Fase 1 — Control desde el iPhone ✅ (hoy)
- [x] Atajo de Siri / pantalla de inicio que habla con Claude (asistente de voz general).
      Ver `mi-agente/iphone/atajo-siri.md`.
- Limitación: aún no ve tus tareas/correo (eso es la Fase 2).

## Fase 2 — El cerebro en la nube 🟡 (en curso)
Un pequeño servidor (FastAPI) que pasa tu voz a Claude Code (tu **suscripción**, sin API key)
dentro del repo. El atajo del iPhone pasa a hablar con **tu** agente (ve tus tareas, recordatorios,
notas). Código y guía: `mi-agente/servidor/`.
- [x] Servidor con endpoint `POST /agente` (texto entra → agente actúa → `{ "reply": ... }`).
- [x] Acceso a tus datos vía Claude Code dentro del repo (lee/escribe `mi-agente/datos/`).
- [x] Guía de despliegue (Claude Code + login de suscripción + Tailscale + atajo).
- [ ] **Tú:** elegir máquina siempre encendida y desplegar (te doy el servicio listo).
- [ ] Auto-commit de los datos para persistir entre reinicios.

## Fase 3 — Correo (Gmail) ✅/💶
- [ ] Leer y **resumir** tu bandeja ("¿algo importante hoy?").
- [ ] **Redactar** respuestas y borradores; enviarlos con tu confirmación.
- [ ] Buscar correos, marcar, archivar.
- Requiere: conectar tu cuenta de Google (OAuth). Técnicamente muy factible.

## Fase 4 — Proyectos e ideas ✅
- [ ] Gestor de proyectos (objetivos, próximos pasos, estado).
- [ ] Captura de ideas y brainstorming; convertir ideas en planes.
- [ ] Seguimiento ("¿cómo va el proyecto X?").

## Fase 5 — Reservas 🧪/💶
Honestidad: **no hay una API universal de reservas.** Lo realista:
- [ ] Donde hay API/bot (p. ej. actividades/tours vía Civitatis, que ya está disponible aquí):
      el agente busca, comprueba disponibilidad y te deja la reserva lista.
- [ ] Donde no la hay (restaurantes, peluquería…): el agente **prepara** la reserva (encuentra el
      sitio, redacta el mensaje/email o rellena el formulario) y la confirmas tú. Reservar de
      forma 100% autónoma y fiable en cualquier sitio todavía no es realista.

## Fase 6 — Llamadas 🧪/💶
- [ ] Hacer llamadas y hablar por ti con una voz de IA (vía Twilio Voice).
- Honestidad: es lo más avanzado, **cuesta dinero** (número + minutos) y requiere montaje. Lo
      dejamos para cuando el resto esté rodado.

## Fase 7+ — Ideas sueltas
- [ ] Resumen automático cada mañana (notificación proactiva).
- [ ] Avisos al vencer recordatorios.
- [ ] Calendario (Google Calendar).
- [ ] Hábitos con racha · Gastos con resumen mensual.
- [ ] Tareas recurrentes y por categorías/proyectos.

---

## Cómo pedir lo siguiente
Dime, por ejemplo: *"vamos con el correo"*, *"monta el cerebro en la nube"*, *"quiero gestor de
proyectos"*. Lo construimos ese día y lo anotamos en el registro.
