import streamlit as st
import pandas as pd
import requests
import os
import time

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Prediction | Muhammad Rizki Fadhilla",
    page_icon="🤖",
    layout="wide",
)

# ── Load CSS ─────────────────────────────────────────────────────────────────
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = os.path.join(os.path.dirname(__file__), "..", "style.css")
if os.path.exists(css_path):
    load_css(css_path)

API_URL = "http://localhost:8000/predict"

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
    ">🤖 House Price Prediction Pipeline</h1>
    <p style="color: #64748B; font-size: 0.95rem;">
        Upload a CSV file containing property features. The data will be sent to the trained ML model via the FastAPI microservice for batch prediction.
    </p>
</div>
""", unsafe_allow_html=True)

# ── MODEL INFO BANNER ─────────────────────────────────────────────────────────
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(59,130,246,0.08), rgba(20,184,166,0.08));
    border: 1px solid rgba(59,130,246,0.2);
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 12px;
">
    <div style="font-size: 1.5rem;">⚡</div>
    <div>
        <div style="font-size: 0.875rem; font-weight: 600; color: #93C5FD;">Model Pipeline</div>
        <div style="font-size: 0.8rem; color: #64748B;">
            CSV Upload → FastAPI REST Endpoint (localhost:8000) → Batch Prediction Output
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background: rgba(245,158,11,0.05); border: 1px solid rgba(245,158,11,0.2); border-radius: 10px; padding: 14px 16px; margin-bottom: 24px;">
    <div style="font-size: 0.85rem; font-weight: 700; color: #F59E0B; margin-bottom: 6px;">⚠️ Deployment Note</div>
    <div style="font-size: 0.85rem; color: #CBD5E1; line-height: 1.6;">
        The live API prediction endpoint for this demonstration is designed to run locally via Docker (<code>localhost:8000</code>). 
        If you are viewing this portfolio on the cloud (e.g., Streamlit Community Cloud), the prediction pipeline will be temporarily offline unless the FastAPI backend is also deployed to a public server.
    </div>
</div>
""", unsafe_allow_html=True)

# ── FILE UPLOAD ───────────────────────────────────────────────────────────────
st.markdown("### 📁 Upload Dataset for Prediction")

uploaded_file = st.file_uploader("Upload your test.csv file here", type=['csv'])

if uploaded_file is not None:
    try:
        df_test = pd.read_csv(uploaded_file)
        
        st.success(f"File uploaded successfully! Loaded {len(df_test)} rows and {df_test.shape[1]} columns.")
        
        st.markdown("#### 📋 Data Preview")
        st.dataframe(df_test.head(5), use_container_width=True)
        
        st.markdown("---")
        
        # ── TRIGGER PIPELINE ──────────────────────────────────────────────────
        if st.button("🔮 Trigger Prediction Pipeline", type="primary", use_container_width=True):
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            predictions = []
            
            # Predict row by row (or you can send batch if API supports it)
            # Assuming API endpoint /predict accepts one dictionary at a time based on original app.py
            total_rows = len(df_test)
            
            with st.spinner("Processing data through FastAPI..."):
                for index, row in df_test.iterrows():
                    # Update progress
                    progress = int(((index + 1) / total_rows) * 100)
                    progress_bar.progress(progress)
                    status_text.text(f"Predicting row {index + 1} of {total_rows}...")
                    
                    payload = row.to_dict()
                    
                    # Convert NA/NaN to None or 0 to avoid JSON serialization errors
                    payload = {k: (0 if pd.isna(v) else v) for k, v in payload.items()}
                    
                    try:
                        response = requests.post(API_URL, json=payload, timeout=5)
                        if response.status_code == 200:
                            pred_val = response.json().get("prediction", 0)
                            predictions.append(pred_val)
                        else:
                            predictions.append("API Error")
                    except Exception as e:
                        predictions.append("Connection Failed")
                
                status_text.text("Prediction Complete!")
                
                # Add predictions to dataframe
                df_results = df_test.copy()
                df_results['Predicted_Price'] = predictions
                
                st.markdown("---")
                st.markdown("### 📊 Prediction Results")
                
                st.dataframe(df_results, use_container_width=True)
                
                # Download button
                csv = df_results.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Results as CSV",
                    data=csv,
                    file_name='prediction_results.csv',
                    mime='text/csv',
                )
                
    except Exception as e:
        st.error(f"Error reading the CSV file: {str(e)}")
