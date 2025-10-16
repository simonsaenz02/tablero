import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Título principal
st.title("🌌 Mapa Estelar Interactivo")
st.markdown("""
Diseña tu propio cielo estrellado.  
Cada color representa un tipo de astro o fenómeno cósmico que puedes ubicar en tu mapa.  
""")

# Paleta de astros
st.subheader("✨ Paleta Cósmica")
st.markdown(
"🔴 **Rojo = Estrella gigante roja**, "
"🟡 **Amarillo = Estrella joven brillante**, "
"🔵 **Azul = Estrella supercaliente**, "
"🟠 **Naranja = Nebulosa en formación**, "
"🟢 **Verde = Planeta habitable**, "
"🟣 **Morado = Agujero de gusano**, "
"⚪ **Blanco = Luna o cometa**, "
"⚫ **Negro = Región de vacío profundo**, "
"🌫️ **Gris = Polvo interestelar**, "
"🤎 **Café = Asteroides o rocas cósmicas**, "
"🌸 **Rosado = Nebulosa rosada**."
)

# ============================
# Panel lateral
# ============================
with st.sidebar:
    st.subheader("🛰️ Personaliza tu Cielo")
    
    st.subheader("Dimensiones del Mapa")
    canvas_width = st.slider("Ancho del cielo", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del cielo", 200, 600, 300, 50)
    
    drawing_mode = st.selectbox(
        "Herramienta espacial:",
        ("freedraw", "line", "rect", "circle", "polygon", "point", "transform"),
    )
    
    stroke_width = st.slider("Tamaño del trazo estelar", 1, 30, 15)
    stroke_color = st.color_picker("Selecciona el color del astro", "#FFFFFF")
    bg_color = st.color_picker("Color del fondo del universo", "#000000")

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
st.markdown("🌠 Crea tus propias constelaciones y explora el universo a tu manera.")

