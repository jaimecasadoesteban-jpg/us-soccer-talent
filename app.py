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

# 2. LÓGICA DEL POPUP (VENTANA EMERGENTE)
@st.dialog("🚀 TU PRIMER PASO A USA")
def show_contact_form():
    st.write("Rellena los datos clave. Si encajas en el perfil, agendamos llamada.")
    with st.form("popup_form"):
        name = st.text_input("Nombre Completo", placeholder="Ej. Jaime Casado")
        c1, c2 = st.columns(2)
        with c1:
            team = st.text_input("Equipo Actual")
            position = st.selectbox("Posición", ["Portero", "Defensa", "Medio", "Delantero"])
        with c2:
            email = st.text_input("Email")
            phone = st.text_input("WhatsApp")
        
        link = st.text_input("Link Highlights (Video/Transfermarkt)")
        
        if st.form_submit_button("ENVIAR PERFIL", use_container_width=True):
            st.success("✅ Datos enviados correctamente.")

# 3. CSS (ESTÉTICA Y CORRECCIONES)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,400;0,800;1,900&family=Inter:wght@300;400;600&display=swap');

    /* CORRECCIÓN DE MÁRGENES (CRÍTICO) */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100%;
    }
    header {visibility: hidden;}

    /* FONDO GLOBAL */
    .stApp { background-color: #020617; color: #f8fafc; font-family: 'Inter', sans-serif; }

    /* ESTILO HERO (PORTADA) */
    .hero-container {
        position: relative;
        width: 100%;
        height: 85vh; /* Altura fija */
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #000; /* Fondo negro si falla video */
    }
    
    .hero-video {
        position: absolute;
        top: 50%;
        left: 50%;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        z-index: 1;
        transform: translate(-50%, -50%);
        opacity: 0.5; /* Oscuridad del video */
        object-fit: cover;
    }
    
    .hero-text {
        position: relative;
        z-index: 2; /* Encima del video */
        text-align: center;
        padding: 20px;
        max-width: 900px;
    }

    /* TIPOGRAFÍA */
    h1 {
        font-family: 'Kanit', sans-serif;
        font-weight: 900 !important;
        font-style: italic;
        text-transform: uppercase;
        font-size: 5rem !important;
        line-height: 0.9 !important;
        color: white;
        text-shadow: 0 0 20px rgba(0,0,0,0.8);
        margin-bottom: 10px !important;
    }
    
    h2 {
        font-family: 'Kanit', sans-serif;
        color: white !important;
        text-transform: uppercase;
    }

    /* BOTÓN */
    .stButton button {
        background: linear-gradient(90deg, #38bdf8, #2563eb);
        color: white;
        border: none;
        padding: 15px 50px;
        font-family: 'Kanit', sans-serif;
        font-size: 1.3rem;
        font-weight: 800;
        text-transform: uppercase;
        border-radius: 4px;
        margin-top: 20px;
        transition: transform 0.2s;
    }
    .stButton button:hover {
        transform: scale(1.05);
        color: white;
    }

    /* TARJETAS IGUALES (CORRECCIÓN TAMAÑO) */
    .info-card {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 12px;
        height: 320px; /* ALTURA FIJA PARA TODAS */
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    .info-card h3 {
        color: #38bdf8;
        font-family: 'Kanit';
        font-size: 1.5rem;
        margin-bottom: 15px;
    }

    /* LOGOS */
    .logo-row {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-top: 40px;
        margin-bottom: 40px;
        flex-wrap: wrap;
    }
    .logo-img {
        height: 45px;
        filter: grayscale(100%) brightness(200%);
        opacity: 0.7;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. HERO SECTION (PORTADA) ---
# Inyectamos HTML con cuidado extremo
st.markdown("""
<div class="hero-container">
    <video autoplay muted loop playsinline class="hero-video">
        <source src="https://videos.pexels.com/video-files/3195239/3195239-uhd_2560_1440_25fps.mp4" type="video/mp4">
    </video>
    <div class="hero-text">
        <p style="color:#38bdf8; font-weight:800; letter-spacing:3px; margin-bottom:10px; font-family:Kanit;">US SOCCER TALENT & STRATEGY</p>
        <h1>TU TALENTO EN ESPAÑA.<br><span style='color:#38bdf8'>TU FUTURO EN USA.</span></h1>
        <p style="font-size: 1.2rem; color: #e2e8f0; text-shadow: 0 2px 4px black; margin-top: 20px;">
            Usamos <b>Business Analytics</b> para validar tu talento ante universidades americanas. 
            Sin intermediarios opacos. Datos reales, oportunidades reales.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# BOTÓN DE ACCIÓN (Fuera del HTML para que funcione el Python)
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if st.button("🚀 INICIAR EVALUACIÓN GRATUITA", use_container_width=True):
        show_contact_form()

# --- LOGOS ---
st.markdown("""
<div class="logo-row">
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Stanford_Cardinal_logo.svg" class="logo-img">
    <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/UCLA_Bruins_script_logo.svg" class="logo-img">
    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d7/North_Carolina_Tar_Heels_logo.svg" class="logo-img">
    <img src="https://upload.wikimedia.org/wikipedia/commons/de/d3/Wake_Forest_University_Athletic_logo.svg" class="logo-img">
</div>
""", unsafe_allow_html=True)

# --- SECCIÓN DATOS ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; font-size:3rem; margin-bottom:10px;'>NO ADIVINAMOS. <span style='color:#38bdf8'>MEDIMOS.</span></h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8; margin-bottom:40px;'>Tu rendimiento en España traducido al estándar NCAA D1.</p>", unsafe_allow_html=True)

col_data1, col_data2 = st.columns([1, 1.5], gap="large")

with col_data1:
    # Tarjetas de datos estilizadas
    st.markdown("""
    <div style="background:rgba(15,23,42,0.5); border-left:4px solid #38bdf8; padding:20px; margin-bottom:15px;">
        <div style="font-family:'Kanit'; font-size:2rem; color:#00ff41; line-height:1;">TOP 8%</div>
        <div style="font-size:0.8rem; letter-spacing:1px; color:#cbd5e1;">DUELOS GANADOS VS LIGA</div>
    </div>
    <div style="background:rgba(15,23,42,0.5); border-left:4px solid #38bdf8; padding:20px; margin-bottom:15px;">
        <div style="font-family:'Kanit'; font-size:2rem; color:white; line-height:1;">0.42</div>
        <div style="font-size:0.8rem; letter-spacing:1px; color:#cbd5e1;">GOLES ESPERADOS (xG) / 90'</div>
    </div>
    <div style="background:rgba(15,23,42,0.5); border-left:4px solid #38bdf8; padding:20px; margin-bottom:15px;">
        <div style="font-family:'Kanit'; font-size:2rem; color:white; line-height:1;">82%</div>
        <div style="font-size:0.8rem; letter-spacing:1px; color:#cbd5e1;">PRECISIÓN PASE PROGRESIVO</div>
    </div>
    """, unsafe_allow_html=True)

with col_data2:
    # Gráfico Radar
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
      margin=dict(l=20, r=20, t=20, b=20),
      height=380
    )
    st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN EXPERIENCIA (TARJETAS IGUALES) ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='font-size:2.5rem; border-left:5px solid #38bdf8; padding-left:20px;'>LA EXPERIENCIA REAL</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col_exp1, col_exp2, col_exp3 = st.columns(3, gap="medium")

with col_exp1:
    st.markdown("""
    <div class="info-card">
        <h3>📚 ACADÉMICO</h3>
        <p>Acceso a universidades Top 500 mundial. Combinarás clases de alto nivel con entrenamientos diarios. Yo estudio Business Analytics en URI mientras compito.</p>
    </div>
    """, unsafe_allow_html=True)

with col_exp2:
    st.markdown("""
    <div class="info-card">
        <h3>⚽ DEPORTIVO</h3>
        <p>Instalaciones profesionales: estadios de hierba natural, gimnasios exclusivos para atletas, fisioterapeutas y material deportivo gratuito (Nike/Adidas).</p>
    </div>
    """, unsafe_allow_html=True)

with col_exp3:
    st.markdown("""
    <div class="info-card">
        <h3>🌍 VISADO F-1</h3>
        <p>Gestionamos todo el proceso burocrático. Preparación para exámenes SAT/TOEFL, traducción de notas y asesoramiento para la entrevista en la embajada.</p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><hr style='border-color:#1e293b'>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; color:#64748b; padding: 20px;">
    <p style="font-size:1rem; color:white;">US SOCCER TALENT & STRATEGY © 2024</p>
    <p>Dirigida por <b>Jaime Casado</b>. Atleta NCAA D1 & Business Analytics Student.</p>
</div>
""", unsafe_allow_html=True)
