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

# 2. CSS "PRO LEAGUE" (ESTILO FINAL)
st.markdown("""
    <style>
    /* Importamos fuente deportiva moderna 'Kanit' y 'Inter' para lectura */
    @import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,300;0,600;0,900;1,900&family=Inter:wght@300;400;600&display=swap');

    /* CORRECCIÓN TÉCNICA: ELIMINAR ESPACIO SUPERIOR QUE CORTA EL TÍTULO */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 5rem !important;
        max-width: 1200px;
    }

    /* FONDO GENERAL */
    .stApp {
        background-color: #020617; /* Fondo base muy oscuro */
        background-image: 
            radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(37, 99, 235, 0.15) 0px, transparent 50%);
        color: #f8fafc;
    }

    /* TIPOGRAFÍA */
    h1 {
        font-family: 'Kanit', sans-serif;
        font-weight: 900 !important;
        font-style: italic;
        text-transform: uppercase;
        font-size: 4.5rem !important;
        line-height: 0.9 !important;
        color: #ffffff;
        margin-bottom: 20px !important;
    }
    
    h2 {
        font-family: 'Kanit', sans-serif;
        font-weight: 600 !important;
        text-transform: uppercase;
        color: #38bdf8 !important; /* Cian Eléctrico */
        font-size: 2rem !important;
        margin-top: 40px;
        margin-bottom: 10px;
        border: none !important; /* Quitamos la línea que no te gustaba */
    }

    p, li, div {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: #cbd5e1;
        line-height: 1.6;
    }

    /* BOTONES PRIMARIOS */
    .stButton>button {
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
        color: white;
        border: none;
        padding: 18px 45px;
        font-family: 'Kanit', sans-serif;
        font-weight: 600;
        font-size: 1.2rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 4px; /* Bordes más rectos, más técnico */
        width: 100%;
        transition: all 0.3s;
        box-shadow: 0 10px 20px rgba(14, 165, 233, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px rgba(14, 165, 233, 0.5);
    }

    /* TARJETAS ESTILO CRISTAL (GLASSMORPHISM) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }
    
    /* INPUTS FORMULARIO */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: rgba(0, 0, 0, 0.3);
        border: 1px solid #334155;
        color: white;
        border-radius: 4px;
        height: 50px;
    }
    .stTextInput>div>div>input:focus {
        border-color: #38bdf8;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.2);
    }

    /* FOTOS */
    img {
        border-radius: 8px;
        filter: brightness(0.9) contrast(1.1); /* Efecto cinemático */
    }
    </style>
    """, unsafe_allow_html=True)

# --- SECCIÓN HERO (MEJORADA) ---
col_hero_text, col_hero_img = st.columns([1.2, 1], gap="large")

with col_hero_text:
    st.markdown('<p style="color:#38bdf8; font-weight:700; letter-spacing:3px; margin-bottom:10px; font-family:Kanit;">US SOCCER TALENT & STRATEGY</p>', unsafe_allow_html=True)
    st.markdown("<h1>TU TALENTO EN ESPAÑA.<br><span style='color:#38bdf8; opacity:0.8;'>TU FUTURO EN USA.</span></h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="margin-bottom: 30px; font-size: 1.2rem; color: #94a3b8;">
    Olvídate de los vídeos de highlights que nadie ve. Somos la primera agencia técnica que utiliza 
    <b>Business Analytics</b> para validar tu talento ante las universidades americanas.
    <br><br>
    Dirigida por <b>Jaime Casado</b>, jugador activo NCAA D1 & Analista.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 INICIAR EVALUACIÓN GRATUITA"):
        st.toast("¡Vamos a ello! Baja al formulario final.")

with col_hero_img:
    # Imagen de alta calidad, genérica de estadio profesional
    st.image("https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=2093&auto=format&fit=crop", use_container_width=True)

st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

# --- SECCIÓN: POR QUÉ FUNCIONA (EL PROBLEMA Y LA SOLUCIÓN) ---
# Usamos columnas de ancho completo para dar sensación de web profesional
st.markdown("""
<div class="glass-card" style="text-align:center; padding: 50px;">
    <h2 style="margin-top:0;">EL PROBLEMA DE LAS AGENCIAS TRADICIONALES</h2>
    <p style="max-width: 800px; margin: 0 auto;">Te prometen becas basándose en "sensaciones". Nosotros no. 
    En Estados Unidos, los entrenadores gestionan presupuestos millonarios y necesitan <b>certeza estadística</b>.</p>
</div>
""", unsafe_allow_html=True)

# --- SECCIÓN DATOS ---
c_data1, c_data2 = st.columns([1, 1], gap="large")

with c_data1:
    st.markdown("<h2>TU PASAPORTE ESTADÍSTICO</h2>", unsafe_allow_html=True)
    st.markdown("""
    Nuestro algoritmo compara tu rendimiento en España (División de Honor, Liga Nacional, etc.) con la media histórica de la NCAA.
    
    * **Identificación de Talento:** ¿Estás en el top 10% en duelos ganados?
    * **Traducción de Nivel:** Un gol en España equivale a X en USA.
    * **Reporte Profesional:** Lo que reciben los entrenadores.
    """)
    
    # Tabla simulada de datos (Añade densidad de información)
    df_demo = pd.DataFrame({
        "Métrica Clave": ["Goles esperados (xG)", "Duelos Defensivos", "Pases Progresivos", "Recuperaciones"],
        "Tu Rendimiento": ["0.45 / 90'", "68%", "8.2 / 90'", "12 / partido"],
        "Media NCAA D1": ["0.31 / 90'", "60%", "6.5 / 90'", "9 / partido"],
        "Estado": ["✅ SUPERIOR", "✅ SUPERIOR", "✅ SUPERIOR", "✅ SUPERIOR"]
    })
    st.dataframe(df_demo, use_container_width=True, hide_index=True)

with c_data2:
    # Gráfico Radar
    categories = ['Puntaje Ofensivo', 'Inteligencia Táctica', 'Físico', 'Técnica', 'Defensa']
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
          r=[4, 5, 4, 5, 3], theta=categories, fill='toself', name='TU PERFIL',
          line_color='#38bdf8', fillcolor='rgba(56, 189, 248, 0.4)'
    ))
    fig.add_trace(go.Scatterpolar(
          r=[3, 3, 3, 3, 3], theta=categories, fill='toself', name='PROMEDIO LIGA',
          line_color='#64748b', line_dash='dot', opacity=0.5
    ))
    fig.update_layout(
      polar=dict(radialaxis=dict(visible=False), bgcolor='rgba(0,0,0,0)'),
      paper_bgcolor='rgba(0,0,0,0)',
      font_color="white",
      showlegend=False,
      margin=dict(l=20, r=20, t=20, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN: REALIDAD (SIN TITULO DE URI FALSO) ---
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
st.markdown("<h2>LA EXPERIENCIA REAL</h2>", unsafe_allow_html=True)

col_exp1, col_exp2, col_exp3 = st.columns(3)

with col_exp1:
    st.markdown('<div class="glass-card" style="height:250px"><h3>📚 ACADÉMICO</h3><p>Estudia en universidades Top 500 mundial. Yo estudio Business Analytics mientras computo.</p></div>', unsafe_allow_html=True)
with col_exp2:
    st.markdown('<div class="glass-card" style="height:250px"><h3>⚽ DEPORTIVO</h3><p>Instalaciones de nivel profesional. Fisioterapeutas, gimnasios exclusivos y estadios llenos.</p></div>', unsafe_allow_html=True)
with col_exp3:
    st.markdown('<div class="glass-card" style="height:250px"><h3>🌍 VISADO F-1</h3><p>Gestionamos la burocracia. Desde el examen TOEFL hasta la entrevista en la embajada.</p></div>', unsafe_allow_html=True)

# --- SECCIÓN FORMULARIO (FINAL) ---
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
st.markdown("""
<div style="border-left: 4px solid #38bdf8; padding-left: 20px;">
    <h2>SOLICITUD DE ANÁLISIS</h2>
    <p>Rellena los datos técnicos. Si encajas en el perfil que buscan las universidades este año, te contactaré personalmente.</p>
</div>
""", unsafe_allow_html=True)

with st.form("main_form"):
    c_form1, c_form2 = st.columns(2, gap="medium")
    
    with c_form1:
        st.text_input("NOMBRE COMPLETO", placeholder="Ej. Javier García")
        st.text_input("EQUIPO ACTUAL", placeholder="Ej. Real Madrid Juv. B")
        st.selectbox("POSICIÓN PRINCIPAL", ["Portero", "Defensa Central", "Lateral", "Pivote", "Interior", "Extremo", "Delantero"])
    
    with c_form2:
        st.text_input("EMAIL", placeholder="correo@ejemplo.com")
        st.text_input("WHATSAPP", placeholder="+34 ...")
        st.text_input("ENLACE A PERFIL (Transfermarkt/RFEF/Video)", placeholder="https://...")

    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.form_submit_button("ENVIAR PERFIL A ANÁLISIS")
