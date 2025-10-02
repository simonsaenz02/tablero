import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Título principal
st.title("🌈 Tablero de Energías")
st.markdown("Dibuja tu energía interior: cada color refleja una emoción o estado de ánimo. "
            "Rojo = Pasión ❤️, Azul = Calma 💙, Verde = Esperanza 💚, Amarillo = Alegría 💛")

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
    stroke_color = st.color_picker("Color de tu energía", "#FFFFFF")
    
    # Background color
    bg_color = st.color_picker("Color del fondo", "#000000")

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
st.markdown("✨ **Tip energético**: Usa trazos libres para tu energía fluida, círculos para armonía, "
            "y líneas rectas para equilibrio. ¡Deja que tu tablero refleje cómo te sientes ahora!")
