"""
SO Quest 🖥️ · Juego interactivo sobre la clasificación de sistemas operativos.
Ejecutar con:  streamlit run app.py
"""
import random

import streamlit as st

from preguntas import (
    CASOS,
    CHULETA,
    CLINICA,
    CRITERIOS,
    NOTA_SUPUESTOS,
    QUIZ,
    VERDADERO_FALSO,
)

st.set_page_config(page_title="SO Quest", page_icon="🖥️", layout="centered")

# ---------------------------------------------------------------------------
# Configuración del juego
# ---------------------------------------------------------------------------
PUNTOS_CRITERIO = 2      # puntos por cada criterio acertado al clasificar
BONUS_PERFECTO = 4       # extra si aciertas los 5 criterios
PUNTOS_PREGUNTA = 5      # puntos por pregunta de opción múltiple / V-F
TAM_RETO = 10            # preguntas del reto mixto

NIVELES = [
    (0, "Novato 🐣"),
    (30, "Aprendiz 💻"),
    (80, "Técnico 🛠️"),
    (150, "Administrador 🧑‍💻"),
    (250, "Kernel Master 👑"),
]

MODOS = [
    "🏠 Inicio",
    "🧩 Clasifica el caso",
    "✅ Verdadero o falso",
    "🧠 Quiz de teoría",
    "🦷 Clínica dental",
    "⚡ Reto mixto",
    "📖 Chuleta",
]

# Convertimos V/F y clínica al mismo formato que el quiz para reutilizar código
VF_ITEMS = [
    {
        "enunciado": afirmacion,
        "opciones": ["Verdadero", "Falso"],
        "correcta": 0 if es_verdadera else 1,
        "explicacion": explicacion,
        "barajar": False,
    }
    for afirmacion, es_verdadera, explicacion in VERDADERO_FALSO
]
POOL_RETO = QUIZ + CLINICA + VF_ITEMS


# ---------------------------------------------------------------------------
# Estado y puntuación
# ---------------------------------------------------------------------------
def iniciar_estado():
    for clave, valor in {"puntos": 0, "racha": 0, "mejor_racha": 0,
                         "aciertos": 0, "intentos": 0}.items():
        st.session_state.setdefault(clave, valor)


def nivel_actual():
    nombre = NIVELES[0][1]
    for minimo, titulo in NIVELES:
        if st.session_state.puntos >= minimo:
            nombre = titulo
    return nombre


def siguiente_nivel():
    for minimo, titulo in NIVELES:
        if st.session_state.puntos < minimo:
            return minimo, titulo
    return None


def registrar(aciertos, intentos, puntos, perfecto):
    s = st.session_state
    s.aciertos += aciertos
    s.intentos += intentos
    s.puntos += puntos
    if perfecto:
        s.racha += 1
        s.mejor_racha = max(s.mejor_racha, s.racha)
    else:
        s.racha = 0


def reiniciar_modo(modo):
    for clave in [k for k in st.session_state if k.startswith(f"{modo}_")]:
        del st.session_state[clave]


def preparar_cola(modo, total, limite=None):
    """Crea (una sola vez) el orden aleatorio de preguntas de un modo."""
    if f"{modo}_orden" not in st.session_state:
        orden = list(range(total))
        random.shuffle(orden)
        st.session_state[f"{modo}_orden"] = orden[:limite] if limite else orden
        st.session_state[f"{modo}_pos"] = 0
        st.session_state[f"{modo}_res"] = None
        st.session_state[f"{modo}_ok"] = 0


def avanzar(modo):
    st.session_state[f"{modo}_pos"] += 1
    st.session_state[f"{modo}_res"] = None


def pantalla_final(modo, titulo):
    orden = st.session_state[f"{modo}_orden"]
    ok = st.session_state[f"{modo}_ok"]
    total = len(orden)
    st.success(f"🏁 ¡{titulo} completado! Has acertado **{ok} de {total}**.")
    if ok / total >= 0.8:
        st.balloons()
        st.write("Nota: **Sobresaliente** 🎉")
    elif ok / total >= 0.5:
        st.write("Nota: **Aprobado**, ¡pero puedes mejorarlo! 💪")
    else:
        st.write("Nota: **A repasar** la chuleta 📖 y volver a intentarlo.")
    st.button("🔁 Jugar otra vez", on_click=reiniciar_modo, args=(modo,), key=f"again_{modo}")


# ---------------------------------------------------------------------------
# Barra lateral
# ---------------------------------------------------------------------------
def barra_lateral():
    s = st.session_state
    st.sidebar.title("🖥️ SO Quest")
    modo = st.sidebar.radio("Elige modo de juego", MODOS, key="modo_menu")
    st.sidebar.divider()
    st.sidebar.metric("Puntos", s.puntos)
    c1, c2 = st.sidebar.columns(2)
    c1.metric("Racha 🔥", s.racha)
    c2.metric("Mejor racha", s.mejor_racha)
    precision = (s.aciertos / s.intentos * 100) if s.intentos else 0
    st.sidebar.write(f"**Nivel:** {nivel_actual()}")
    st.sidebar.write(f"**Precisión:** {precision:.0f}% ({s.aciertos}/{s.intentos})")
    prox = siguiente_nivel()
    if prox:
        minimo, titulo = prox
        st.sidebar.progress(min(s.puntos / minimo, 1.0))
        st.sidebar.caption(f"Te faltan {minimo - s.puntos} puntos para {titulo}")
    else:
        st.sidebar.caption("¡Nivel máximo alcanzado!")
    if st.sidebar.button("🗑️ Reiniciar todo"):
        st.session_state.clear()
        st.rerun()
    return modo


# ---------------------------------------------------------------------------
# Modo: clasificar casos (5 criterios)
# ---------------------------------------------------------------------------
def modo_clasificador():
    modo = "clas"
    st.header("🧩 Clasifica el caso")
    st.caption("Elige un tipo para cada uno de los 5 criterios. "
               f"{PUNTOS_CRITERIO} puntos por criterio + {BONUS_PERFECTO} de bonus si aciertas los 5.")
    preparar_cola(modo, len(CASOS))
    pos = st.session_state[f"{modo}_pos"]
    orden = st.session_state[f"{modo}_orden"]
    if pos >= len(orden):
        pantalla_final(modo, "Clasificador")
        return

    idx = orden[pos]
    caso = CASOS[idx]
    st.progress(pos / len(orden), text=f"Caso {pos + 1} de {len(orden)}")
    st.subheader(caso["titulo"] + ("  🆕" if caso["nuevo"] else ""))
    st.info(caso["enunciado"])

    res = st.session_state[f"{modo}_res"]
    if res is None:
        with st.expander("💡 Pista"):
            st.write(caso["pista"])
        with st.form(f"form_clas_{idx}"):
            elegido = {}
            for clave, crit in CRITERIOS.items():
                elegido[clave] = st.selectbox(
                    crit["nombre"], crit["opciones"], index=None,
                    placeholder="Elige una opción…", key=f"clas_{idx}_{clave}",
                )
            enviar = st.form_submit_button("Comprobar ✅", type="primary")
        if enviar:
            if None in elegido.values():
                st.warning("Responde los 5 criterios antes de comprobar.")
            else:
                aciertos = sum(elegido[k] == caso["respuesta"][k] for k in CRITERIOS)
                perfecto = aciertos == len(CRITERIOS)
                puntos = aciertos * PUNTOS_CRITERIO + (BONUS_PERFECTO if perfecto else 0)
                registrar(aciertos, len(CRITERIOS), puntos, perfecto)
                st.session_state[f"{modo}_ok"] += 1 if perfecto else 0
                st.session_state[f"{modo}_res"] = {
                    "elegido": elegido, "aciertos": aciertos,
                    "puntos": puntos, "perfecto": perfecto,
                }
                st.rerun()
    else:
        if res["perfecto"]:
            st.success(f"🎯 ¡Perfecto! 5/5 · +{res['puntos']} puntos")
        else:
            st.error(f"Has acertado {res['aciertos']}/5 · +{res['puntos']} puntos")
        filas = []
        for clave, crit in CRITERIOS.items():
            correcta = caso["respuesta"][clave]
            tu = res["elegido"][clave]
            filas.append({
                "Criterio": crit["nombre"],
                "Tu respuesta": tu,
                "Correcta": correcta,
                "": "✅" if tu == correcta else "❌",
            })
        st.dataframe(filas, hide_index=True)
        st.markdown(f"**Criterio clave: {caso['clave']}.** {caso['justificacion']}")
        st.caption(NOTA_SUPUESTOS)
        st.button("Siguiente caso ➡️", on_click=avanzar, args=(modo,), type="primary")


# ---------------------------------------------------------------------------
# Modo genérico: preguntas de opción múltiple (quiz, V/F, clínica, reto)
# ---------------------------------------------------------------------------
def modo_opciones(modo, titulo, items, limite=None, descripcion=""):
    st.header(titulo)
    if descripcion:
        st.caption(descripcion)
    preparar_cola(modo, len(items), limite)
    pos = st.session_state[f"{modo}_pos"]
    orden = st.session_state[f"{modo}_orden"]
    if pos >= len(orden):
        pantalla_final(modo, titulo)
        return

    idx = orden[pos]
    item = items[idx]
    st.progress(pos / len(orden), text=f"Pregunta {pos + 1} de {len(orden)}")
    st.markdown(f"### {item['enunciado']}")

    # Opciones barajadas de forma estable (no cambian al recargar la página)
    opciones = list(item["opciones"])
    texto_correcto = opciones[item["correcta"]]
    if item.get("barajar", True):
        random.Random(f"{modo}-{idx}").shuffle(opciones)

    res = st.session_state[f"{modo}_res"]
    if res is None:
        with st.form(f"form_{modo}_{pos}"):
            eleccion = st.radio("Tu respuesta", opciones, index=None,
                                key=f"{modo}_radio_{pos}")
            enviar = st.form_submit_button("Comprobar ✅", type="primary")
        if enviar:
            if eleccion is None:
                st.warning("Elige una opción primero.")
            else:
                ok = eleccion == texto_correcto
                registrar(1 if ok else 0, 1, PUNTOS_PREGUNTA if ok else 0, ok)
                st.session_state[f"{modo}_ok"] += 1 if ok else 0
                st.session_state[f"{modo}_res"] = {"eleccion": eleccion, "ok": ok}
                st.rerun()
    else:
        if res["ok"]:
            st.success(f"✅ ¡Correcto! +{PUNTOS_PREGUNTA} puntos")
        else:
            st.error(f"❌ Has elegido «{res['eleccion']}». La correcta era: **{texto_correcto}**")
        st.info(item["explicacion"])
        st.button("Siguiente ➡️", on_click=avanzar, args=(modo,), type="primary")


# ---------------------------------------------------------------------------
# Inicio y chuleta
# ---------------------------------------------------------------------------
def pantalla_inicio():
    st.title("🖥️ SO Quest")
    st.subheader("Clasificación de sistemas operativos")
    st.write(
        "Aprende y practica los **5 criterios** para clasificar un sistema operativo "
        "(tiempo de respuesta, usuarios, procesos, procesadores y red) jugando."
    )
    c1, c2, c3 = st.columns(3)
    c1.metric("Casos para clasificar", len(CASOS))
    c2.metric("Verdadero o falso", len(VF_ITEMS))
    c3.metric("Preguntas de quiz", len(QUIZ) + len(CLINICA))
    st.markdown(
        """
**Modos de juego**
- 🧩 **Clasifica el caso**: elige un tipo de cada criterio y descubre tus fallos.
- ✅ **Verdadero o falso**: cuidado, algunas parecen ciertas a primera vista.
- 🧠 **Quiz de teoría**: conceptos como quantum, cambio de contexto o simétrico vs asimétrico.
- 🦷 **Clínica dental**: elige el SO adecuado para cada necesidad.
- ⚡ **Reto mixto**: 10 preguntas al azar para ver tu nota final.
        """
    )
    st.info("👈 Elige un modo en el menú de la izquierda para empezar.")


def pantalla_chuleta():
    st.header("📖 Chuleta")
    st.markdown(CHULETA)


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------
def main():
    iniciar_estado()
    modo = barra_lateral()
    if modo == MODOS[0]:
        pantalla_inicio()
    elif modo == MODOS[1]:
        modo_clasificador()
    elif modo == MODOS[2]:
        modo_opciones("vf", "✅ Verdadero o falso", VF_ITEMS,
                      descripcion="¿Verdadero o falso? Cuidado con las trampas.")
    elif modo == MODOS[3]:
        modo_opciones("quiz", "🧠 Quiz de teoría", QUIZ,
                      descripcion="Preguntas de opción múltiple sobre los conceptos clave.")
    elif modo == MODOS[4]:
        modo_opciones("clinica", "🦷 Clínica dental", CLINICA,
                      descripcion="Una clínica quiere informatizarse: elige el SO adecuado.")
    elif modo == MODOS[5]:
        modo_opciones("reto", "⚡ Reto mixto", POOL_RETO, limite=TAM_RETO,
                      descripcion=f"{TAM_RETO} preguntas al azar de todos los bloques.")
    else:
        pantalla_chuleta()


main()
