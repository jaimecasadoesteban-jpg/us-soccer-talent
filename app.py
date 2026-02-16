import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="US Soccer Talent & Strategy",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS PERSONALIZADO AVANZADO (ESTÉTICA NEON/FUT)
st.markdown("""
    <style>
    /* Importamos una fuente potente de Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');

    /* Fondo general con degradado sutil */
    .stApp {
        background: linear-gradient(to bottom right, #000000, #0e1117, #1c1c1c);
        color: #ffffff;
        font-family: 'Montserrat', sans-serif;
    }

    /* Títulos agresivos con efecto neón */
    h1 {
        font-family: 'Montserrat', sans-serif;
        font-weight: 900 !important;
        text-transform: uppercase;
        letter-spacing: -1px;
        color: #ffffff !important;
        text-shadow: 0 0 10px #00ff41, 0 0 20px #00ff41; /* Glow verde */
        font-size: 3rem !important;
    }
    
    h2, h3 {
        font-family: 'Montserrat', sans-serif;
        font-weight: 700 !important;
        text-transform: uppercase;
        color: #00ff41 !important; /* Texto verde */
    }

    /* Subtítulos más limpios */
    .stMarkdown p {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #d1d5db; /* Gris claro para leer mejor */
    }

    /* Botones estilo "Cyberpunk" */
    .stButton>button {
        background: linear-gradient(45deg, #00ff41, #00c232);
        color: #000000;
        font-family: 'Montserrat', sans-serif;
        font-weight: 900;
        border-radius: 4px;
        border: none;
        padding: 15px 40px;
        text-transform: uppercase;
        box-shadow: 0 4px 15px rgba(0, 255, 65, 0.4); /* Sombra verde */
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05); /* Crece un poco al pasar el ratón */
        box-shadow: 0 6px 20px rgba(0, 255, 65, 0.6);
    }

    /* Tarjetas de métricas estilo FUT */
    .metric-card {
        background: linear-gradient(135deg, #1f2937, #111827);
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #374151;
        border-left: 5px solid #00ff41;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s;
    }
    .metric-card:hover {
         transform: translateY(-5px); /* Se levanta al pasar el ratón */
         border-color: #00ff41;
         box-shadow: 0 0 20px rgba(0, 255, 65, 0.2);
    }
    .metric-card h1 {
        font-size: 2rem !important;
        margin-bottom: 0px;
        text-shadow: none; /* Quitamos el neón de los textos pequeños de las tarjetas */
        color: #ffffff !important;
    }
    .metric-card p {
        color: #00ff41;
        font-weight: 700;
        letter-spacing: 1px;
        font-size: 0.9rem;
    }

    /* Inputs del formulario más modernos */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #111827;
        color: white;
        border: 1px solid #374151;
        border-radius: 4px;
    }
    .stTextInput>div>div>input:focus {
        border-color: #00ff41;
        box-shadow: 0 0 5px #00ff41;
    }
    
    /* Ajuste para la imagen principal */
    .hero-image {
        border-radius: 12px;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 10px 10px -5px rgba(0, 0, 0, 0.1);
        border: 2px solid #374151;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SECCIÓN 1: HERO (IMPACTO VISUAL MEJORADO) ---
col1, col2 = st.columns([1.2, 1], gap="large") # Un poco más de espacio para el texto

with col1:
    # Usamos HTML directo para el título principal para control total del estilo
    st.markdown('<h1>TU TALENTO EN ESPAÑA.<br><span style="color:#00ff41;">TU FUTURO EN USA.</span></h1>', unsafe_allow_html=True)
    st.write("""
    ### US SOCCER TALENT & STRATEGY
    
    Olvídate de los intermediarios tradicionales. Somos la primera agencia impulsada por **Business Analytics** e **Inteligencia Artificial**.
    
    Yo juego en la NCAA D1 ahora mismo. Sé lo que buscan. Te analizo con datos reales y te conecto directamente. Sin humo.
    """)
    st.write("") # Espacio extra
    st.button("🚀 QUIERO MI ANÁLISIS GRATUITO")

with col2:
    # He cambiado la imagen por una más dramática y le he añadido una clase CSS
    st.markdown('<img src="https://images.unsplash.com/photo-1628891890467-b79f2c8ba9dc?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="hero-image" style="width:100%;">', unsafe_allow_html=True)
    st.caption("Visualiza tu objetivo. URI Soccer Stadium.")

st.markdown("---")

# --- SECCIÓN 2: LA METODOLOGÍA (DATA DRIVEN) ---
st.header("1. NO ADIVINAMOS. MEDIMOS.")
st.write("En USA todo son números. Usamos Big Data para comparar tu rendimiento en España con el nivel real de la NCAA.")

# Simulación de datos 
categories = ['Goles/90min', 'Asistencias', 'Robos', 'Duelos Aéreos', 'Progresión de Balón']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[4.2, 3, 5, 4.5, 3.8],
      theta=categories,
      fill='toself',
      name='TU PROYECCIÓN (Basada en datos)',
      line_color='#00ff41',
      opacity=0.8
))
fig.add_trace(go.Scatterpolar(
      r=[3, 3.5, 2.5, 3, 3],
      theta=categories,
      fill='toself',
      name='Promedio NCAA D1 (Referencia)',
      line_color='#ff0055',
      opacity=0.5
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5],
      gridcolor='#374151', # Color de rejilla más sutil
      linecolor='#374151',
      tickfont=dict(color='white')
    ),
    angularaxis=dict(
      tickfont=dict(color='white', size=12, family='Montserrat'),
      linecolor='#374151'
    ),
    bgcolor='rgba(0,0,0,0)' # Fondo transparente para el gráfico
  ),
  paper_bgcolor='rgba(0,0,0,0)', # Fondo transparente para el papel
  font_color="white",
  showlegend=True,
  legend=dict(
      bgcolor='rgba(17, 24, 39, 0.8)',
      bordercolor='#374151',
      borderwidth=1
  ),
  margin=dict(l=20, r=20, t=20, b=20)
)

c1, c2 = st.columns([1.5, 1], gap="medium")
with c1:
    st.plotly_chart(fig, use_container_width=True)
with c2:
    st.write("") # Espacio para alinear verticalmente
    st.markdown("""
    <div style="background-color: #111827; padding: 20px; border-radius: 10px; border: 1px solid #00ff41;">
        <h3 style="margin-top:0;">¿QUÉ DICE ESTE GRÁFICO?</h3>
        <p style="color: #d1d5db;">Este no es un gráfico cualquiera. Es tu pasaporte.</p>
        <p>El área <strong style="color:#00ff41">VERDE NEÓN</strong> es tu dominio. Si tu huella estadística cubre más área que el promedio rojo de la NCAA, sabemos que estás listo.</p>
        <p>Analizamos métricas avanzadas que los ojeadores tradicionales ignoran.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN 3: LA EXPERIENCIA (TU VIDA EN URI) ---
st.header("2. VIVE EL SUEÑO AMERICANO")
st.write("Soy Jaime. Juego y estudio en University of Rhode Island. Esto no es una oficina, es mi vida diaria. Te enseño el camino que yo ya he recorrido.")

# Métricas rápidas de impacto con estilo mejorado
m1, m2, m3, m4 = st.columns(4)
m1.markdown('<div class="metric-card"><h1>Rhode Island</h1><p>LOCATION (USA)</p></div>', unsafe_allow_html=True)
m2.markdown('<div class="metric-card"><h1>NCAA D1</h1><p>ELITE COMPETITION</p></div>', unsafe_allow_html=True)
m3.markdown('<div class="metric-card"><h1>Analytics</h1><p>MY MAJOR & TOOL</p></div>', unsafe_allow_html=True)
m4.markdown('<div class="metric-card"><h1>Scholarship</h1><p>THE ULTIMATE GOAL</p></div>', unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN 4: CONTACTO (EMBUDO) ---
st.header("3. EMPIEZA TU CAMINO")
st.write("Rellena este formulario. Si tus datos iniciales encajan, agendaremos una videollamada de 5 minutos conmigo.")

with st.form("contact_form"):
    st.write("### 📋 DATOS DEL JUGADOR")
    col_f1, col_f2 = st.columns(2, gap="medium")
    with col_f1:
        name = st.text_input("Nombre Completo")
        team = st.text_input("Equipo Actual y Categoría")
        stats_link = st.text_input("Enlace a Highlights (YouTube/Hudl)")
    with col_f2:
        email = st.text_input("Email")
        position = st.selectbox("Posición Principal", ["Portero", "Defensa Central", "Lateral", "Mediocentro Defensivo", "Mediocentro Ofensivo", "Extremo", "Delantero Centro"])
        phone = st.text_input("Teléfono (WhatsApp)")
    
    st.write("")
    submitted = st.form_submit_button("ENVIAR PERFIL PARA ANÁLISIS")
    if submitted:
        st.success(f"¡Gracias {name}! Hemos recibido tus datos. Si tu perfil encaja, te contactaré en 48h.")
