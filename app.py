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

# 2. DEFINICIÓN DEL POPUP (MODAL)
# Esto hace que el formulario salte en medio de la pantalla
@st.dialog("🚀 ANÁLISIS DE PERFIL - PASO 1")
def show_contact_form():
    st.write("Rellena tus datos básicos. Si el algoritmo detecta viabilidad, te contactaré en 24h.")
    with st.form("popup_form"):
        name = st.text_input("Nombre Completo")
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            team = st.text_input("Equipo y Categoría")
            position = st.selectbox("Posición", ["Portero", "Defensa", "Medio", "Delantero"])
        with col_f2:
            email = st.text_input("Email")
            phone = st.text_input("WhatsApp")
        
        link = st.text_input("Enlace (Transfermarkt / Video)")
        
        if st.form_submit_button("ENVIAR DATOS", use_container_width=True):
            st.success("✅ Recibido. Cierra esta ventana.")

# 3. CSS ESTRICTO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,300;0,600;0,800;1,900&family=Inter:wght@300;400;600&display=swap');

    /* Ocultar elementos sobrantes */
    header {visibility: hidden;}
    .block-container {padding-top: 0rem !important; padding-bottom: 5rem !important; max-width: 100%;}

    /* Fondo */
    .stApp { background-color: #020617; color: #f8fafc; font-family: 'Inter', sans-serif; }

    /* CONTENEDOR VIDEO Y TEXTO */
    .hero-wrapper {
        position: relative;
        height: 90vh; /* Altura pantalla completa */
        width: 100%;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    /* VIDEO DE FONDO */
    .hero-video {
        position: absolute;
        top: 50%;
        left: 50%;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        z-index: 0;
        transform: translate(-50%, -50%);
        filter: brightness(0.3); /* Oscurecer para leer texto */
    }

    /* CONTENIDO SOBRE EL VIDEO */
    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 1000px;
        padding: 20px;
    }

    h1 {
        font-family: 'Kanit', sans-serif;
        font-weight: 900 !important;
        font-style: italic;
        text-transform: uppercase;
        font-size: 5rem !important;
        line-height: 0.9 !important;
        color: white;
        text-shadow: 0 0 30px rgba(0,0,0,0.8);
        margin-bottom: 20px !important;
    }

    .hero-subtitle {
        font-size: 1.3rem;
        color: #e2e8f0;
        margin-bottom: 30px;
        text-shadow: 0 2px 4px black;
    }

    /* LOGOS */
    .logo-container {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 30px;
        flex-wrap: wrap;
    }
    .uni-logo { height: 50px; opacity: 0.7; filter: grayscale(100%) brightness(200%); }

    /* ESTILO BOTÓN */
    .stButton button {
        background: linear-gradient(90deg, #0ea5e9, #2563eb);
        color: white;
        border: none;
        padding: 15px 40px;
        font-family: 'Kanit', sans-serif;
        font-size: 1.2rem;
        text-transform: uppercase;
        font-weight: 700;
        border-radius: 4px;
        box-shadow: 0 0 20px rgba(14, 165, 233, 0.5);
    }
    
    /* CAJAS EXPERIENCIA Y DATOS */
    .glass-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 12px;
        height: 100%;
    }
    .stat-box {
        background: rgba(15, 23, 42, 0.6);
        border-left: 4px solid #38bdf8;
        padding: 20px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION (HTML PURO PARA CONTROLAR VIDEO) ---
st.markdown("""
<div class="hero-wrapper">
    <video autoplay muted loop playsinline class="hero-video">
        <source src="https://videos.pexels.com/video-files/3195239/3195239-uhd_2560_1440_25fps.mp4" type="video/mp4">
    </video>

    <div class="hero-content">
        <p style="color:#38bdf8; font-weight:800; letter-spacing:3px; margin-bottom:10px; font-family:Kanit;">US SOCCER TALENT & STRATEGY</p>
        <h1>TU TALENTO EN ESPAÑA.<br><span style='color:#38bdf8'>TU FUTURO EN USA.</span></h1>
        <p class="hero-subtitle">
            Usamos <b>Business Analytics</b> para validar tu talento ante universidades americanas. 
            Sin intermediarios opacos. Datos reales, oportunidades reales.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- BOTÓN FLOTANTE (FUERA DEL HTML PARA USAR PYTHON) ---
# Usamos columnas para centrar el botón justo debajo del texto visualmente
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if st.button("🚀 INICIAR EVALUACIÓN GRATUITA", use_container_width=True):
        show_contact_form()

# --- LOGOS (DEBAJO DEL BOTÓN) ---
st.markdown("""
<div class="logo-container" style="padding-bottom: 50px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Stanford_Cardinal_logo.svg" class="uni-logo">
    <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/UCLA_Bruins_script_logo.svg" class="uni-logo">
    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d7/North_Carolina_Tar_Heels_logo.svg" class="uni-logo">
    <img src="https://upload.wikimedia.org/wikipedia/commons/de/d3/Wake_Forest_University_Athletic_logo.svg" class="uni-logo">
</div>
""", unsafe_allow_html=True)

# --- SECCIÓN DATOS ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; font-family:Kanit; color:white; font-size:3rem;'>NO ADIVINAMOS. <span style='color:#38bdf8'>MEDIMOS.</span></h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; margin-bottom:40px;'>Tu rendimiento en España traducido al estándar NCAA D1.</p>", unsafe_allow_html=True)

col_d1, col_d2 = st.columns([1, 1.5], gap="large")

with col_d1:
    st.markdown("""
    <div class="stat-box">
        <div style="font-family:'Kanit'; font-size:2.5rem; color:#00ff41; line-height:1;">TOP 8%</div>
        <div style="font-size:0.9rem; color:#94a3b8; letter-spacing:1px;">DUELOS GANADOS VS LIGA</div>
    </div>
    <div class="stat-box">
        <div style="font-family:'Kanit'; font-size:2.5rem; color:white; line-height:1;">0.42</div>
        <div style="font-size:0.9rem; color:#94a3b8; letter-spacing:1px;">GOLES ESPERADOS (xG) / 90'</div>
    </div>
    <div class="stat-box">
        <div style="font-family:'Kanit'; font-size:2.5rem; color:white; line-height:1;">82%</div>
        <div style="font-size:0.9rem; color:#94a3b8; letter-spacing:1px;">PRECISIÓN PASE PROGRESIVO</div>
    </div>
    """, unsafe_allow_html=True)

with col_d2:
    categories = ['Físico', 'Técnica', 'Táctica', 'Mental', 'Stats']
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
          r=[4.5, 4, 5, 4, 4.5], theta=categories, fill='toself', name='TU PERFIL',
          line_color='#38bdf8', fillcolor='rgba(56, 189, 248, 0.5)'
    ))
    fig.add_trace(go.Scatterpolar(
          r=[3, 3, 3, 3, 3], theta=categories, fill='toself', name='MEDIA NCAA',
          line_color='#ffffff', line_dash='dot', opacity=0.3
    ))
    fig.update_layout(
      polar=dict(radialaxis=dict(visible=False), bgcolor='rgba(0,0,0,0)'),
      paper_bgcolor='rgba(0,0,0,0)',
      font_color="white",
      showlegend=False,
      margin=dict(l=20, r=20, t=10, b=10),
      height=400
    )
    st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN EXPERIENCIA REAL (RESTAURADA) ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='font-family:Kanit; color:white; font-size:2.5rem; border-left:5px solid #38bdf8; padding-left:20px;'>LA EXPERIENCIA REAL</h2>", unsafe_allow_html=True)

col_exp1, col_exp2, col_exp3 = st.columns(3, gap="medium")

with col_exp1:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color:#38bdf8">📚 ACADÉMICO</h3>
        <p>Estudia en universidades Top 500 mundial. Yo estudio Business Analytics mientras compito al máximo nivel.</p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color:#38bdf8">⚽ DEPORTIVO</h3>
        <p>Instalaciones de nivel profesional. Fisioterapeutas, gimnasios exclusivos y estadios llenos.</p>
    </div>
    """, unsafe_allow_html=True)

with col_exp3:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color:#38bdf8">🌍 VISADO F-1</h3>
        <p>Gestionamos la burocracia integral. Desde el examen TOEFL hasta la entrevista en la embajada.</p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><hr style='border-color:#1e293b'>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; color:#64748b; padding: 20px;">
    <p style="font-size:1.1rem; color:white;">Dirigida por <b>Jaime Casado</b>. Atleta NCAA D1 & Business Analytics Student.</p>
</div>
""", unsafe_allow_html=True)
