# 🖥️ SO Quest

Juego interactivo hecho con **Streamlit** para practicar la **clasificación de sistemas operativos**
según los 5 criterios: tiempo de respuesta, número de usuarios, número de procesos,
número de procesadores y trabajo en red.

Basado en la tarea *Clasificación de sistemas operativos* (IES Virgen Espino).

## 🎮 Modos de juego

| Modo | Qué hace |
|---|---|
| 🧩 Clasifica el caso | 17 casos reales (10 de la tarea + 7 extra: Smart TV, marcapasos, clúster, cajero, Raspberry Pi, consola, robot soldador). Eliges un tipo para cada criterio. |
| ✅ Verdadero o falso | 16 afirmaciones (8 de la tarea + 8 extra) con explicación. |
| 🧠 Quiz de teoría | 12 preguntas: quantum, cambio de contexto, simétrico vs asimétrico… |
| 🦷 Clínica dental | El caso práctico de la tarea en formato test. |
| ⚡ Reto mixto | 10 preguntas al azar y nota final. |
| 📖 Chuleta | Resumen de teoría. |

Incluye puntos, racha 🔥, niveles (de *Novato* a *Kernel Master*) y precisión.

## 📁 Estructura

```
├── app.py            # Interfaz y lógica del juego
├── preguntas.py      # Banco de casos y preguntas (aquí se añade contenido)
├── requirements.txt  # Dependencias
└── README.md
```

## ▶️ Ejecutar en local

```bash
git clone https://github.com/TU_USUARIO/so-quest.git
cd so-quest
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Publicarlo gratis (Streamlit Community Cloud)

1. Sube este proyecto a un repositorio de GitHub.
2. Entra en <https://share.streamlit.io> e inicia sesión con GitHub.
3. Pulsa **Create app**, elige tu repositorio, rama `main` y archivo principal `app.py`.
4. Pulsa **Deploy**. Recibirás un enlace público para compartir.

## ➕ Añadir tus propias preguntas

Edita `preguntas.py`:

- **Caso nuevo**: copia una llamada a `_caso(...)` en la lista `CASOS`.
- **Verdadero/falso**: añade una tupla `("afirmación", True/False, "explicación")`.
- **Quiz**: añade un diccionario con `enunciado`, `opciones`, `correcta` (posición) y `explicacion`.

## 👥 Autores

Manuel Ramos Perca · Joel Flores Lopez
