"""
preguntas.py
Banco de contenido del juego "SO Quest".
Para añadir más preguntas basta con copiar un diccionario de la lista
correspondiente y cambiar sus textos. No hace falta tocar app.py.
"""

# ---------------------------------------------------------------------------
# Los 5 criterios de clasificación de un sistema operativo
# ---------------------------------------------------------------------------
CRITERIOS = {
    "tiempo": {
        "nombre": "1. Tiempo de respuesta",
        "opciones": ["Por lotes", "Interactivo (tiempo compartido)", "Tiempo real"],
    },
    "usuarios": {
        "nombre": "2. Número de usuarios",
        "opciones": ["Monousuario", "Multiusuario"],
    },
    "procesos": {
        "nombre": "3. Número de procesos",
        "opciones": ["Monoprogramación", "Multiprogramación"],
    },
    "procesadores": {
        "nombre": "4. Número de procesadores",
        "opciones": ["Monoproceso", "Multiproceso simétrico", "Multiproceso asimétrico"],
    },
    "red": {
        "nombre": "5. Trabajo en red",
        "opciones": ["Centralizado", "En red", "Distribuido"],
    },
}

# Atajos para escribir los casos más cómodamente
LOTES, INTER, RT = CRITERIOS["tiempo"]["opciones"]
MONO_U, MULTI_U = CRITERIOS["usuarios"]["opciones"]
MONO_P, MULTI_P = CRITERIOS["procesos"]["opciones"]
MONO_CPU, SIM, ASIM = CRITERIOS["procesadores"]["opciones"]
CENTRAL, RED, DISTRIB = CRITERIOS["red"]["opciones"]


def _caso(titulo, enunciado, resp, clave, justificacion, pista, nuevo=False):
    return {
        "titulo": titulo,
        "enunciado": enunciado,
        "respuesta": dict(zip(CRITERIOS.keys(), resp)),
        "clave": clave,
        "justificacion": justificacion,
        "pista": pista,
        "nuevo": nuevo,  # True = caso extra que no estaba en la tarea
    }


# ---------------------------------------------------------------------------
# Casos para clasificar (los 10 de la tarea + 7 extra)
# ---------------------------------------------------------------------------
CASOS = [
    _caso(
        "🚗 Frenos ABS de un coche",
        "Un pequeño ordenador con un solo microcontrolador lee los sensores de las "
        "ruedas cientos de veces por segundo y abre o cierra las válvulas de freno. "
        "No tiene pantalla ni nadie que lo maneje.",
        [RT, MONO_U, MONO_P, MONO_CPU, CENTRAL],
        "Tiempo de respuesta",
        "Debe actuar en milisegundos con un plazo garantizado; si falla, hay accidente.",
        "Si tarda más del plazo, el resultado es inútil aunque sea correcto.",
    ),
    _caso(
        "💻 Portátil con Windows 11",
        "Tienes abiertos el navegador, Spotify y Word. Tiene un procesador de "
        "8 núcleos iguales y está conectado al wifi de casa.",
        [INTER, MONO_U, MULTI_P, SIM, RED],
        "Procesos",
        "Navegador, Spotify y Word a la vez; los 8 núcleos iguales se reparten el trabajo.",
        "Fíjate en que los 8 núcleos son iguales entre sí.",
    ),
    _caso(
        "🖧 Servidor Linux del instituto",
        "30 alumnos se conectan a la vez desde sus PC por SSH; cada uno trabaja con "
        "su propia cuenta y sus programas se ejecutan en el servidor. Tiene 2 "
        "procesadores de 16 núcleos.",
        [INTER, MULTI_U, MULTI_P, SIM, RED],
        "Usuarios",
        "30 alumnos a la vez, cada uno con su cuenta, y sus programas corren en el servidor.",
        "¿Cuántas personas lo usan a la vez?",
    ),
    _caso(
        "🔍 El buscador de Google",
        "Miles de servidores en varios países trabajan juntos y responden en menos "
        "de un segundo; el usuario lo ve como un único servicio.",
        [INTER, MULTI_U, MULTI_P, SIM, DISTRIB],
        "Trabajo en red",
        "Miles de servidores cooperan y el usuario los ve como un único servicio.",
        "«El usuario lo ve como un único servicio» es la gran pista.",
    ),
    _caso(
        "🏦 Ordenador central de un banco",
        "Cada noche procesa, sin que nadie intervenga, los recibos de todos los "
        "clientes y genera los extractos.",
        [LOTES, MONO_U, MULTI_P, SIM, CENTRAL],
        "Tiempo de respuesta",
        "Trabajo nocturno masivo, sin que nadie intervenga ni espere el resultado.",
        "Nadie está delante esperando una respuesta.",
    ),
    _caso(
        "📟 PC de 1985 con MS-DOS",
        "Ejecuta un programa de contabilidad y, para abrir otro, hay que cerrar el "
        "primero. No está conectado a nada.",
        [INTER, MONO_U, MONO_P, MONO_CPU, CENTRAL],
        "Procesos",
        "Para abrir otro programa hay que cerrar el primero. Además, no tiene red.",
        "Un solo programa cada vez.",
    ),
    _caso(
        "🏥 Monitor de constantes vitales",
        "Mide el pulso y el oxígeno de un paciente y debe dar la alarma en menos de "
        "1 segundo si algo va mal. Envía los datos al control de enfermería por la red.",
        [RT, MONO_U, MULTI_P, MONO_CPU, RED],
        "Tiempo de respuesta",
        "La alarma debe sonar en menos de 1 s, plazo garantizado.",
        "Hay un plazo máximo que no se puede superar.",
    ),
    _caso(
        "🏫 Aula de informática",
        "20 PC con Windows: cada alumno usa el suyo, pero todos imprimen en la misma "
        "impresora y guardan los trabajos en una carpeta compartida del servidor.",
        [INTER, MONO_U, MULTI_P, SIM, RED],
        "Trabajo en red",
        "Cada PC tiene su propio SO, pero comparten impresora y carpeta del servidor.",
        "Cada equipo tiene su propio sistema operativo.",
    ),
    _caso(
        "✈️ Reservas de una aerolínea (años 80)",
        "Un gran ordenador central en Madrid, con varios procesadores, hace todo el "
        "trabajo; los mostradores de los aeropuertos solo tienen un teclado y una "
        "pantalla (terminales) conectados a él.",
        [INTER, MULTI_U, MULTI_P, SIM, CENTRAL],
        "Trabajo en red",
        "Todo el trabajo lo hace el ordenador central; los terminales solo tienen teclado y pantalla.",
        "Los terminales no tienen ni procesador ni SO propios.",
    ),
    _caso(
        "📱 Móvil Android",
        "Tiene un procesador de 8 núcleos (4 potentes y 4 de bajo consumo) y lo usa "
        "una sola persona.",
        [INTER, MONO_U, MULTI_P, SIM, RED],
        "Procesadores",
        "Aunque los núcleos difieran, cualquiera ejecuta el SO y se reparte el trabajo "
        "(es simétrico: lo que importa es quién reparte, no la potencia).",
        "Piensa en quién reparte el trabajo, no en la potencia de cada núcleo.",
    ),
    # ------------------------- CASOS EXTRA -------------------------
    _caso(
        "📺 Smart TV",
        "Una tele con Android TV, procesador de 4 núcleos iguales, wifi y varias apps "
        "abiertas a la vez (Netflix en segundo plano y el menú en primer plano). "
        "La usa quien tiene el mando.",
        [INTER, MONO_U, MULTI_P, SIM, RED],
        "Procesos",
        "Varias apps a la vez en 4 núcleos iguales y conexión a Internet.",
        "Es parecida a un móvil.",
        nuevo=True,
    ),
    _caso(
        "❤️ Marcapasos",
        "Un microcontrolador implantado en el pecho que genera un impulso eléctrico "
        "en el instante exacto, con un único programa de control. No tiene red.",
        [RT, MONO_U, MONO_P, MONO_CPU, CENTRAL],
        "Tiempo de respuesta",
        "El impulso debe darse dentro de un plazo garantizado: un retraso pone en riesgo una vida.",
        "Un fallo de tiempo aquí es muy grave.",
        nuevo=True,
    ),
    _caso(
        "🧪 Clúster de investigación",
        "Cientos de investigadores envían sus trabajos a una cola. Un clúster de 1.000 "
        "nodos que se comporta como una única máquina los ejecuta cuando hay hueco, "
        "sin que nadie los espere, y devuelve los resultados horas después.",
        [LOTES, MULTI_U, MULTI_P, SIM, DISTRIB],
        "Tiempo de respuesta",
        "Los trabajos se encolan y se ejecutan sin interacción: es proceso por lotes sobre un sistema distribuido.",
        "Cola de trabajos + nadie esperando delante de la pantalla.",
        nuevo=True,
    ),
    _caso(
        "🏧 Cajero automático",
        "Un ordenador con un solo procesador, dentro del cajero, ejecuta únicamente "
        "el programa del cajero y atiende a una persona cada vez. Se conecta por "
        "red a los servidores del banco.",
        [INTER, MONO_U, MONO_P, MONO_CPU, RED],
        "Usuarios",
        "Una persona cada vez, un solo programa y un solo procesador; solo se conecta al banco por la red.",
        "Cuenta cuántas personas, programas y procesadores hay.",
        nuevo=True,
    ),
    _caso(
        "🍓 Raspberry Pi compartida",
        "Una Raspberry Pi 4 (4 núcleos iguales) en casa. Tres hermanos se conectan "
        "por SSH, cada uno con su usuario y contraseña, y ejecutan sus scripts a la vez.",
        [INTER, MULTI_U, MULTI_P, SIM, RED],
        "Usuarios",
        "Tres cuentas distintas trabajando a la vez: multiusuario, aunque la máquina sea pequeña.",
        "El tamaño del equipo no cambia el número de usuarios.",
        nuevo=True,
    ),
    _caso(
        "🎮 Videoconsola actual",
        "Una consola con 8 núcleos iguales que ejecuta el juego, el chat de voz y las "
        "descargas a la vez, conectada a Internet. La usa una sola cuenta a la vez.",
        [INTER, MONO_U, MULTI_P, SIM, RED],
        "Trabajo en red",
        "Es el ejemplo clásico de la tarea: interactiva, monousuario, multiprogramación, multiproceso y en red.",
        "Tu mando espera respuesta inmediata, pero no hay plazo crítico de vida o muerte.",
        nuevo=True,
    ),
    _caso(
        "🤖 Robot soldador de una fábrica",
        "Un controlador con un solo procesador mueve un brazo soldador con precisión "
        "de milisegundos, ejecutando un único programa de control. Recibe las órdenes "
        "de producción desde la red de la fábrica.",
        [RT, MONO_U, MONO_P, MONO_CPU, RED],
        "Tiempo de respuesta",
        "El movimiento debe cumplir plazos exactos; una soldadura fuera de tiempo estropea la pieza.",
        "¿Qué pasa si la soldadura llega tarde?",
        nuevo=True,
    ),
]

# Nota que se muestra en el juego (copiada de la tarea)
NOTA_SUPUESTOS = (
    "Cuando el enunciado no da un dato (por ejemplo usuarios en el banco, o simétrico/"
    "asimétrico en los grandes equipos centrales), se supone lo más habitual en un equipo de ese tipo."
)


# ---------------------------------------------------------------------------
# Verdadero o falso (8 de la tarea + 8 extra)
# ---------------------------------------------------------------------------
VERDADERO_FALSO = [
    ("Un sistema multiusuario tiene que ser también de multiprogramación.", True,
     "Varios usuarios a la vez obligan a tener programas de todos en memoria y a repartirse la CPU: eso es multiprogramación."),
    ("Un sistema de tiempo real es, simplemente, un sistema muy rápido.", False,
     "Tiempo real no significa velocidad, sino garantizar la respuesta dentro de un plazo máximo."),
    ("Un ordenador con un procesador de un solo núcleo no puede ser de multiprogramación.", False,
     "La multiprogramación alterna procesos en un solo núcleo conmutando muy rápido; no necesita varios procesadores."),
    ("En el multiproceso asimétrico todos los procesadores pueden hacer cualquier tarea.", False,
     "Eso describe el simétrico. En el asimétrico hay un procesador maestro que reparte el trabajo."),
    ("Un sistema en red y un sistema distribuido son lo mismo.", False,
     "En red, cada equipo tiene su propio SO y comparte recursos; en distribuido, varios equipos funcionan como un único sistema transparente."),
    ("El procesamiento por lotes ya no se usa hoy en día.", False,
     "Se sigue usando en tareas sin interacción: nóminas, facturación y copias de seguridad nocturnas."),
    ("MS-DOS era un sistema monousuario y de monoprogramación.", True,
     "MS-DOS atendía a un solo usuario y ejecutaba un programa a la vez, sin multitarea."),
    ("Los sistemas de tiempo compartido son un tipo de sistema interactivo.", True,
     "El tiempo compartido reparte la CPU en turnos cortos para que cada usuario perciba respuesta inmediata."),
    # ------------------------- EXTRA -------------------------
    ("Un sistema monoproceso no puede ser interactivo.", False,
     "Interactivo habla del tiempo de respuesta, no del número de procesadores. El MS-DOS de 1985 era monoproceso e interactivo."),
    ("Linux es un sistema operativo multiusuario.", True,
     "Permite varias cuentas con sus permisos y varias sesiones simultáneas (por ejemplo por SSH)."),
    ("En multiprogramación, con un solo núcleo, dos programas se ejecutan literalmente en el mismo instante.", False,
     "Se alternan tan rápido que parece que van a la vez, pero en cada instante la CPU ejecuta solo uno."),
    ("En un sistema distribuido, el usuario percibe un único sistema aunque haya muchas máquinas.", True,
     "Esa transparencia es justo lo que lo diferencia de un sistema en red."),
    ("Un sistema por lotes necesita que el usuario esté delante esperando el resultado.", False,
     "Al contrario: los trabajos se ejecutan sin interacción y el resultado se recoge después."),
    ("En un sistema de tiempo real, entregar un resultado correcto pero tarde puede considerarse un fallo.", True,
     "Lo importante es cumplir el plazo garantizado, no solo que el resultado sea correcto."),
    ("Un sistema operativo monousuario no puede ser de multiprogramación.", False,
     "Windows 11 en tu portátil es monousuario y tiene navegador, Spotify y Word abiertos a la vez."),
    ("En un sistema en red, todos los equipos comparten un único sistema operativo.", False,
     "Cada equipo tiene su propio SO; lo que se comparte son recursos (impresoras, carpetas, servicios)."),
]


# ---------------------------------------------------------------------------
# Quiz de teoría (opción múltiple). "correcta" = posición en "opciones"
# ---------------------------------------------------------------------------
QUIZ = [
    {
        "enunciado": "En el multiproceso asimétrico, ¿quién ejecuta el sistema operativo y reparte el trabajo?",
        "opciones": ["Cualquier procesador", "Un procesador maestro", "El usuario", "La memoria RAM"],
        "correcta": 1,
        "explicacion": "En el asimétrico hay un maestro; los demás procesadores ejecutan lo que se les asigna.",
    },
    {
        "enunciado": "¿Cuál es el ejemplo típico de sistema de tiempo real?",
        "opciones": ["Un editor de texto", "El airbag de un coche", "Una copia de seguridad nocturna", "Un navegador web"],
        "correcta": 1,
        "explicacion": "El airbag debe dispararse dentro de un plazo garantizado: un retraso es un fallo grave.",
    },
    {
        "enunciado": "¿Qué tipo de trabajo es típico del procesamiento por lotes?",
        "opciones": ["Jugar online", "Calcular las nóminas de una empresa de noche", "Escribir un correo", "Videollamada"],
        "correcta": 1,
        "explicacion": "Son trabajos masivos que se ejecutan sin interacción del usuario.",
    },
    {
        "enunciado": "¿Qué característica define al tiempo compartido?",
        "opciones": [
            "Un solo usuario usa toda la CPU",
            "La CPU se reparte en turnos muy cortos entre los usuarios o procesos",
            "El sistema solo funciona de noche",
            "Todos los procesadores son distintos",
        ],
        "correcta": 1,
        "explicacion": "El reparto en turnos cortos da a cada usuario la sensación de respuesta inmediata.",
    },
    {
        "enunciado": "¿Qué es el «quantum» en un sistema de tiempo compartido?",
        "opciones": [
            "Un tipo de procesador",
            "El tiempo máximo que un proceso usa la CPU antes de cederla",
            "Un virus informático",
            "La capacidad del disco",
        ],
        "correcta": 1,
        "explicacion": "Es el intervalo de CPU asignado a cada proceso en cada turno.",
    },
    {
        "enunciado": "¿Cómo se llama el cambio de un proceso a otro en la CPU?",
        "opciones": ["Cambio de contexto", "Reinicio de sistema", "Desfragmentación", "Arranque en frío"],
        "correcta": 0,
        "explicacion": "El SO guarda el estado del proceso que sale y carga el del que entra.",
    },
    {
        "enunciado": "¿Qué sistema es monousuario y de monoprogramación?",
        "opciones": ["Linux en un servidor", "Windows 11", "MS-DOS", "Android"],
        "correcta": 2,
        "explicacion": "MS-DOS atendía a un usuario y ejecutaba un programa a la vez.",
    },
    {
        "enunciado": "En un sistema de red, ¿qué tiene cada equipo?",
        "opciones": ["Su propio sistema operativo", "Un único sistema operativo para todos", "Ningún sistema operativo", "Solo teclado y pantalla"],
        "correcta": 0,
        "explicacion": "Cada equipo tiene su SO y comparte recursos con los demás.",
    },
    {
        "enunciado": "Un terminal con solo teclado y pantalla conectado a un gran ordenador es típico de un sistema…",
        "opciones": ["Centralizado", "Distribuido", "De tiempo real", "Asimétrico"],
        "correcta": 0,
        "explicacion": "Todo el trabajo lo hace el ordenador central; el terminal no procesa nada.",
    },
    {
        "enunciado": "¿Qué distingue a un sistema distribuido?",
        "opciones": [
            "Que tiene muchas pantallas",
            "Que varios equipos funcionan como un único sistema transparente para el usuario",
            "Que solo tiene un procesador",
            "Que no usa red",
        ],
        "correcta": 1,
        "explicacion": "La transparencia (el usuario no sabe dónde se ejecuta ni dónde se guarda) es la clave.",
    },
    {
        "enunciado": "Un móvil con 4 núcleos potentes y 4 de bajo consumo, donde cualquier núcleo ejecuta el SO, es…",
        "opciones": ["Multiproceso asimétrico", "Multiproceso simétrico", "Monoproceso", "Distribuido"],
        "correcta": 1,
        "explicacion": "Lo que cuenta es quién reparte el trabajo, no la potencia de cada núcleo.",
    },
    {
        "enunciado": "¿Cuántos tipos de cada criterio tiene a la vez un mismo sistema operativo?",
        "opciones": ["Todos los tipos", "Uno de cada criterio", "Solo uno en total", "Depende del fabricante"],
        "correcta": 1,
        "explicacion": "Un SO pertenece a la vez a un tipo de cada uno de los 5 criterios.",
    },
]


# ---------------------------------------------------------------------------
# Caso práctico: la clínica dental (opción múltiple)
# ---------------------------------------------------------------------------
CLINICA = [
    {
        "enunciado": "🦷 **Recepción:** 3 PC donde se dan las citas y se cobra a los pacientes.",
        "opciones": [
            "Tiempo real, multiusuario y distribuido",
            "Interactivo, monousuario, multiprogramación y en red",
            "Por lotes, monousuario y centralizado",
            "Distribuido y asimétrico",
        ],
        "correcta": 1,
        "explicacion": "Cada PC lo usa una sola persona que necesita respuesta inmediata, y están conectados en red.",
    },
    {
        "enunciado": "🦷 **Servidor de historiales:** guarda las fichas y los 4 dentistas lo consultan a la vez desde sus consultas.",
        "opciones": [
            "Monousuario y por lotes",
            "Multiusuario, interactivo (tiempo compartido) y multiprogramación",
            "Tiempo real y monoprogramación",
            "Monoproceso y centralizado sin usuarios",
        ],
        "correcta": 1,
        "explicacion": "Criterio clave: usuarios. 4 dentistas a la vez, cada uno con su cuenta y permisos.",
    },
    {
        "enunciado": "🦷 **Aparato de rayos X:** debe disparar exactamente el tiempo programado (por ejemplo 0,2 s).",
        "opciones": ["Por lotes", "Interactivo", "Tiempo real", "Distribuido"],
        "correcta": 2,
        "explicacion": "El disparo debe cumplir un plazo exacto y garantizado: un error de tiempo daría una dosis incorrecta.",
    },
    {
        "enunciado": "🦷 **Copia de seguridad:** cada noche se copian todos los historiales y facturas, sin nadie presente.",
        "opciones": ["Tiempo real", "Por lotes", "Interactivo", "Multiproceso asimétrico"],
        "correcta": 1,
        "explicacion": "Es una tarea programada que se ejecuta sola, sin interacción con ningún usuario.",
    },
    {
        "enunciado": "🦷 **Segunda clínica:** se abre otra sede en otra ciudad y las dos trabajan con los mismos historiales. Cada sede tiene sus propios equipos y SO.",
        "opciones": ["Sistema en red", "Sistema distribuido", "Sistema centralizado", "Sistema de tiempo real"],
        "correcta": 0,
        "explicacion": "Se conectan para compartir historiales, pero cada sede sigue con sus equipos y su SO. Sería distribuido solo si funcionaran como una única máquina transparente.",
    },
]


# ---------------------------------------------------------------------------
# Chuleta de teoría
# ---------------------------------------------------------------------------
CHULETA = """
### Los 5 criterios

| Criterio | Tipos |
|---|---|
| **1. Tiempo de respuesta** | Por lotes · Interactivo (tiempo compartido) · Tiempo real |
| **2. Número de usuarios** | Monousuario · Multiusuario |
| **3. Número de procesos** | Monoprogramación · Multiprogramación |
| **4. Número de procesadores** | Monoproceso · Multiproceso (simétrico o asimétrico) |
| **5. Trabajo en red** | Centralizado · En red · Distribuido |

> Un mismo SO pertenece a la vez a **un tipo de cada criterio**.

### Trucos rápidos

- **Tiempo real** → no es «rápido», es **plazo garantizado**.
- **Por lotes** → sin interacción (nóminas, copias nocturnas).
- **Multiusuario** → varias cuentas a la vez; obliga a multiprogramación.
- **Multiprogramación** → se puede dar con **un solo núcleo** (los procesos se alternan).
- **Simétrico** → cualquier procesador ejecuta el SO. **Asimétrico** → hay un **maestro**.
- **En red** → cada equipo con su SO. **Distribuido** → varios equipos = **un único sistema transparente**.
- **Centralizado** → todo el trabajo en un ordenador; los terminales solo tienen teclado y pantalla.
"""
