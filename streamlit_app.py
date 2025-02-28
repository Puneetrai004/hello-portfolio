import streamlit as st
import pandas as pd
import plotly.express as px
import json
from streamlit_lottie import st_lottie
import requests
import os
from pathlib import Path
import random
from datetime import datetime
import base64
import time

# Page configuration
st.set_page_config(
    page_title="Puneet Kumar Rai | ML Engineer & Data Scientist", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

# Custom CSS with modern dark theme
def set_custom_theme():
    st.markdown("""
    <style>
    /* Global styles */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: #f0f2f5;
    }
    
    [data-testid="stSidebar"] {
        background-color: rgba(21, 31, 46, 0.8);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem 1rem;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-weight: 700;
        color: #e0f7fa;
    }
    
    h1 {
        background: linear-gradient(90deg, #00c6ff, #8e2de2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        margin-bottom: 1.5rem !important;
    }
    
    .card {
        background-color: rgba(42, 52, 65, 0.7);
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    
    .skill-tag {
        display: inline-block;
        background: linear-gradient(to right, #4776E6, #8E54E9);
        color: white;
        padding: 5px 10px;
        margin: 5px;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    .badge {
        display: inline-block;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        transition: all 0.3s ease;
    }
    
    .timeline-item {
        position: relative;
        padding-left: 30px;
        margin-bottom: 2rem;
    }
    
    .timeline-item:before {
        content: "";
        position: absolute;
        left: 0;
        top: 5px;
        width: 15px;
        height: 15px;
        border-radius: 50%;
        background: linear-gradient(to right, #4776E6, #8E54E9);
    }
    
    .counter {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #00c6ff, #8e2de2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .social-button {
        display: flex;
        align-items: center;
        padding: 0.8rem 1.2rem;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.05);
        transition: all 0.3s ease;
        color: white !important;
        text-decoration: none !important;
    }
    
    .social-button:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-2px);
    }
    
    .experience-card {
        background: rgba(42, 52, 65, 0.7);
        border-left: 4px solid #8E54E9;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

set_custom_theme()

# Helper functions
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def timeline_item(period, title, description):
    st.markdown(f"""
    <div class="timeline-item">
        <div style="font-size: 0.9rem; color: #b3e5fc;">{period}</div>
        <div style="font-size: 1.2rem; font-weight: 600; margin: 0.3rem 0;">{title}</div>
        <div style="color: #e0f7fa;">{description}</div>
    </div>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<h1 style="text-align: center;">Puneet Kumar Rai</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; color: #81d4fa;">Data Scientist | ML Engineer</h3>', unsafe_allow_html=True)
    
    # Profile Image
    st.markdown("""
    <div style="text-align: center; margin: 1.5rem 0;">
        <img src="https://raw.githubusercontent.com/Puneetrai004/portfolio/main/assets/profile.jpg" 
            style="width: 80%; border-radius: 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.4);">
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    nav_selection = st.radio("", ["🏠 Home", "🚀 Projects", "🛠️ Skills", "💼 Experience", "🎓 Education", "📬 Contact"])
    
    # Contact Info
    st.markdown("""
    <div style="margin: 2rem 0;">
        <h3 style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📨 Contact</h3>
        <p>📧: justpuneetrai@gmail.com<br>
           📱: +91 9555230429<br>
           🏠: Chandani, Ghazipur, UP</p>
    </div>
    """, unsafe_allow_html=True)

# Main Content
if nav_selection == "🏠 Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <h1 style="font-size: 3.5rem; margin-bottom: 0.5rem;">
            Puneet Kumar Rai <span style="font-size: 2rem;">👋</span>
        </h1>
        <h2 style="font-size: 2rem; margin-bottom: 2rem;">
            B.Tech Mining Engineering @ IIT (BHU)
        </h2>
        <div class="card">
            <h3>🌟 Professional Summary</h3>
            <ul>
                <li>Machine Learning Specialist with 3+ industrial projects</li>
                <li>94% accuracy in mineral classification using CNN</li>
                <li>Experienced event manager for 60,000+ attendees</li>
                <li>Award-winning technical photographer</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        lottie_tech = load_lottie("https://assets9.lottiefiles.com/packages/lf20_hi95bvmx/tech.json")
        if lottie_tech:
            st_lottie(lottie_tech, height=300, key="tech")

elif nav_selection == "🚀 Projects":
    st.header("🔭 Featured Projects")
    
    with st.expander("Mineral Classification using ML (94% Accuracy)", expanded=True):
        col1, col2 = st.columns([3,2])
        with col1:
            st.markdown("""
            <div class="card">
                <h3>🪨 CNN-based Mineral Classification</h3>
                <div class="badge">Sep 2023 - Nov 2023</div>
                <ul>
                    <li>Implemented EfficientNet architecture under Dr. Amarendra Kumar</li>
                    <li>Integrated OpenCV for image preprocessing</li>
                    <li>Achieved 94% validation accuracy</li>
                </ul>
                <div style="margin-top: 1rem;">
                    <span class="skill-tag">Python</span>
                    <span class="skill-tag">TensorFlow</span>
                    <span class="skill-tag">Computer Vision</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.image("https://via.placeholder.com/600x400.png?text=Mineral+Classification+Demo", use_column_width=True)
    
    with st.expander("Employee Performance Prediction (93% Accuracy)"):
        st.markdown("""
        <div class="card">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div>
                    <h3>📈 ML Pipeline Development</h3>
                    <ul>
                        <li>Optimized Random Forest with GridSearchCV</li>
                        <li>Feature engineering & data preprocessing</li>
                        <li>Automated EDA process</li>
                    </ul>
                </div>
                <div>
                    <h3>📊 Performance Metrics</h3>
                    <div style="display: flex; justify-content: space-around; margin-top: 1rem;">
                        <div style="text-align: center;">
                            <div class="counter">93%</div>
                            <div>Accuracy</div>
                        </div>
                        <div style="text-align: center;">
                            <div class="counter">0.91</div>
                            <div>F1-Score</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif nav_selection == "🛠️ Skills":
    st.header("🛠️ Technical Arsenal")
    
    tab1, tab2, tab3 = st.tabs(["Programming", "ML Stack", "Soft Skills"])
    
    with tab1:
        st.markdown("""
        <div class="card">
            <h3>💻 Languages & Tools</h3>
            <div style="columns: 2;">
                <div style="break-inside: avoid;">
                    <h4>Core Languages</h4>
                    <div class="skill-tag">Python</div>
                    <div class="skill-tag">C++</div>
                    <div class="skill-tag">SQL</div>
                </div>
                <div style="break-inside: avoid;">
                    <h4>Development Tools</h4>
                    <div class="skill-tag">VS Code</div>
                    <div class="skill-tag">Jupyter</div>
                    <div class="skill-tag">Git</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="card">
            <h3>🤖 Machine Learning Stack</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
                <div class="skill-tag">TensorFlow</div>
                <div class="skill-tag">Scikit-learn</div>
                <div class="skill-tag">OpenCV</div>
                <div class="skill-tag">PyTorch</div>
                <div class="skill-tag">NLTK</div>
                <div class="skill-tag">Pandas</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="card">
            <h3>🌟 Professional Skills</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                <div class="badge">Team Leadership</div>
                <div class="badge">Event Management</div>
                <div class="badge">Public Speaking</div>
                <div class="badge">Technical Mentoring</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif nav_selection == "💼 Experience":
    st.header("💼 Leadership Experience")
    
    with st.container():
        col1, col2 = st.columns([1,3])
        with col1:
            st.image("https://img.icons8.com/3d-fluency/94/conference.png", width=100)
        with col2:
            st.markdown("""
            <div class="experience-card">
                <h3>🎪 PR Executive - Kashiyatra'24</h3>
                <div class="badge">Nov 2023 - Feb 2024</div>
                <div class="badge">60,000+ Participants</div>
                <ul>
                    <li>Led 25-member team for Asia's largest college fest</li>
                    <li>Coordinated 90+ events across 3 days</li>
                    <li>Managed VIP guests and media relations</li>
                    <li>Handled budget of ₹50+ lakhs</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    with st.container():
        col1, col2 = st.columns([1,3])
        with col1:
            st.image("https://img.icons8.com/3d-fluency/94/student-male--v3.png", width=100)
        with col2:
            st.markdown("""
            <div class="experience-card">
                <h3>👨🏫 Induction Mentor</h3>
                <div class="badge">Aug 2023 - May 2024</div>
                <div class="badge">20+ Freshers</div>
                <ul>
                    <li>Academic guidance & career counseling</li>
                    <li>Organized department orientation</li>
                    <li>Resource development for juniors</li>
                    <li>Conducted weekly mentorship sessions</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

elif nav_selection == "🎓 Education":
    st.header("🎓 Academic Journey")
    
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        <div class="card">
            <h3>🏛️ IIT (BHU) Varanasi</h3>
            <div style="display: flex; justify-content: space-between;">
                <div>
                    <div class="counter">8.13</div>
                    <div>CGPA (2022-2026)</div>
                </div>
                <div>
                    <div class="badge">Ongoing</div>
                    <div>B.Tech Mining Engineering</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        timeline_item(
            "2019-2021",
            "🔬 Senior Secondary (CBSE XII)",
            "MJRP Public School, Ghazipur · 96% · School Topper in Physics & Chemistry"
        )
        
        timeline_item(
            "2017-2019",
            "📚 Secondary (CBSE X)",
            "MJRP Public School, Ghazipur · 95.4% · Consistent Academic Excellence"
        )

elif nav_selection == "📬 Contact":
    st.header("📬 Let's Connect!")
    
    col1, col2 = st.columns(2)
    with col1:
        with open("Puneet_Rai_Resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        
        st.markdown("""
        <div class="card">
            <h3>📌 Contact Information</h3>
            <div style="line-height: 2;">
                ✉️ <strong>Email:</strong> justpuneetrai@gmail.com<br>
                📱 <strong>Phone:</strong> +91 95552 30429<br>
                🏠 <strong>Address:</strong><br>
                Village Chandani, Post Kundesar,<br>
                Ghazipur, Uttar Pradesh 233227
            </div>
            <h3 style="margin-top: 1.5rem;">📎 Attachments</h3>
        """, unsafe_allow_html=True)
        
        st.download_button(
            label="📄 Download Full Resume",
            data=PDFbyte,
            file_name="Puneet_Rai_Resume.pdf",
            mime="application/octet-stream",
        )
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>🌐 Digital Presence</h3>
            <div style="display: grid; gap: 1rem; margin-top: 1.5rem;">
                <a href="#" class="social-button" style="text-decoration: none;">
                    <span>🔗 LinkedIn</span>
                </a>
                <a href="#" class="social-button" style="text-decoration: none;">
                    <span>🐱 GitHub</span>
                </a>
                <a href="#" class="social-button" style="text-decoration: none;">
                    <span>📷 Instagram</span>
                </a>
            </div>
            <h3 style="margin-top: 1.5rem;">📅 Schedule Meeting</h3>
            <button class="stButton" style="width: 100%; padding: 1rem;">
                🗓️ Book Calendar Slot
            </button>
        </div>
        """, unsafe_allow_html=True)

# Run with: streamlit run app.py
