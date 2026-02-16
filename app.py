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

# 2. CSS "MIDNIGHT ELITE" (PREMIUM & TECH)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;500;700;900&display=swap');

    /* FONDO CON PROFUNDIDAD (NO NEGRO PLANO) */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #1e293b, #0f172a, #020617);
        color: #f8fafc;
        font-family: 'Montserrat', sans-serif;
    }

    /* TÍTULOS */
    h1 {
        font-weight: 900 !important;
        text-transform: uppercase;
        background: -webkit-linear-gradient(0deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.8rem !important;
        letter-spacing: -2px;
        margin-bottom: 0px;
    }
    
    h2 {
        font-weight: 700 !important;
        color: #ffffff !important;
        font-size: 2.2rem !important;
        border-left: 5px solid #38bdf8; /* Barra azul a la izquierda */
        padding-left: 15px;
        margin-top: 40px;
    }

    h3 {
        color: #94a3b8 !important;
        font-weight: 500 !important;
    }

    /* TEXTO NORMAL */
    p, li, .stMarkdown {
        font-size: 1.15rem;
        color: #cbd5e1; /* Gris azulado muy claro */
        line-height: 1.7;
    }

    /* BOTONES GRADIENTE AZUL/VIOLETA */
    .stButton>button {
        background: linear-gradient(90deg, #0ea5e9, #3b82f6);
        color: white;
        font-weight: 700;
        border: none;
        border-radius: 8px;
        padding: 18px 40px;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.5);
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 30px -5px rgba(59, 130, 246, 0.7);
    }

    /* TARJETAS DE MÉTRICAS (GLASSMORPHISM) */
    .metric-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: all 0.3s;
    }
    .metric-card:hover {
        border-color: #38bdf8;
        transform: translateY(-5px);
        background: rgba(30, 41, 59, 0.9);
    }
    .metric-card h1 {
        font-size: 1.8rem !important;
        background: none;
        -webkit-text-fill-color: white;
        margin-bottom: 5px;
        text-shadow: none;
    }
    .metric-card p {
        color: #38bdf8; /* Cian */
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 700;
    }

    /* INPUTS FORMULARIO */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: rgba(15, 23, 42, 0.6);
        color: white;
        border: 1px solid #334155;
        border-radius: 8px;
        height: 50px;
    }
    .stTextInput>div>div>input:focus {
        border-color: #38bdf8;
        box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }

    /* QUITAMOS EL MARGEN SUPERIOR MOLESTO */
    .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SECCIÓN 1: HERO (IMPACTO) ---
c_hero1, c_hero2 = st.columns([1.3, 1], gap="large")

with c_hero1:
    st.markdown('<p style="color:#38bdf8; font-weight:700; letter-spacing:2px; margin-bottom:0;">US SOCCER TALENT & STRATEGY</p>', unsafe_allow_html=True)
    st.markdown("<h1>TU TALENTO EN ESPAÑA<br>TU FUTURO EN USA</h1>", unsafe_allow_html=True)
    st.write("""
    La primera agencia impulsada por **Business Analytics** y experiencia real en NCAA D1.
    
    Sin intermediarios opacos. Soy Jaime, juego allí y estudio los datos. Te conecto con universidades americanas basándome en tu rendimiento real, no en promesas.
    """)
    st.write("")
    st.button("🚀 INICIAR MI ANÁLISIS")

with c_hero2:
    # Imagen limpia sin caption falso
    st.image("https://images.unsplash.com/photo-1551958219-acbc608c6377?q=80&w=2070&auto=format&fit=crop", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- SECCIÓN 2: DATOS (EL CORAZÓN) ---
st.header("NO ADIVINAMOS. MEDIMOS.")
st.write("En USA, el presupuesto se asigna por estadísticas. Usamos modelos comparativos para traducir tu juego al estándar americano.")

# GRÁFICO MEJORADO (COLORES AZULES)
categories = ['Goles/90min', 'Asistencias', 'Robos', 'Duelos Aéreos', 'Progresión']

fig = go.Figure()

# Tu perfil (Azul cian brillante)
fig.add_trace(go.Scatterpolar(
      r=[4.2, 3, 5, 4.5, 3.8],
      theta=categories,
      fill='toself',
      name='TU PROYECCIÓN',
      line_color='#38bdf8',
      fillcolor='rgba(56, 189, 248, 0.3)',
      marker=dict(size=6)
))

# Promedio (Gris/Blanco sutil)
fig.add_trace(go.Scatterpolar(
      r=[3, 3.5, 2.5, 3, 3],
      theta=categories,
      fill='toself',
      name='Promedio NCAA D1',
      line_color='#94a3b8',
      fillcolor='rgba(148, 163, 184, 0.1)',
      line=dict(dash='dot')
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(visible=True, range=[0, 5], gridcolor='#334155', linecolor='#334155', tickfont=dict(color='#94a3b8')),
    angularaxis=dict(tickfont=dict(color='white', size=12, family='Montserrat'), linecolor='#334155'),
    bgcolor='rgba(0,0,0,0)'
  ),
  paper_bgcolor='rgba(0,0,0,0)',
  font_color="white",
  showlegend=True,
  legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="center", x=0.5), # Leyenda arriba horizontal
  margin=dict(l=40, r=40, t=40, b=20)
)

col_graph1, col_graph2 = st.columns([1.5, 1], gap="medium")
with col_graph1:
    st.plotly_chart(fig, use_container_width=True)
with col_graph2:
    st.markdown("""
    <div style="background: rgba(56, 189, 248, 0.1); border-left: 4px solid #38bdf8; padding: 20px; border-radius: 0 8px 8px 0; margin-top: 40px;">
        <h3 style="color: white !important; margin-top:0;">TU PASAPORTE VISUAL</h3>
        <p>Este gráfico es lo que enviamos a los entrenadores. Ignoran los vídeos largos; miran la huella estadística.</p>
        <p>Si tu área <span style="color:#38bdf8; font-weight:bold;">AZUL</span> cubre el promedio gris, eres un candidato viable para beca completa.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- SECCIÓN 3: REALIDAD (URI) ---
st.header("VIVE EL SUEÑO AMERICANO")
st.write("University of Rhode Island no es solo mi equipo, es el ejemplo de lo que puedes conseguir. Compaginar estudios de alto nivel con deporte de élite.")

# MÉTRICAS ESTILO PREMIUM
m1, m2, m3, m4 = st.columns(4)
m1.markdown('<div class="metric-card"><h1>RHODE ISLAND</h1><p>LOCATION</p></div>', unsafe_allow_html=True)
m2.markdown('<div class="metric-card"><h1>NCAA D1</h1><p>COMPETITION</p></div>', unsafe_allow_html=True)
m3.markdown('<div class="metric-card"><h1>ANALYTICS</h1><p>MY MAJOR</p></div>', unsafe_allow_html=True)
m4.markdown('<div class="metric-card"><h1>SCHOLARSHIP</h1><p>THE GOAL</p></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- SECCIÓN 4: FORMULARIO ---
st.header("EMPIEZA TU CAMINO")
st.write("Completa tu perfil preliminar. Si tus métricas iniciales encajan, agendaremos una llamada estratégica.")

with st.container():
    st.markdown('<div style="background: rgba(15, 23, 42, 0.4); padding: 30px; border-radius: 16px; border: 1px solid #1e293b;">', unsafe_allow_html=True)
    with st.form("contact_form"):
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            name = st.text_input("Nombre Completo", placeholder="Ej: Juan García")
            team = st.text_input("Equipo y Categoría", placeholder="Ej: Rayo Majadahonda - Div. Honor")
            stats = st.text_input("Link a Highlights/Stats", placeholder="Hudl, YouTube o Transfermarkt")
        with c2:
            email = st.text_input("Email de contacto")
            pos = st.selectbox("Posición", ["Portero", "Defensa", "Mediocentro", "Extremo", "Delantero"])
            phone = st.text_input("WhatsApp", placeholder="+34 600 000 000")
        
        st.write("")
        submit = st.form_submit_button("ENVIAR PERFIL A JAIME")
        if submit:
            st.success("Perfil enviado. Analizando datos...")
    st.markdown('</div>', unsafe_allow_html=True)
