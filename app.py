import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests 

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="US Soccer Talent & Strategy",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 🔴 PEGA AQUÍ TU URL DE N8N (PRODUCTION URL) 🔴 ---
N8N_WEBHOOK_URL = "https://automatizaciones-n8n.wp4rv5.easypanel.host/webhook/contacto" 

def enviar_datos_a_n8n(datos):
    """Envía los datos al webhook de n8n"""
    try:
        response = requests.post(N8N_WEBHOOK_URL, json=datos)
        return response.status_code == 200
    except:
        return False

# 2. LÓGICA POPUP
@st.dialog("🚀 ANÁLISIS PRELIMINAR")
def show_contact_form():
    st.write("Rellena tus datos. Procesaremos tu perfil en tiempo real.")
    
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
        
        submitted = st.form_submit_button("ENVIAR PERFIL", use_container_width=True)
        
        if submitted:
            if not name or not email or not link:
                st.error("⚠️ Por favor, rellena los campos obligatorios.")
            else:
                # Preparamos el paquete de datos para n8n
                payload = {
                    "nombre": name,
                    "equipo": team,
                    "posicion": position,
                    "email": email,
                    "telefono": phone,
                    "video": link
                }
                
                # Enviamos
                exito = enviar_datos_a_n8n(payload)
                
                if exito:
                    st.success("✅ Perfil recibido correctamente. Te contactaremos en 24h.")
                    st.balloons()
                else:
                    st.error("⚠️ Error de conexión. Por favor contáctanos por Instagram.")

# 3. CSS "PURE DARK" (TU DISEÑO FINAL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,400;0,800;1,900&family=Inter:wght@300;400;600&display=swap');

    .block-container { 
        padding-top: 2rem !important; 
        padding-bottom: 5rem !important; 
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        max-width: 100% !important; 
    }
    
    @media (max-width: 768px) {
        .block-container { padding-left: 1rem !important; padding-right: 1rem !important; }
    }

    header { visibility: hidden; }
    footer { visibility: hidden; }

    .stApp { 
        background-color: #020617; 
        background-image: radial-gradient(circle at 50% 0%, #1e293b 0%, #020617 80%);
        color: #f8fafc; 
        font-family: 'Inter', sans-serif; 
    }

    .agency-name {
        color: #38bdf8;
        font-family: 'Kanit', sans-serif;
        font-weight: 800;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 10px;
        font-size: 1.1rem;
        text-align: center;
    }

    h1 {
        font-family: 'Kanit', sans-serif;
        font-weight: 900 !important;
        font-style: italic;
        text-transform: uppercase;
        font-size: 4.5rem !important;
        line-height: 1 !important;
        background: linear-gradient(180deg, #ffffff 0%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px !important;
        text-align: center;
        letter-spacing: -1px;
    }
    
    h2 {
        font-family: 'Kanit', sans-serif;
        color: white !important;
        text-transform: uppercase;
        font-size: 3rem !important;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #94a3b8;
        max-width: 800px; 
        margin: 0 auto 40px auto;
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
    }

    .stButton button {
        background: #38bdf8;
        color: #0f172a;
        border: none;
        padding: 18px 50px;
        font-family: 'Kanit', sans-serif;
        font-size: 1.2rem;
        font-weight: 800;
        text-transform: uppercase;
        border-radius: 4px; 
        transition: all 0.3s;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
        display: block;
        margin: 0 auto;
    }
    .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 40px rgba(56, 189, 248, 0.6);
        background: white;
    }

    .stat-card, .info-card {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid #1e293b;
        border-left: 4px solid #38bdf8;
        padding: 30px;
        margin-bottom: 20px;
        border-radius: 8px;
    }
    
    .stExpander { border: none !important; background: transparent !important; }
    .stExpander > details > summary {
        font-family: 'Kanit', sans-serif !important;
        font-size: 1.1rem !important;
        color: white !important;
        background-color: rgba(30, 41, 59, 0.5) !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        padding: 20px !important;
    }
    .stExpander > details > div {
        background-color: rgba(15, 23, 42, 0.5) !important;
        color: #cbd5e1 !important;
        padding: 20px !important;
        border-radius: 0 0 8px 8px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. HERO SECTION ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p class="agency-name">US SOCCER TALENT & STRATEGY</p>', unsafe_allow_html=True)
st.markdown("<h1>TU TALENTO EN ESPAÑA.<br><span style='color:#38bdf8; -webkit-text-fill-color: #38bdf8;'>TU FUTURO EN USA.</span></h1>", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
    La primera agencia impulsada por <b>Business Analytics</b>. <br>
    Sin opiniones subjetivas. Solo datos que convencen a las universidades.
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if st.button("🚀 INICIAR EVALUACIÓN GRATUITA", use_container_width=True):
        show_contact_form()

# --- 2. SECCIÓN DATOS ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; margin-bottom:10px;'>NO ADIVINAMOS. <span style='color:#38bdf8'>MEDIMOS.</span></h2>", unsafe_allow_html=True)
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
      margin=dict(l=40, r=40, t=20, b=20),
      height=450
    )
    st.plotly_chart(fig, use_container_width=True)

# --- 3. SECCIÓN EXPERIENCIA ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; margin-bottom:40px;'>LA EXPERIENCIA 360°</h2>", unsafe_allow_html=True)
col_e1, col_e2, col_e3 = st.columns(3, gap="medium")

def info_card(emoji, title, text):
    st.markdown(f"""
    <div class="info-card" style="height:300px;">
        <div style="font-size:2.2rem; margin-bottom:15px;">{emoji}</div>
        <h3 style="color:#38bdf8; font-family:'Kanit'; font-size:1.4rem;">{title}</h3>
        <p style="color:#cbd5e1; font-size:1rem; line-height:1.6;">{text}</p>
    </div>
    """, unsafe_allow_html=True)

with col_e1:
    info_card("📚", "ACADÉMICO", "Estudia en universidades Top. Yo compagino Business Analytics con la competición. Tu título valdrá en todo el mundo.")
with col_e2:
    info_card("🏟️", "DEPORTIVO", "Instalaciones que superan a muchos equipos profesionales de Europa. Fisios, gimnasios y estadios llenos.")
with col_e3:
    info_card("🇺🇸", "VISADO F-1", "Gestión integral. Desde el examen TOEFL hasta la entrevista en la embajada. Estamos contigo siempre.")

# --- 4. SECCIÓN: FAQ ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; margin-bottom:10px;'>DUDAS COMUNES</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8; margin-bottom:40px;'>Claridad total antes de empezar.</p>", unsafe_allow_html=True)

c_faq1, c_faq2 = st.columns([1, 2], gap="large")
with c_faq2:
    with st.expander("❓ ¿QUÉ NIVEL NECESITO REALMENTE?"):
        st.write("Las universidades buscan perfiles en **2RFEF, 3RFEF, Preferente o Juvenil División de Honor**. Nuestro algoritmo analiza tus métricas para encontrar tu encaje.")
    
    with st.expander("💸 ¿LA BECA CUBRE EL 100%?"):
        st.write("Es posible, siempre y cuando a la universidad le encajes y hayas demostrado tu potencial.")

    with st.expander("🎓 ¿QUÉ PASA CON EL INGLÉS?"):
        st.write("Necesitas aprobar TOEFL, SAT o Duolingo. No es un proceso complicado. Nosotros te ayudamos a prepararlos y gestionamos la documentación con las universidades.")

    with st.expander("🏥 ¿Y SI ME LESIONO?"):
        st.write("En NCAA tienes acceso a seguros médicos y fisios de élite sin coste. Además, suelen respetar tu beca académica durante la recuperación.")

with c_faq1:
    st.markdown("""
    <div style="padding:20px; text-align:right;">
        <h3 style="color:#38bdf8; font-size:1.8rem;">RESOLVEMOS TU FUTURO</h3>
        <p style="color:#94a3b8; font-size:1.1rem;">
            Ir a USA es una inversión de vida. No dejes cabos sueltos.
            <br><br>
            Yo pasé por las mismas dudas que tú hace 2 años.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><br><hr style='border-color:#1e293b'>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding: 30px;">
    <p style="font-size:1.2rem; color:white; font-family:'Kanit';">US SOCCER TALENT & STRATEGY © 2026</p>
    <p style="color:#64748b;">Dirigida por <b>Jaime Casado</b> | University of Rhode Island</p>
</div>
""", unsafe_allow_html=True)
