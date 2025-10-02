import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Título principal
st.title("🌌 Tablero de Energías")
st.markdown("""
Dibuja tu energía interior.  
Cada color refleja un estado distinto de tu ser.  

**Rojo = Energía vital, impulso**  
**Azul = Paz y calma interior**  
**Verde = Renacimiento y esperanza**  
**Amarillo = Alegría y claridad**  
**Naranja = Transformación y cambio**  
**Morado = Intuición y sabiduría**  
**Blanco = Pureza y nuevos comienzos**  
**Negro = Misterio y fuerza**  
**Gris = Intranquilidad y transición**  
**Rosado = Afecto y sensibilidad**
**Café = Estancamiento y desaliento**
""")

with st.sidebar:
    st.subheader("🔮 Personaliza tu Energía")
    
    # Canvas dimensions
    st.subheader("Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)
    
    # Drawing mode
    drawing_mode = st.selectbox(
        "Herramienta de Energía:",
        ("freedraw", "line", "rect", "circle", "polygon", "point", "transform"),
    )
    
    # Stroke width
    stroke_width = st.slider("Intensidad del trazo", 1, 30, 15)
    
    # Stroke color
    stroke_color = st.color_picker("Selecciona el color de tu energía", "#FFFFFF")
    
    # Background color
    bg_color = st.color_picker("Color del fondo (tu universo)", "#000000")

# Canvas
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
st.markdown("✨No pienses demasiado en lo que dibujas. "
            "Deja que tus trazos fluyan, y observa qué colores emergen: "
            "esa es la vibración de tu energía en este momento.")
