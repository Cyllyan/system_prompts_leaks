# 📱 Atajo de iPhone / Siri para Mi Agente

Esto te monta un **asistente de voz** en el iPhone: lo lanzas diciendo *"Oye Siri, Asistente"* o
tocando un icono en la pantalla de inicio. Habla directamente con Claude (la API de Anthropic).

> ⚠️ **Fase 1.** Este atajo habla con un Claude **general**: te responde, redacta, resume, traduce,
> hace ideas, etc. Todavía **no** ve tus tareas/correo de `mi-agente/` — eso llega en la Fase 2,
> cuando montemos "el cerebro" en la nube y el atajo apunte a él (solo cambiará la URL).

## Qué necesitas
- Un iPhone con la app **Atajos** (Shortcuts, viene de serie).
- Una **API key de Anthropic**: entra en https://console.anthropic.com → *API Keys* → crea una.
  Es tu clave personal; guárdala solo en tu atajo (privado).

## Pasos en la app Atajos

1. Abre **Atajos** → **+** (nuevo atajo). Ponle de nombre **`Asistente`** (ese será el nombre que
   dirás a Siri: *"Oye Siri, Asistente"*).

2. Añade la acción **"Dictar texto"** (Dictate Text). *(Para escribir en vez de hablar, usa
   "Pedir entrada" / Ask for Input.)*

3. Añade **"Obtener contenido de URL"** (Get Contents of URL) y configúrala:
   - **URL:** `https://api.anthropic.com/v1/messages`
   - **Método:** `POST`
   - **Cabeceras** (Headers):
     - `x-api-key` = *(tu API key)*
     - `anthropic-version` = `2023-06-01`
     - `content-type` = `application/json`
   - **Cuerpo de la solicitud:** `JSON`, con esta estructura:
     ```json
     {
       "model": "claude-sonnet-5-5",
       "max_tokens": 1024,
       "system": "Eres Mi Agente, el asistente personal de tu usuario. Hablas español, tuteas, eres cercano, directo y breve. Respondes en texto corto y claro, pensado para escucharse en voz alta.",
       "messages": [
         { "role": "user", "content": "AQUÍ_EL_TEXTO_DICTADO" }
       ]
     }
     ```
     En el campo `content`, borra `AQUÍ_EL_TEXTO_DICTADO` e inserta la **variable del paso 2**
     ("Texto dictado").

4. Añade **"Obtener valor del diccionario"** (Get Dictionary Value): obtén la clave **`content`**
   del "Contenido de URL".

5. Añade **"Obtener elemento de la lista"** (Get Item from List): el **primer** elemento.

6. Añade otra vez **"Obtener valor del diccionario"**: obtén la clave **`text`** de ese elemento.

7. Añade **"Reproducir texto"** (Speak Text) con ese valor. *(Opcional: añade también "Mostrar
   resultado" para verlo en pantalla.)*

8. Guarda. Para el **acceso de un toque**: menú del atajo → **"Añadir a pantalla de inicio"**.

## Cómo se usa
- Por voz: *"Oye Siri, Asistente"* → te pregunta → le hablas → te contesta en voz alta.
- De un toque: pulsas el icono en la pantalla de inicio.

## Si algo falla
- **Error de modelo:** copia el nombre exacto del modelo desde la consola de Anthropic
  (`console.anthropic.com` → Models) y ponlo en `"model"`. Para respuestas más rápidas prueba
  `claude-haiku-5-5`; para más calidad, un modelo Sonnet u Opus.
- **401 / clave inválida:** revisa que `x-api-key` sea tu clave sin espacios.
- **No lee la respuesta:** revisa que en el paso 4 la clave sea `content` y en el 6 sea `text`.

## Siguiente paso (Fase 2)
Montamos "el cerebro" en la nube: un pequeño servidor con la memoria y las herramientas de
`mi-agente/` (tus tareas, y luego correo, etc.). Entonces, en el paso 3, solo cambiarás la URL por
la de tu servidor y el atajo pasará a hablar con **tu** agente, no con un Claude genérico.
