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

# Inicializar estado del formulario si no existe
if 'show_form' not in st.session_state:
    st.session_state.show_form = False

def open_form():
    st.session_state.show_form = True

# 2. CSS AVANZADO (ESTILO CINE & FUTBOL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,300;0,600;0,800;1,900&family=Inter:wght@300;400;600&display=swap');

    /* CORRECCIONES DE LAYOUT */
    .block-container { padding-top: 0rem !important; padding-bottom: 5rem !important; max-width: 100%; }
    header { visibility: hidden; } /* Ocultar barra superior de Streamlit */
    
    /* FONDO OSCURO GLOBAL */
    .stApp { background-color: #020617; color: #f8fafc; font-family: 'Inter', sans-serif; }

    /* ESTILO DEL VIDEO HERO */
    .hero-container {
        position: relative;
        width: 100%;
        height: 85vh; /* Ocupa casi toda la pantalla */
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    
    .hero-video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: 0;
        opacity: 0.4; /* Oscurecer vídeo */
        filter: grayscale(30%) contrast(1.2);
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
        max-width: 900px;
        padding: 20px;
        background: radial-gradient(circle, rgba(2,6,23,0.8) 0%, rgba(2,6,23,0) 70%);
    }

    /* TIPOGRAFÍA HERO */
    h1 {
        font-family: 'Kanit', sans-serif;
        font-weight: 900 !important;
        font-style: italic;
        text-transform: uppercase;
        font-size: 5rem !important;
        line-height: 0.9 !important;
        text-shadow: 0 0 40px rgba(56, 189, 248, 0.3);
        margin-bottom: 20px !important;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        color: #cbd5e1;
        margin-bottom: 40px;
        font-weight: 300;
        text-shadow: 0 2px 4px rgba(0,0,0,0.8);
    }

    /* LOGOS BAR */
    .logo-bar {
        display: flex;
        justify-content: center;
        gap: 50px;
        padding: 30px 0;
        background: #0f172a;
        border-bottom: 1px solid #1e293b;
        margin-bottom: 50px;
        flex-wrap: wrap;
    }
    .uni-logo { height: 40px; opacity: 0.6; filter: grayscale(100%); transition: all 0.3s; }
    .uni-logo:hover { opacity: 1; filter: grayscale(0%); transform: scale(1.1); }

    /* BOTÓN CTA PRINCIPAL */
    .stButton button {
        background: linear-gradient(90deg, #0ea5e9, #2563eb);
        color: white;
        border: none;
        padding: 20px 60px;
        font-family: 'Kanit', sans-serif;
        font-size: 1.5rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 0px; /* Estilo Nike */
        clip-path: polygon(10% 0, 100% 0, 100% 100%, 0% 100%);
        transition: all 0.3s;
        box-shadow: 0 0 20px rgba(14, 165, 233, 0.4);
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 40px rgba(14, 165, 233, 0.8);
    }

    /* TARJETAS DE DATOS (NUEVAS) */
    .stat-box {
        background: rgba(30, 41, 59, 0.4);
        border-left: 4px solid #38bdf8;
        padding: 20px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 10px;
    }
    .stat-value { font-family: 'Kanit'; font-size: 2rem; color: white; line-height: 1; }
    .stat-label { font-size: 0.9rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; }

    /* FORMULARIO FLOTANTE */
    .form-container {
        background: #1e293b;
        padding: 40px;
        border-radius: 12px;
        border: 2px solid #38bdf8;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        margin-top: 20px;
        animation: fadeIn 0.5s ease-in-out;
    }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
    </style>
""", unsafe_allow_html=True)

# --- 1. HERO SECTION CON VIDEO ---
# Usamos HTML puro para el video de fondo y el contenido superpuesto
st.markdown("""
<div class="hero-container">
    <video autoplay muted loop playsinline class="hero-video">
        <source src="https://videos.pexels.com/video-files/5436660/5436660-uhd_2560_1440_24fps.mp4" type="video/mp4">
    </video>
    <div class="hero-content">
        <p style="color:#38bdf8; font-weight:800; letter-spacing:4px; margin-bottom:10px;">US SOCCER TALENT & STRATEGY</p>
        <h1>TU TALENTO ES EL DATO.<br>USA ES EL DESTINO.</h1>
        <p class="hero-subtitle">
            Usamos Business Analytics para validar tu rendimiento. No vendemos humo, vendemos 
            evidencia estadística a las universidades que buscan ganadores.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. BARRA DE LOGOS (UNIVERSIDADES) ---
st.markdown("""
<div class="logo-bar">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Stanford_Cardinal_logo.svg/1200px-Stanford_Cardinal_logo.svg.png" class="uni-logo" title="Stanford">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/UCLA_Bruins_script_logo.svg/2560px-UCLA_Bruins_script_logo.svg.png" class="uni-logo" title="UCLA">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/North_Carolina_Tar_Heels_logo.svg/1200px-North_Carolina_Tar_Heels_logo.svg.png" class="uni-logo" title="UNC">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Wake_Forest_University_Athletic_logo.svg/1200px-Wake_Forest_University_Athletic_logo.svg.png" class="uni-logo" title="Wake Forest">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/NCAA_logo.svg/1024px-NCAA_logo.svg.png" class="uni-logo" title="NCAA">
</div>
""", unsafe_allow_html=True)

# --- 3. BOTÓN DE ACCIÓN (Lógica de Python) ---
# Creamos tres columnas para centrar el botón gigante
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    if st.button("🚀 DESBLOQUEAR MI FUTURO EN USA", type="primary", use_container_width=True):
        open_form()

# --- 4. ZONA DEL FORMULARIO (APARECE SOLO AL CLICAR) ---
if st.session_state.show_form:
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#38bdf8;'>FICHA TÉCNICA INICIAL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Rellena tus datos. Si el algoritmo detecta potencial, agendamos llamada.</p>", unsafe_allow_html=True)
    
    with st.form("contact_form"):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("NOMBRE COMPLETO")
            st.text_input("EQUIPO ACTUAL Y CATEGORÍA")
            st.selectbox("POSICIÓN", ["Portero", "Defensa", "Medio", "Delantero"])
        with c2:
            st.text_input("EMAIL")
            st.text_input("WHATSAPP")
            st.text_input("LINK TRANSFERMARKT / VIDEO")
        
        st.write("")
        submit = st.form_submit_button("ENVIAR DATOS PARA ANÁLISIS")
        if submit:
            st.success("✅ Datos recibidos. Iniciando análisis de viabilidad...")
    
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- 5. SECCIÓN DATOS (NUEVA: SIN TABLA) ---
st.markdown("<h2 style='text-align:center; font-family:Kanit; font-size:3rem;'>NO ADIVINAMOS. <span style='color:#38bdf8'>MEDIMOS.</span></h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; margin-bottom:40px;'>Tu rendimiento en España traducido al estándar NCAA D1.</p>", unsafe_allow_html=True)

col_d1, col_d2 = st.columns([1, 1.5], gap="large")

with col_d1:
    # Tarjetas de Estadísticas (Estilo Dashboard)
    st.markdown("""
    <div class="stat-box">
        <div class="stat-value" style="color:#00ff41;">TOP 8%</div>
        <div class="stat-label">DUELOS GANADOS VS LIGA</div>
    </div>
    <div class="stat-box">
        <div class="stat-value">0.42</div>
        <div class="stat-label">GOLES ESPERADOS (xG) / 90'</div>
    </div>
    <div class="stat-box">
        <div class="stat-value">82%</div>
        <div class="stat-label">PRECISIÓN PASE PROGRESIVO</div>
    </div>
    <p style="font-size:0.9rem; color:#64748b; margin-top:20px;">
        *Ejemplo de análisis real. Comparamos tus métricas con la base de datos de 200 universidades.
    </p>
    """, unsafe_allow_html=True)

with col_d2:
    # Gráfico Radar Premium
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
      height=350
    )
    st.plotly_chart(fig, use_container_width=True)

# --- 6. FOOTER (FIRMA) ---
st.markdown("<hr style='border-color:#1e293b'>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; color:#64748b; padding: 20px;">
    <p style="font-size:0.9rem;">US SOCCER TALENT & STRATEGY © 2024</p>
    <p style="font-size:1.1rem; color:white;">Dirigida por <b>Jaime Casado</b>. Atleta NCAA D1 & Business Analytics Student.</p>
</div>
""", unsafe_allow_html=True)
