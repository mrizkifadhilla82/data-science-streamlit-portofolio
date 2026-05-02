import streamlit as st
import os

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Muhammad Rizki Fadhilla | Data Scientist",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load CSS ─────────────────────────────────────────────────────────────────
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_path):
    load_css(css_path)

# ── TITLE & DESCRIPTION (Assignment Requirement) ──────────────────────────────
st.title("My Portfolio with Streamlit")
st.markdown("""
Welcome to my personal portfolio! This app showcases my journey as a **Data Scientist** and **Machine Learning Enthusiast**.

Here you will find:
- 👤 **About Me** — my background, skills, and tech stack
- 📂 **Projects** — real-world data science projects with business context, pain points, and solutions
- 🤖 **Prediction** — live ML model demo (House Price Prediction via FastAPI)
- 📊 **Visualization** — interactive data and model performance charts
""")

st.markdown("---")

import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Check for profile photo
profile_pic = None
if os.path.exists("profile.jpg"):
    profile_pic = get_base64_of_bin_file("profile.jpg")
elif os.path.exists("profile.png"):
    profile_pic = get_base64_of_bin_file("profile.png")

if profile_pic:
    avatar_html = f"""
<div style="
    width: 120px;
    height: 120px;
    border-radius: 50%;
    margin: 0 auto 24px auto;
    box-shadow: 0 0 40px rgba(59, 130, 246, 0.3);
    background-image: url('data:image/png;base64,{profile_pic}');
    background-size: cover;
    background-position: center;
    border: 2px solid #3B82F6;
"></div>
"""
else:
    avatar_html = """
<div style="
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: linear-gradient(135deg, #1D4ED8, #14B8A6);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 48px;
    margin: 0 auto 24px auto;
    box-shadow: 0 0 40px rgba(59, 130, 246, 0.3);
">🔬</div>
"""

# ── HERO SECTION ─────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #0D1120 0%, #1a2744 100%);
    border: 1px solid #1E3A5F;
    border-radius: 16px;
    padding: 48px 40px;
    margin-bottom: 32px;
    text-align: center;
">
{avatar_html}
<h1 style="
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #3B82F6, #14B8A6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
">Muhammad Rizki Fadhilla</h1>
<p style="
    font-size: 1.1rem;
    color: #64748B;
    font-weight: 500;
    margin-bottom: 20px;
    letter-spacing: 0.05em;
">Data Scientist | Machine Learning Enthusiast</p>
<p style="
    font-size: 0.95rem;
    color: #94A3B8;
    max-width: 600px;
    margin: 0 auto 28px auto;
    line-height: 1.7;
">
    Passionate about transforming raw data into business impact through machine learning,
    statistical analysis, and scalable data pipelines. Currently building end-to-end ML systems
    with Python, Scikit-learn, FastAPI & Docker.
</p>
<div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
        <a href="https://www.linkedin.com/in/mrizkifadhilla" target="_blank" style="
            background: linear-gradient(135deg, #0077B5, #0a90d4);
            color: white !important;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.875rem;
            display: inline-block;
        ">🔗 LinkedIn</a>
        <a href="https://github.com/mrizkifadhilla82/mrizkifadhilla82" target="_blank" style="
            background: linear-gradient(135deg, #1a1a2e, #2d2d4e);
            color: white !important;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.875rem;
            border: 1px solid #334155;
            display: inline-block;
        ">💻 GitHub</a>
        <a href="mailto:mrizky12@gmail.com" style="
            background: linear-gradient(135deg, #7C3AED, #6D28D9);
            color: white !important;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.875rem;
            display: inline-block;
        ">✉️ Email</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── QUICK STATS ───────────────────────────────────────────────────────────────
st.markdown("### 📊 Quick Stats")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Projects", "3", help="Completed ML/Data Science projects")
with col2:
    st.metric("Tools", "10+", help="Python, SQL, Scikit-learn, TensorFlow, MLflow, Docker, FastAPI...")
with col3:
    st.metric("Models Deployed", "1", help="House Price Prediction API via Docker + FastAPI")
with col4:
    st.metric("Status", "🟢 Open", help="Open to opportunities")

st.markdown("---")

# ── ABOUT ─────────────────────────────────────────────────────────────────────
st.markdown("### 👤 About Me")
st.markdown("""
I am a **Data Scientist** and **Machine Learning Enthusiast** with a strong foundation in
statistical modeling, machine learning, and data pipeline development. I specialize in
turning complex business problems into actionable, data-driven solutions.

My current focus is on **MLOps** — building production-ready systems that bridge the gap
between model development and real-world deployment.
""")

# ── TECH STACK ────────────────────────────────────────────────────────────────
st.markdown("### 🛠️ Tech Stack")

tech_stack = [
    ("🐍", "Python", "#3776AB"),
    ("📊", "SQL", "#CC2927"),
    ("🤖", "Scikit-learn", "#F7931E"),
    ("⚡", "XGBoost", "#0C7A3D"),
    ("🧠", "TensorFlow", "#FF6F00"),
    ("📦", "MLflow", "#0194E2"),
    ("🐳", "Docker", "#2496ED"),
    ("🚀", "FastAPI", "#009688"),
    ("📈", "Pandas", "#150458"),
    ("🔢", "NumPy", "#013243"),
]

cols = st.columns(5)
for i, (icon, name, color) in enumerate(tech_stack):
    with cols[i % 5]:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #111827, #1E293B);
            border: 1px solid #1E3A5F;
            border-radius: 10px;
            padding: 12px 8px;
            text-align: center;
            margin-bottom: 10px;
        ">
            <div style="font-size: 1.5rem; margin-bottom: 4px;">{icon}</div>
            <div style="font-size: 0.8rem; font-weight: 600; color: #94A3B8;">{name}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ── FEATURED PROJECTS PREVIEW ─────────────────────────────────────────────────
st.markdown("### 🚀 Featured Projects")
st.markdown("*Click on a project to see full details and business context.*")

# CSS hover untuk project cards
st.markdown("""
<style>
.proj-card {
    background: linear-gradient(135deg, #111827, #1E293B);
    border: 1px solid #1E3A5F;
    border-radius: 12px;
    padding: 24px;
    min-height: 200px;
    cursor: pointer;
    transition: all 0.25s ease;
    position: relative;
    overflow: hidden;
}
.proj-card:hover {
    border-color: #3B82F6;
    box-shadow: 0 8px 30px rgba(59, 130, 246, 0.2);
    transform: translateY(-4px);
    background: linear-gradient(135deg, #0f1f3d, #1a2f50);
}
.proj-card:hover .proj-arrow {
    opacity: 1;
    transform: translateX(4px);
}
.proj-arrow {
    opacity: 0;
    transition: all 0.25s ease;
    font-size: 1rem;
    position: absolute;
    top: 16px;
    right: 16px;
    color: #3B82F6;
}
</style>
""", unsafe_allow_html=True)

project_previews = [
    {
        "emoji": "🏠",
        "title": "House Price Prediction",
        "desc": "End-to-end ML pipeline with FastAPI + Docker deployment",
        "tag": "Regression / MLOps",
        "status": "🟢 Deployed",
    },
    {
        "emoji": "🏦",
        "title": "Bank Customer Churn Prediction",
        "desc": "Classification with SMOTE to handle imbalanced data",
        "tag": "Classification / ML",
        "status": "✅ Completed",
    },
    {
        "emoji": "🛍️",
        "title": "E-Commerce RFM Analysis",
        "desc": "Customer segmentation using Recency, Frequency, Monetary analysis",
        "tag": "Analytics",
        "status": "✅ Completed",
    },
]

cols = st.columns(3)
for i, p in enumerate(project_previews):
    with cols[i]:
        st.markdown(f"""
        <a href="/Projects" target="_self" style="text-decoration: none;">
        <div class="proj-card">
            <span class="proj-arrow">→</span>
            <div style="font-size: 2rem; margin-bottom: 8px;">{p['emoji']}</div>
            <div style="
                font-size: 0.65rem;
                font-weight: 600;
                color: #3B82F6;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                margin-bottom: 6px;
            ">{p['tag']} · {p['status']}</div>
            <div style="
                font-size: 0.95rem;
                font-weight: 700;
                color: #F1F5F9;
                margin-bottom: 8px;
            ">{p['title']}</div>
            <div style="font-size: 0.82rem; color: #64748B; line-height: 1.5;">
                {p['desc']}
            </div>
        </div>
        </a>
        """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-top: 32px;">
    <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(59, 130, 246, 0.05); border: 1px solid rgba(59, 130, 246, 0.2); padding: 8px 20px; border-radius: 20px;">
        <span style="font-size: 1.1rem;">🚀</span>
        <span style="font-size: 0.85rem; color: #93C5FD; font-weight: 500; letter-spacing: 0.02em;">More projects are currently in the pipeline. Stay tuned!</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── CONTACT ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### 📬 Get In Touch")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div style="background: #111827; border: 1px solid #1E3A5F; border-radius: 10px; padding: 16px; text-align: center;">
        <div style="font-size: 1.5rem;">✉️</div>
        <div style="font-size: 0.8rem; color: #64748B; margin-top: 4px;">Email</div>
        <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 4px;">mrizky12@gmail.com</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="background: #111827; border: 1px solid #1E3A5F; border-radius: 10px; padding: 16px; text-align: center;">
        <div style="font-size: 1.5rem;">🔗</div>
        <div style="font-size: 0.8rem; color: #64748B; margin-top: 4px;">LinkedIn</div>
        <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 4px;">mrizkifadhilla</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div style="background: #111827; border: 1px solid #1E3A5F; border-radius: 10px; padding: 16px; text-align: center;">
        <div style="font-size: 1.5rem;">💻</div>
        <div style="font-size: 0.8rem; color: #64748B; margin-top: 4px;">GitHub</div>
        <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 4px;">mrizkifadhilla82</div>
    </div>
    """, unsafe_allow_html=True)
