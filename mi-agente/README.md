# 🤖 Mi Agente — asistente personal desde Claude

Un asistente personal para tus tareas diarias que **gestionas desde Claude**, sin WhatsApp ni
servidores. Vive en este repositorio: sus "recuerdos" son archivos de texto que persisten en git,
así que no olvida nada entre sesiones. Lo vamos ampliando poco a poco.

## Cómo se usa

En cualquier sesión de Claude sobre este repo, escribe el comando **`/agente`** seguido de lo que
quieras, en lenguaje natural:

```
/agente ¿qué tengo hoy?
/agente añade tarea comprar pan para mañana, prioridad alta
/agente recuérdame llamar al dentista el martes a las 10
/agente marca como hecha la tarea del informe
/agente apunta la idea: regalar un libro de cocina
/agente ¿qué notas tengo sobre regalos?
```

- `/agente` **sin texto** → te muestra el **resumen del día**.
- También puedes hablarle normal (sin el comando) y pedirle que actúe como tu agente; el comando
  solo es un atajo que carga su configuración y tus datos.

## Qué sabe hacer (v1)
- 📋 **Tareas**: añadir, listar, completar, priorizar, borrar.
- ⏰ **Recordatorios**: crear con fecha/hora, ver los de hoy y los vencidos.
- 📝 **Notas**: guardar ideas y buscarlas.
- 🌅 **Resumen del día**: lo que toca y qué atender primero.
- 💬 **Asistente general**: redactar, resumir, traducir, responder.

## Estructura
```
mi-agente/
├── README.md        ← esto
├── AGENTE.md        ← instrucciones de cómo se comporta el agente ("su cerebro")
├── ROADMAP.md       ← ideas para ampliarlo (incluido WhatsApp en el futuro)
└── datos/
    ├── tareas.md        ← tus tareas
    ├── recordatorios.md ← tus recordatorios
    ├── notas.md         ← tus notas
    └── registro.md      ← bitácora de lo que añadimos cada día

.claude/commands/agente.md  ← define el comando /agente
```

## Importante: persistencia en la nube
Esta sesión corre en un contenedor temporal. Para que tus tareas y notas **no se pierdan**, hay
que **commitear y hacer push** de los cambios. El agente te lo irá recordando, y puedes pedírselo
cuando quieras: *"guarda los cambios"*.

## Cómo crecemos
Lo ampliamos cada día. ¿Quieres algo nuevo (hábitos, gastos, resumen automático por la mañana,
WhatsApp…)? Solo pídelo. Lo que vamos añadiendo queda anotado en `datos/registro.md`.
