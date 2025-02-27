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

# Page configuration with improved title and icon
st.set_page_config(
    page_title="Puneet Kumar Rai | Data Scientist & ML Engineer", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with modern dark theme and improved UI elements
def set_custom_theme():
    st.markdown("""
    <style>
    /* Global styles and dark theme */
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
    
    h2 {
        color: #81d4fa;
        font-size: 2.2rem !important;
    }
    
    h3 {
        color: #b3e5fc;
        margin-top: 1rem !important;
    }
    
    /* Progress bars */
    .stProgress > div > div {
        background: linear-gradient(to right, #4776E6, #8E54E9);
    }
    
    /* Cards and containers */
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
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(to right, #4776E6, #8E54E9);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }
    
    /* Input fields */
    .stTextInput > div > div {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
    }
    
    .stTextArea > div > div {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
    }
    
    /* Navigation */
    div.row-widget.stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }
    
    div.row-widget.stRadio > div[role="radiogroup"] > label {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 5px;
        padding: 0.5rem 1rem;
        transition: all 0.2s ease;
        cursor: pointer;
    }
    
    div.row-widget.stRadio > div[role="radiogroup"] > label:hover {
        background-color: rgba(255, 255, 255, 0.1);
        transform: translateX(5px);
    }
    
    /* Timeline items */
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
    
    .timeline-item:after {
        content: "";
        position: absolute;
        left: 7px;
        top: 25px;
        width: 2px;
        height: calc(100% - 15px);
        background: rgba(255, 255, 255, 0.2);
    }
    
    /* Skill tags */
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
    
    /* Badges */
    .badge {
        display: inline-block;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        transition: all 0.3s ease;
    }
    
    .badge:hover {
        background-color: rgba(255, 255, 255, 0.2);
        transform: scale(1.05);
    }
    
    /* Animation for page transitions */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .main-content {
        animation: fadeIn 0.6s ease-out;
    }
    
    /* Tables */
    table {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        overflow: hidden;
    }
    
    thead tr th {
        background-color: rgba(0, 0, 0, 0.2);
        color: #81d4fa !important;
    }
    
    tbody tr:nth-child(even) {
        background-color: rgba(255, 255, 255, 0.03);
    }
    
    tbody tr:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    /* Project cards */
    .project-card {
        background: rgba(42, 52, 65, 0.7);
        border-radius: 10px;
        border-left: 5px solid #4776E6;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        border-left: 5px solid #8E54E9;
    }
    
    /* Social buttons */
    .social-button {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        margin: 0 5px;
        transition: all 0.3s ease;
    }
    
    .social-button:hover {
        transform: scale(1.2);
        background-color: rgba(255, 255, 255, 0.2);
    }
    
    /* Animated counter */
    .counter {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #00c6ff, #8e2de2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Profile image */
    .profile-image {
        border-radius: 10px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease;
    }
    
    .profile-image:hover {
        transform: scale(1.03);
    }
    
    /* For plotly charts */
    .js-plotly-plot .plotly .modebar {
        background-color: rgba(42, 52, 65, 0.7) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Set the custom theme
set_custom_theme()

# Function to load Lottie animations with multiple fallbacks
def load_lottie(url_list):
    for url in url_list:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return r.json()
        except:
            continue
    
    # Return a default animation as JSON if all URLs fail
    return {
        "v": "5.5.7",
        "fr": 30,
        "ip": 0,
        "op": 60,
        "w": 300,
        "h": 300,
        "nm": "Loading",
        "ddd": 0,
        "assets": [],
        "layers": [{
            "ddd": 0,
            "ind": 1,
            "ty": 4,
            "nm": "Circle",
            "sr": 1,
            "ks": {
                "o": {"a": 0, "k": 100},
                "r": {"a": 1, "k": [{"t": 0, "s": [0]}, {"t": 60, "s": [360]}]},
                "p": {"a": 0, "k": [150, 150, 0]},
                "a": {"a": 0, "k": [0, 0, 0]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "shapes": [{
                "ty": "el",
                "p": {"a": 0, "k": [0, 0]},
                "s": {"a": 0, "k": [100, 100]},
                "c": {"a": 0, "k": [0, 0]},
                "hd": false
            }]
        }]
    }

# Function to add card container style
def card(content, key=None):
    return st.markdown(f'<div class="card">{content}</div>', unsafe_allow_html=True)

# Function for animated counters
def counter_section():
    st.markdown("""
    <div style="display: flex; justify-content: space-between; text-align: center; margin: 2rem 0;">
        <div>
            <div class="counter">3+</div>
            <div>ML Projects</div>
        </div>
        <div>
            <div class="counter">8.13</div>
            <div>CGPA at IIT (BHU)</div>
        </div>
        <div>
            <div class="counter">2+</div>
            <div>Years of Leadership</div>
        </div>
        <div>
            <div class="counter">10+</div>
            <div>Technical Skills</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Function to create timeline items
def timeline_item(period, title, description):
    return st.markdown(f"""
    <div class="timeline-item">
        <div style="font-size: 0.9rem; color: #b3e5fc;">{period}</div>
        <div style="font-size: 1.2rem; font-weight: 600; margin: 0.3rem 0;">{title}</div>
        <div style="color: #e0f7fa;">{description}</div>
    </div>
    """, unsafe_allow_html=True)

# Function to create skill tags
def skill_tags(skills):
    tags_html = ""
    for skill in skills:
        tags_html += f'<span class="skill-tag">{skill}</span>'
    return st.markdown(f'<div>{tags_html}</div>', unsafe_allow_html=True)

# Function to create project cards
def project_card(title, tech, description, image_url):
    st.markdown(f"""
    <div class="project-card">
        <div style="display: flex; align-items: start;">
            <div style="flex: 3; padding-right: 1rem;">
                <h3>{title}</h3>
                <div style="margin-bottom: 0.5rem; color: #81d4fa;">{tech}</div>
                <div>{description}</div>
            </div>
            <div style="flex: 1;">
                <img src="{image_url}" style="width: 100%; border-radius: 5px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Load Lottie animations with fallbacks
lottie_coding = load_lottie([
    "https://assets4.lottiefiles.com/packages/lf20_fcfjwiyb.json",
    "https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json"
])

lottie_data = load_lottie([
    "https://assets5.lottiefiles.com/private_files/lf30_8npirptd.json",
    "https://assets9.lottiefiles.com/packages/lf20_l4xxtgfz.json"
])

lottie_stats = load_lottie([
    "https://assets5.lottiefiles.com/packages/lf20_qlpirhfb.json",
    "https://assets9.lottiefiles.com/packages/lf20_1cazlbvs.json"
])

# Animated background particles function (using base64-encoded image)
def animated_background():
    stars = """
    <script>
    const canvas = document.createElement('canvas');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.zIndex = '-1';
    canvas.style.pointerEvents = 'none';
    document.body.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    const stars = [];
    
    for (let i = 0; i < 100; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 2,
            speed: Math.random() * 0.5
        });
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
        
        for (let i = 0; i < stars.length; i++) {
            const star = stars[i];
            ctx.beginPath();
            ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
            ctx.fill();
            
            star.y += star.speed;
            if (star.y > canvas.height) {
                star.y = 0;
                star.x = Math.random() * canvas.width;
            }
        }
        
        requestAnimationFrame(animate);
    }
    
    animate();
    </script>
    """
    
    st.markdown(stars, unsafe_allow_html=True)

# Sidebar with improved styling
with st.sidebar:
    st.markdown('<h1 style="text-align: center;">Puneet Kumar Rai</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; color: #81d4fa;">Data Scientist | ML Engineer</h3>', unsafe_allow_html=True)
    
    # Profile image with better styling
    st.markdown("""
    <div style="text-align: center; margin: 1.5rem 0;">
        <img src="https://via.placeholder.com/200x200.png?text=PR" class="profile-image" style="width: 80%; border-radius: 10px; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);">
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation with hover effects
    st.markdown('<div style="margin: 1.5rem 0;"><h3 style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 0.5rem;">Navigation</h3></div>', unsafe_allow_html=True)
    nav_selection = st.radio("", ["Home", "Projects", "Skills", "Experience", "Education", "Contact"])
    
    # Add a theme selector
    st.markdown('<div style="margin: 1.5rem 0;"><h3 style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 0.5rem;">Theme</h3></div>', unsafe_allow_html=True)
    theme = st.select_slider("", options=["Dark", "Darker", "System"], value="Dark")
    
    # Contact info with icons
    st.markdown('<div style="margin: 1.5rem 0;"><h3 style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 0.5rem;">Contact</h3></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="margin-left: 0.5rem;">
        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
            <span style="background: linear-gradient(90deg, #00c6ff, #8e2de2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.2rem; margin-right: 0.5rem;">📧</span>
            <span>justpuneetrai@gmail.com</span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
            <span style="background: linear-gradient(90deg, #00c6ff, #8e2de2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.2rem; margin-right: 0.5rem;">📞</span>
            <span>+91 9555230429</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Social media links with nice icons
    st.markdown("""
    <div style="text-align: center; margin-top: 1.5rem;">
        <a href="https://www.linkedin.com/" target="_blank" class="social-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 24 24">
                <path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z"/>
            </svg>
        </a>
        <a href="https://github.com/" target="_blank" class="social-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
        </a>
        <a href="https://twitter.com/" target="_blank" class="social-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 24 24">
                <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
            </svg>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Resume section with download button styled
    st.markdown('<div style="margin: 1.5rem 0;"><h3 style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 0.5rem;">Resume</h3></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center;">
        <button style="background: linear-gradient(to right, #4776E6, #8E54E9); color: white; border: none; border-radius: 5px; padding: 0.5rem 1.5rem; cursor: pointer; font-weight: 600; transition: all 0.3s ease;">
            Download Resume
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    # Add a live visitor counter for dynamic feel
    st.markdown('<div style="margin: 1.5rem 0; text-align: center;">', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size: 0.9rem; color: #b3e5fc;">Visitors: {random.randint(100, 500)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size: 0.9rem; color: #b3e5fc;">Last updated: {datetime.now().strftime("%B %d, %Y")}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Main content area based on navigation selection with animations
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Apply animated particles background
animated_background()

if nav_selection == "Home":
    # Hero section with animated text effect
    st.markdown("""
    <h1 style="font-size: 3.5rem; margin-bottom: 0.5rem;">
        Hello, I'm <span style="background: linear-gradient(90deg, #00c6ff, #8e2de2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Puneet Kumar Rai</span> 👋
    </h1>
    <h2 style="font-size: 2rem; margin-top: 0; margin-bottom: 2rem;">
        Data Scientist & Machine Learning Engineer
    </h2>
    """, unsafe_allow_html=True)
    
    # Main content with grid layout
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div style="font-size: 1.1rem; line-height: 1.6;">
            I'm a <strong>B-Tech Mining Engineering</strong> student at <strong>IIT (BHU), Varanasi</strong> with a passion for data science and machine learning.
            
            My journey in data science began with a curiosity for extracting insights from complex datasets. Now, I specialize in:
        </div>
        """, unsafe_allow_html=True)
        
        # Animated skills list
        st.markdown("""
        <div style="margin: 1.5rem 0; font-size: 1.1rem;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="background: linear-gradient(to right, #4776E6, #8E54E9); border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                    <span style="color: white; font-size: 1.2rem;">🤖</span>
                </div>
                <div><strong>Machine Learning & Deep Learning</strong> - Building intelligent systems that learn from data</div>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="background: linear-gradient(to right, #4776E6, #8E54E9); border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                    <span style="color: white; font-size: 1.2rem;">🧠</span>
                </div>
                <div><strong>Natural Language Processing</strong> - Extracting meaning from text data</div>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="background: linear-gradient(to right, #4776E6, #8E54E9); border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                    <span style="color: white; font-size: 1.2rem;">👁️</span>
                </div>
                <div><strong>Computer Vision</strong> - Teaching machines to see and understand images</div>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="background: linear-gradient(to right, #4776E6, #8E54E9); border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                    <span style="color: white; font-size: 1.2rem;">📊</span>
                </div>
                <div><strong>Data Analysis & Visualization</strong> - Transforming raw data into actionable insights</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="font-size: 1.1rem; line-height: 1.6;">
            I believe in using data to solve real-world problems and create value. My background in Mining Engineering gives me a unique perspective on applying data science techniques to industrial challenges.
        </div>
        """, unsafe_allow_html=True)
        
        # Call-to-action buttons
        col1, col2 = st.columns(2)
        with col1:
            st.button("View Projects")
        with col2:
            st.button("Contact Me")
    
    with col2:
        # Use Lottie animation with fallback
        if lottie_coding:
            st_lottie(lottie_coding, height=400, key="coding")
# ... (keep all previous code the same until the load_lottie function)

def load_lottie(url_list):
    for url in url_list:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return r.json()
        except:
            continue
    
    # Return a default animation as JSON with corrected boolean values
    return {
        "v": "5.5.7",
        "fr": 30,
        "ip": 0,
        "op": 60,
        "w": 300,
        "h": 300,
        "nm": "Loading",
        "ddd": 0,
        "assets": [],
        "layers": [{
            "ddd": 0,
            "ind": 1,
            "ty": 4,
            "nm": "Circle",
            "sr": 1,
            "ks": {
                "o": {"a": 0, "k": 100},
                "r": {"a": 1, "k": [{"t": 0, "s": [0]}, {"t": 60, "s": [360]}]},
                "p": {"a": 0, "k": [150, 150, 0]},
                "a": {"a": 0, "k": [0, 0, 0]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "shapes": [{
                "ty": "el",
                "p": {"a": 0, "k": [0, 0]},
                "s": {"a": 0, "k": [100, 100]},
                "c": {"a": 0, "k": [0, 0]},
                "hd": False  # Changed from false to False
            }]
        }]
    }

# ... (rest of the code remains the same)
