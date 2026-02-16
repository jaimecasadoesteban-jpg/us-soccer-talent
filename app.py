import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. CONFIGURACIÓN DE PÁGINA (ESTÉTICA DEPORTIVA)
st.set_page_config(
    page_title="US Soccer Talent & Strategy",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS PERSONALIZADO (MODO "DARK/NEON")
# Esto fuerza el fondo oscuro y textos blancos con acentos verdes (tipo campo de fútbol)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: -1px;
    }
    h1 { color: #00ff41; font-size: 3.5rem !important; } /* Verde Neón */
    h2 { color: #ffffff; border-bottom: 2px solid #00ff41; padding-bottom: 10px; }
    .stButton>button {
        background-color: #00ff41;
        color: #000000;
        font-weight: bold;
        border-radius: 0px;
        border: none;
        padding: 15px 30px;
        text-transform: uppercase;
    }
    .metric-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00ff41;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SECCIÓN 1: HERO (IMPACTO) ---
col1, col2 = st.columns([1, 1])

with col1:
    st.title("TU TALENTO EN ESPAÑA. TU FUTURO EN USA.")
    st.write("""
    ### US SOCCER TALENT & STRATEGY
    No somos intermediarios. Somos analistas y jugadores. 
    Te llevamos a la liga universitaria de EE.UU. basándonos en tus datos reales, no en promesas vacías.
    """)
    st.button("🚀 ANALIZA TU PERFIL AHORA")

with col2:
    # Aquí iría una foto tuya de calidad jugando en URI
    st.image("https://images.unsplash.com/photo-1517927033932-b3d18e61fb3a", caption="URI Soccer - Live the Dream", use_container_width=True)

st.markdown("---")

# --- SECCIÓN 2: LA METODOLOGÍA (DATA DRIVEN) ---
st.header("1. NO ADIVINAMOS. MEDIMOS.")
st.write("En USA todo son números. Usamos Big Data para comparar tu rendimiento en España con el nivel real de la NCAA.")

# Simulación de datos (Lo que harás en tu backend)
# 
categories = ['Goles/90min', 'Asistencias', 'Robos', 'Duelos Ganados', 'Distancia Recorrida']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[4, 3, 5, 4, 5],
      theta=categories,
      fill='toself',
      name='Tu Perfil (Proyección)',
      line_color='#00ff41'
))
fig.add_trace(go.Scatterpolar(
      r=[3, 4, 2, 3, 3],
      theta=categories,
      fill='toself',
      name='Promedio NCAA D1',
      line_color='#ff0055'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5],
      gridcolor='#333',
      linecolor='#333'
    ),
    bgcolor='#0e1117'
  ),
  paper_bgcolor='#0e1117',
  font_color="white",
  showlegend=True
)

c1, c2 = st.columns([2, 1])
with c1:
    st.plotly_chart(fig, use_container_width=True)
with c2:
    st.info("""
    **¿QUÉ DICE ESTE GRÁFICO?**
    
    Analizamos métricas clave como **Goles esperados (xG)** y **Duelos defensivos**. 
    
    Si superas el promedio de la liga (Línea Roja), garantizamos que las universidades verán tu perfil.
    """)

st.markdown("---")

# --- SECCIÓN 3: LA EXPERIENCIA (TU VIDA EN URI) ---
st.header("2. VIVE EL SUEÑO AMERICANO")
st.write("Soy Jaime. Juego y estudio en University of Rhode Island. Esto no es una oficina, es mi vida diaria.")

# Métricas rápidas de impacto
m1, m2, m3, m4 = st.columns(4)
m1.markdown('<div class="metric-card"><h1>Rhode Island</h1><p>LOCATION</p></div>', unsafe_allow_html=True)
m2.markdown('<div class="metric-card"><h1>D1 / NCAA</h1><p>COMPETITION</p></div>', unsafe_allow_html=True)
m3.markdown('<div class="metric-card"><h1>Business</h1><p>MAJOR</p></div>', unsafe_allow_html=True)
m4.markdown('<div class="metric-card"><h1>Scholarship</h1><p>GOAL</p></div>', unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN 4: CONTACTO (EMBUDO) ---
st.header("3. EMPIEZA TU CAMINO")
st.write("Rellena este formulario para una evaluación preliminar de 5 minutos.")

with st.form("contact_form"):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        name = st.text_input("Nombre Completo")
        team = st.text_input("Equipo Actual y Categoría")
        stats_link = st.text_input("Enlace a Highlights (YouTube/Hudl)")
    with col_f2:
        email = st.text_input("Email")
        position = st.selectbox("Posición Principal", ["Portero", "Defensa Central", "Lateral", "Mediocentro", "Extremo", "Delantero"])
        phone = st.text_input("Teléfono (WhatsApp)")
    
    submitted = st.form_submit_button("ENVIAR PERFIL")
    if submitted:
        st.success(f"¡Gracias {name}! Hemos recibido tus datos. Si tu perfil encaja, te contactaré en 48h.")
