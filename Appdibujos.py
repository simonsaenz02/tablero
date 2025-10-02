import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Título principal
st.title("🌌 Tablero de Energías")
st.markdown("""
Dibuja tu energía interior.  
Cada color refleja un estado distinto de tu ser.  
""")

# Mostrar significados de los colores en columnas
st.subheader("🌈 Paleta de Energías")
cols = st.columns(5)

with cols[0]:
    st.markdown("🔴 **Rojo** = Energía vital, impulso")
    st.markdown("🟡 **Amarillo** = Alegría y claridad")import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Título principal
st.title("🌌 Tablero de Energías")
st.markdown("""
Dibuja tu energía interior.  
Cada color refleja un estado distinto de tu ser.  
""")

# Paleta de energías en una sola oración
st.subheader("🌈 Paleta de Energías")
st.markdown(
"🔴 **Rojo = Energía vital, impulso**, "
"🟡 **Amarillo = Alegría y claridad**, "
"🔵 **Azul = Paz y calma interior**, "
"🟠 **Naranja = Transformación y cambio**, "
"🟢 **Verde = Renacimiento y esperanza**, "
"🟣 **Morado = Intuición y sabiduría**, "
"⚪ **Blanco = Pureza y nuevos comienzos**, "
"⚫ **Negro = Misterio y fuerza**, "
"🌫️ **Gris = Intranquilidad y transición**, "
"🤎 **Café = Estancamiento y desaliento**, "
"🌸 **Rosado = Afecto y sensibilidad**."
)

# ============================
# Panel lateral
# ============================
with st.sidebar:
    st.subheader("🔮 Personaliza tu Energía")
    
    st.subheader("Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)
    
    drawing_mode = st.selectbox(
        "Herramienta de Energía:",
        ("freedraw", "line", "rect", "circle", "polygon", "point", "transform"),
    )
    
    stroke_width = st.slider("Intensidad del trazo", 1, 30, 15)
    stroke_color = st.color_picker("Selecciona el color de tu energía", "#FFFFFF")
    bg_color = st.color_picker("Color del fondo (tu universo)", "#000000")

# ============================
# Canvas
# ============================
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)

st.divider()
st.markdown("✨ No pienses demasiado en lo que dibujas. "
            "Deja que tus trazos fluyan, y observa qué colores emergen: "
            "esa es la vibración de tu energía en este momento.")


with cols[1]:
    st.markdown("🔵 **Azul** = Paz y calma interior")
    st.markdown("🟠 **Naranja** = Transformación y cambio")

with cols[2]:
    st.markdown("🟢 **Verde** = Renacimiento y esperanza")
    st.markdown("🟣 **Morado** = Intuición y sabiduría")

with cols[3]:
    st.markdown("⚪ **Blanco** = Pureza y nuevos comienzos")
    st.markdown("⚫ **Negro** = Misterio y fuerza")

with cols[4]:
    st.markdown("🌫️ **Gris** = Intranquilidad y transición")
    st.markdown("🤎 **Café** = Estancamiento y desaliento")
    st.markdown("🌸 **Rosado** = Afecto y sensibilidad")

# ============================
# Panel lateral
# ============================
with st.sidebar:
    st.subheader("🔮 Personaliza tu Energía")
    
    st.subheader("Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)
    
    drawing_mode = st.selectbox(
        "Herramienta de Energía:",
        ("freedraw", "line", "rect", "circle", "polygon", "point", "transform"),
    )
    
    stroke_width = st.slider("Intensidad del trazo", 1, 30, 15)
    stroke_color = st.color_picker("Selecciona el color de tu energía", "#FFFFFF")
    bg_color = st.color_picker("Color del fondo (tu universo)", "#000000")

# ============================
# Canvas
# ============================
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)

st.divider()
st.markdown("✨ No pienses demasiado en lo que dibujas. "
            "Deja que tus trazos fluyan, y observa qué colores emergen: "
            "esa es la vibración de tu energía en este momento.")
