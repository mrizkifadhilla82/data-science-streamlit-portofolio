import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.projects import PROJECTS

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Projects | Muhammad Rizki Fadhilla",
    page_icon="📂",
    layout="wide",
)

# ── Load CSS ─────────────────────────────────────────────────────────────────
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = os.path.join(os.path.dirname(__file__), "..", "style.css")
if os.path.exists(css_path):
    load_css(css_path)

# ── PAGE HEADER ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-bottom: 32px;">
    <h1 style="
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #3B82F6, #14B8A6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 8px;
    ">📂 My Projects</h1>
    <p style="color: #64748B; font-size: 0.95rem;">
        Select a project below to see full details — from business problem and pain points to solutions and impact.
    </p>
</div>
""", unsafe_allow_html=True)

# ── TABS ──────────────────────────────────────────────────────────────────────
PROJECT_EMOJIS = {
    "house-price-prediction": "🏠",
    "bank-churn-prediction": "🏦",
    "ecommerce-rfm-analysis": "🛍️",
}

tab_labels = [
    f"{PROJECT_EMOJIS.get(p['id'], '📌')} {p['title']}"
    for p in PROJECTS
]

tabs = st.tabs(tab_labels)

# ── RENDER EACH PROJECT IN ITS OWN TAB ───────────────────────────────────────
def render_project(project):
    emoji = PROJECT_EMOJIS.get(project["id"], "📌")

    # Header card
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #0D1120, #111827);
        border: 1px solid #1E3A5F;
        border-radius: 14px;
        padding: 24px 28px;
        margin-bottom: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    ">
        <div>
            <span style="
                font-size: 0.65rem;
                font-weight: 700;
                color: #3B82F6;
                text-transform: uppercase;
                letter-spacing: 0.1em;
                background: rgba(59,130,246,0.1);
                border: 1px solid rgba(59,130,246,0.2);
                padding: 3px 10px;
                border-radius: 20px;
            ">{project['domain']}</span>
            <h2 style="
                font-size: 1.5rem;
                font-weight: 700;
                color: #F1F5F9;
                margin: 10px 0 0 0;
            ">{emoji} {project['title']}</h2>
        </div>
        <div style="
            font-size: 1.1rem;
            font-weight: 600;
            color: #94A3B8;
        ">{project['status']}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Display Project Image if exists ──
    image_file = project.get("image_path", "")
    if os.path.exists(image_file):
        # Membungkus dengan kolom agar gambar ada di tengah dan tidak terlalu besar
        col_img_left, col_img_center, col_img_right = st.columns([1, 3, 1])
        with col_img_center:
            st.image(image_file, use_container_width=True, caption=project['title'])
    else:
        st.info(f"🖼️ **Placeholder for {project['title']} Image.** Please save an image as `{image_file}` in the main project folder to fulfill the assignment guideline.")

    # Business Problem + Pain Points | Solution + Impact
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style="
            background: rgba(239,68,68,0.05);
            border: 1px solid rgba(239,68,68,0.15);
            border-radius: 10px;
            padding: 16px 20px;
            margin-bottom: 12px;
        ">
            <div style="font-size: 0.8rem; font-weight: 700; color: #EF4444; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em;">
                🔴 Business Problem
            </div>
            <p style="font-size: 0.875rem; color: #CBD5E1; line-height: 1.7; margin: 0;">
                {project['business_problem'].strip()}
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            """
            <div style="
                background: rgba(245,158,11,0.05);
                border: 1px solid rgba(245,158,11,0.15);
                border-radius: 10px;
                padding: 16px 20px;
                margin-bottom: 12px;
            ">
                <div style="font-size: 0.8rem; font-weight: 700; color: #F59E0B; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em;">
                    ⚠️ Pain Points
                </div>
            """
            + "".join([
                f'<div style="font-size: 0.85rem; color: #CBD5E1; margin-bottom: 6px; padding-left: 4px;">• {pp}</div>'
                for pp in project['pain_points']
            ])
            + "</div>",
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(f"""
        <div style="
            background: rgba(16,185,129,0.05);
            border: 1px solid rgba(16,185,129,0.15);
            border-radius: 10px;
            padding: 16px 20px;
            margin-bottom: 12px;
        ">
            <div style="font-size: 0.8rem; font-weight: 700; color: #10B981; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em;">
                ✅ Solution & Approach
            </div>
            <p style="font-size: 0.875rem; color: #CBD5E1; line-height: 1.7; margin: 0;">
                {project['solution'].strip()}
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            """
            <div style="
                background: rgba(59,130,246,0.05);
                border: 1px solid rgba(59,130,246,0.15);
                border-radius: 10px;
                padding: 16px 20px;
                margin-bottom: 12px;
            ">
                <div style="font-size: 0.8rem; font-weight: 700; color: #3B82F6; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em;">
                    📊 Impact & Results
                </div>
            """
            + "".join([
                f'<div style="font-size: 0.85rem; color: #CBD5E1; margin-bottom: 6px; padding-left: 4px;">✦ {imp}</div>'
                for imp in project['impact']
            ])
            + "</div>",
            unsafe_allow_html=True,
        )

    # Tools & Links
    tools_html = " ".join([
        f'<span style="background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.2); color: #93C5FD; font-size: 0.75rem; font-weight: 600; padding: 3px 10px; border-radius: 20px;">{t}</span>'
        for t in project['tools']
    ])

    links_html = f'<a href="{project["github"]}" target="_blank" style="background: rgba(255,255,255,0.05); border: 1px solid #334155; color: #94A3B8; font-size: 0.8rem; font-weight: 600; padding: 6px 14px; border-radius: 6px; text-decoration: none; margin-right: 8px;">💻 GitHub</a>'

    if project.get("demo"):
        links_html += f'<a href="{project["demo"]}" target="_blank" style="background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.3); color: #3B82F6; font-size: 0.8rem; font-weight: 600; padding: 6px 14px; border-radius: 6px; text-decoration: none;">🌐 Live Demo</a>'

    st.markdown(f"""
    <div style="margin-top: 8px; padding: 16px 0 8px 0; border-top: 1px solid #1E3A5F;">
        <div style="margin-bottom: 12px;">
            <span style="font-size: 0.75rem; color: #64748B; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">🛠️ Tools: </span>
            {tools_html}
        </div>
        <div>{links_html}</div>
    </div>
    """, unsafe_allow_html=True)


for tab, project in zip(tabs, PROJECTS):
    with tab:
        render_project(project)
