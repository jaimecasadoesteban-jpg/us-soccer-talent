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

# 2. LÓGICA POPUP
@st.dialog("🚀 ANÁLISIS PRELIMINAR")
def show_contact_form():
    st.write("Rellena tus datos. Buscamos perfiles específicos para 2025/26.")
    with st.form("popup_form"):
        name = st.text_input("Nombre Completo")
        c1, c2 = st.columns(2)
        with c1:
            team = st.text_input("Equipo y Categoría")
            position = st.selectbox("Posición", ["Portero", "Defensa", "Medio", "Delantero"])
        with c2:
            email = st.text_input("Email")
            phone = st.text_input("WhatsApp")
        
        link = st.text_input("Link Highlights (Obligatorio)")
        
        if st.form_submit_button("ENVIAR PERFIL", use_container_width=True):
            st.success("✅ Perfil enviado al equipo de análisis.")

# 3. CSS "DARK ELITE" (LIMPIO Y SEGURO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,400;0,800;1,900&family=Inter:wght@300;400;600&display=swap');

    /* RESETEO */
    .block-container { padding-top: 2rem !important; max-width: 1200px !important; }
    header { visibility: hidden; }
    footer { visibility: hidden; }

    /* FONDO GENERAL */
    .stApp { background-color: #020617; color: #f8fafc; font-family: 'Inter', sans-serif; }

    /* TIPOGRAFÍA */
    h1 {
        font-family: 'Kanit', sans-serif;
        font-weight: 900 !important;
        font-style: italic;
        text-transform: uppercase;
        font-size: 4.5rem !important; /* Tamaño gigante */
        line-height: 1 !important;
        color: white;
        margin-bottom: 10px !important;
        text-align: center;
    }
    
    h2 {
        font-family: 'Kanit', sans-serif;
        color: white !important;
        text-transform: uppercase;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.4rem;
        color: #94a3b8;
        max-width: 800px;
        margin: 0 auto 30px auto;
        font-family: 'Inter', sans-serif;
    }

    /* BOTONES */
    .stButton button {
        background: linear-gradient(90deg, #38bdf8, #2563eb);
        color: white;
        border: none;
        padding: 18px 50px;
        font-family: 'Kanit', sans-serif;
        font-size: 1.2rem;
        font-weight: 800;
        text-transform: uppercase;
        border-radius: 4px; 
        transition: all 0.3s;
        box-shadow: 0 0 20px rgba(37, 99, 235, 0.5);
        display: block;
        margin: 0 auto; /* Centrado */
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 40px rgba(37, 99, 235, 0.8);
    }

    /* TARJETAS DATOS */
    .stat-card {
        background: rgba(15, 23, 42, 1);
        border: 1px solid #1e293b;
        border-left: 4px solid #38bdf8;
        padding: 25px;
        margin-bottom: 15px;
        border-radius: 8px;
    }

    /* ACORDEÓN FAQ */
    .stExpander {
        border: none !important;
        background-color: transparent !important;
        margin-bottom: 10px;
    }
    .stExpander > details > summary {
        font-family: 'Kanit', sans-serif !important;
        font-size: 1.2rem !important;
        color: white !important;
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        padding: 20px !important;
    }
    .stExpander > details > div {
        background-color: #0f172a !important;
        color: #cbd5e1 !important;
        padding: 20px !important;
        border-radius: 0 0 8px 8px;
    }
    
    /* IMAGEN HERO REDONDEADA */
    img {
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. HERO SECTION (ESTILO APPLE: TEXTO -> IMAGEN) ---

# Títulos (Centrados y Limpios)
st.markdown("<h1>TU TALENTO EN ESPAÑA.<br><span style='color:#38bdf8'>TU FUTURO EN USA.</span></h1>", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
    La primera agencia impulsada por <b>Business Analytics</b>. <br>
    Sin opiniones subjetivas. Solo datos que convencen a las universidades.
</div>
""", unsafe_allow_html=True)

# Imagen Cinemática (Nativa de Streamlit - NO FALLA)
# Usamos una imagen de estadio nocturno muy profesional
st.image("https://images.unsplash.com/photo-1522778119026-d647f0596c63?q=80&w=2070&auto=format&fit=crop", use_container_width=True)

# Botón de Acción (Centrado debajo de la imagen)
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if st.button("🚀 INICIAR EVALUACIÓN GRATUITA", use_container_width=True):
        show_contact_form()

# --- 2. SECCIÓN DATOS ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; font-size:3.5rem; margin-bottom:10px;'>NO ADIVINAMOS. <span style='color:#38bdf8'>MEDIMOS.</span></h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8; margin-bottom:50px; font-size:1.2rem;'>Tu rendimiento en España traducido al estándar NCAA D1.</p>", unsafe_allow_html=True)

col_d1, col_d2 = st.columns([1, 1.5], gap="large")
with col_d1:
    st.markdown("""
    <div class="stat-card">
        <div style="font-family:'Kanit'; font-size:2.5rem; color:#00ff41; line-height:1;">TOP 8%</div>
        <div style="font-size:0.9rem; letter-spacing:1px; color:#cbd5e1; margin-top:5px;">DUELOS GANADOS VS LIGA</div>
    </div>
    <div class="stat-card">
        <div style="font-family:'Kanit'; font-size:2.5rem; color:white; line-height:1;">0.42</div>
        <div style="font-size:0.9rem; letter-spacing:1px; color:#cbd5e1; margin-top:5px;">GOLES ESPERADOS (xG) / 90'</div>
    </div>
    <div class="stat-card">
        <div style="font-family:'Kanit'; font-size:2.5rem; color:white; line-height:1;">82%</div>
        <div style="font-size:0.9rem; letter-spacing:1px; color:#cbd5e1; margin-top:5px;">PRECISIÓN PASE PROGRESIVO</div>
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
      margin=dict(l=20, r=20, t=20, b=20),
      height=450
    )
    st.plotly_chart(fig, use_container_width=True)

# --- 3. SECCIÓN EXPERIENCIA ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; margin-bottom:40px;'>LA EXPERIENCIA 360°</h2>", unsafe_allow_html=True)
col_e1, col_e2, col_e3 = st.columns(3, gap="medium")

def info_card(emoji, title, text):
    st.markdown(f"""
    <div style="background:rgba(30,41,59,0.4); padding:30px; border-radius:12px; height:280px; border:1px solid #1e293b;">
        <div style="font-size:2rem; margin-bottom:10px;">{emoji}</div>
        <h3 style="color:#38bdf8; font-family:'Kanit'; font-size:1.4rem;">{title}</h3>
        <p style="color:#cbd5e1; font-size:1rem; line-height:1.6;">{text}</p>
    </div>
    """, unsafe_allow_html=True)

with col_e1:
    info_card("📚", "ACADÉMICO", "Estudia en universidades Top. Yo compagino Business Analytics con la competición. Tu título valdrá en todo el mundo.")
with col_e2:
    info_card("🏟️", "DEPORTIVO", "Instalaciones que superan a muchos equipos profesionales de Europa. Fisios, gimnasios y estadios llenos.")
with col_e3:
    info_card("🇺🇸", "VISADO F-1", "Gestión integral. Desde el examen TOEFL hasta la entrevista en la embajada. Sin errores burocráticos.")

# --- 4. SECCIÓN: PREGUNTAS FRECUENTES (FAQ) ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; margin-bottom:10px;'>DUDAS COMUNES</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8; margin-bottom:40px;'>Claridad total antes de empezar.</p>", unsafe_allow_html=True)

c_faq1, c_faq2 = st.columns([1, 2])
with c_faq2:
    with st.expander("❓ ¿QUÉ NIVEL NECESITO REALMENTE PARA CONSEGUIR BECA?"):
        st.write("""
        No necesitas ser profesional, pero sí destacar en tu liga. Las universidades buscan perfiles titulares en **División de Honor, Liga Nacional o Preferente Senior**.
        Nuestro algoritmo analiza tus minutos jugados y métricas clave. Si estás en un equipo de menor categoría pero tienes estadísticas "fuera de serie" (ej. +20 goles), también hay opciones.
        """)
    
    with st.expander("💸 ¿LA BECA CUBRE EL 100% DE LOS GASTOS?"):
        st.write("""
        Es posible (Full Ride), pero reservado para el top 1% de los talentos.
        **La realidad:** La mayoría de jugadores obtienen un **paquete mixto**. Sumamos tu Beca Deportiva + Beca Académica (por tus notas de Bachillerato) + Ayuda Internacional. 
        Nuestro trabajo es maximizar esa suma para que tu coste final sea mínimo.
        """)

    with st.expander("🎓 ¿QUÉ PASA SI MI INGLÉS NO ES PERFECTO?"):
        st.write("""
        No te preocupes. Necesitas aprobar el examen **TOEFL** y el **SAT**, pero las universidades tienen baremos flexibles para atletas.
        Nosotros te indicamos la puntuación exacta que necesitas según la división (NCAA D1, D2 o NAIA) y te ayudamos a preparar el papeleo.
        """)

    with st.expander("🏥 ¿QUÉ SUCEDE SI ME LESIONO ALLÍ?"):
        st.write("""
        En la NCAA, los atletas tienen acceso a los mejores seguros médicos y fisioterapia de élite diaria **sin coste extra**.
        Además, si la lesión es grave, la mayoría de universidades respetan tu beca académica para que puedas terminar la carrera aunque no puedas jugar esa temporada.
        """)

with c_faq1:
    st.markdown("""
    <div style="padding:20px; text-align:right;">
        <h3 style="color:#38bdf8; font-size:1.5rem;">RESOLVEMOS TU FUTURO</h3>
        <p style="color:#94a3b8;">
            Ir a USA es una inversión de vida. No dejes cabos sueltos.
            <br><br>
            Yo pasé por las mismas dudas que tú hace 2 años.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><hr style='border-color:#1e293b'>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding: 30px;">
    <p style="font-size:1.2rem; color:white; font-family:'Kanit';">US SOCCER TALENT & STRATEGY © 2026</p>
    <p style="color:#64748b;">Dirigida por <b>Jaime Casado</b> | University of Rhode Island</p>
</div>
""", unsafe_allow_html=True)
