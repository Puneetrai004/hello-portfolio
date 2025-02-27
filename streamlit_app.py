import streamlit as st
import pandas as pd
import plotly.express as px
import json
from streamlit_lottie import st_lottie
import requests
import os
from pathlib import Path

# Page configuration
st.set_page_config(page_title="Puneet Kumar Rai - Data Science Portfolio", 
                   page_icon="📊", 
                   layout="wide")

# Custom CSS
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except:
        # Define fallback CSS if file not found
        st.markdown("""
        <style>
        body {
            font-family: 'Inter', sans-serif;
            color: #262730;
        }
        h1, h2, h3, h4, h5, h6 {
            font-weight: 700;
            color: #1a1a1a;
        }
        .stProgress > div > div {
            background-color: #4169E1;
        }
        </style>
        """, unsafe_allow_html=True)

# Try to use custom CSS, fallback to default if not found
css_path = Path("style/style.css")
if css_path.exists():
    local_css(css_path)
else:
    local_css(None)  # Will use fallback CSS

# Function to load Lottie animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Load animations with fallback
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_data = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_8npirptd.json")

# Sidebar
with st.sidebar:
    st.title("Puneet Kumar Rai")
    st.subheader("Data Scientist | ML Engineer")
    
    # Use a placeholder image instead of file
    st.image("https://via.placeholder.com/200x200.png?text=Puneet+Rai", width=200)
    
    st.markdown("### Navigation")
    nav_selection = st.radio("", ["Home", "Projects", "Skills", "Experience", "Education", "Contact"])
    
    st.markdown("### Contact")
    st.markdown("📧 justpuneetrai@gmail.com")
    st.markdown("📞 +91 9555230429")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/)")
    st.markdown("🔗 [GitHub](https://github.com/)")
    
    # Remove resume download for now
    st.markdown("### Resume")
    st.markdown("Available upon request")

# Main content area based on navigation selection
if nav_selection == "Home":
    st.markdown("# Hello, I'm Puneet Kumar Rai 👋")
    st.markdown("## Data Scientist & Machine Learning Engineer")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        I'm a B-Tech Mining Engineering student at IIT (BHU), Varanasi with a passion for data science and machine learning.
        
        My journey in data science began with a curiosity for extracting insights from complex datasets. Now, I specialize in:
        
        - 🤖 Machine Learning & Deep Learning
        - 🧠 Natural Language Processing
        - 👁️ Computer Vision
        - 📊 Data Analysis & Visualization
        
        I believe in using data to solve real-world problems and create value. My background in Mining Engineering gives me a unique perspective on applying data science techniques to industrial challenges.
        
        Explore my projects and skills to see how I can leverage data for your organization!
        """)
    with col2:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.image("https://via.placeholder.com/300x300.png?text=Data+Science", width=300)
    
    # Brief stats
    st.markdown("## At a Glance")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("### 3+")
        st.markdown("Major ML Projects")
    with col2:
        st.markdown("### 8.13")
        st.markdown("CGPA at IIT (BHU)")
    with col3:
        st.markdown("### 2+")
        st.markdown("Years of Leadership")
    with col4:
        st.markdown("### 4+")
        st.markdown("Technical Skills")

elif nav_selection == "Projects":
    st.markdown("# Projects Portfolio")
    st.markdown("Explore my data science and machine learning projects")
    
    # Project 1
    with st.container():
        st.subheader("Mineral Classification using CNN")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Technologies:** Computer Vision, CNN, TensorFlow, EfficientNet
            
            **Duration:** Sep 2023 - Nov 2023
            
            **Supervisor:** Dr. Amarendra Kumar
            
            ### Description:
            - Researched about Image Segmentation, Classification and Object Detection to create a Machine Learning Model
            - Implemented CNN Efficient-Net Architecture 
            - Developed a Model to classify Minerals with 94 percent Accuracy
            
            """)
        with col2:
            st.image("https://via.placeholder.com/400x300.png?text=Mineral+Classification", width=300)
            
        st.markdown("---")
    
    # Project 2
    with st.container():
        st.subheader("Twitter Sentiment Analysis")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Technologies:** NLP, Text Preprocessing, Machine Learning
            
            ### Description:
            - Preprocessed tweets with stemming, lemmatization, and feature extraction using Bag-of-Words and TF-IDF
            - Achieved an F1-score of 0.55
            - Developed and evaluated sentiment classification models using diverse text representations
            - Optimized accuracy through advanced preprocessing techniques
            
            """)
        with col2:
            st.image("https://via.placeholder.com/400x300.png?text=Twitter+Sentiment", width=300)
            
        st.markdown("---")
    
    # Project 3
    with st.container():
        st.subheader("Predicting Employee Performance Index")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Technologies:** Feature Engineering, Supervised Learning, ML Algorithms
            
            ### Description:
            - Performed EDA, Label Encoding, and Standardization to preprocess data
            - Identified key predictors through correlation analysis
            - Trained predictive models using Logistic Regression, Random Forest, SVM, and XGBoost
            - Achieved 93% accuracy through hyperparameter tuning of Random Forest with GridSearchCV
            
            """)
        with col2:
            st.image("https://via.placeholder.com/400x300.png?text=Employee+Performance", width=300)
            
        st.markdown("---")

elif nav_selection == "Skills":
    st.markdown("# Skills & Expertise")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("## Technical Skills")
        
        # Programming Languages
        st.markdown("### Programming Languages")
        lang_col1, lang_col2, lang_col3, lang_col4 = st.columns(4)
        with lang_col1:
            st.markdown("**Python**")
            st.progress(0.9)
        with lang_col2:
            st.markdown("**C++**")
            st.progress(0.8)
        with lang_col3:
            st.markdown("**C**")
            st.progress(0.7)
        with lang_col4:
            st.markdown("**MySQL**")
            st.progress(0.75)
        
        # Data Science Libraries
        st.markdown("### Data Science & ML Libraries")
        ds_col1, ds_col2, ds_col3, ds_col4 = st.columns(4)
        with ds_col1:
            st.markdown("**Pandas**")
            st.progress(0.95)
        with ds_col2:
            st.markdown("**NumPy**")
            st.progress(0.9)
        with ds_col3:
            st.markdown("**Scikit-learn**")
            st.progress(0.85)
        with ds_col4:
            st.markdown("**Matplotlib/Seaborn**")
            st.progress(0.8)
        
        # ML/AI Skills
        st.markdown("### Machine Learning & AI")
        ml_col1, ml_col2, ml_col3, ml_col4 = st.columns(4)
        with ml_col1:
            st.markdown("**Computer Vision**")
            st.progress(0.8)
        with ml_col2:
            st.markdown("**NLP**")
            st.progress(0.75)
        with ml_col3:
            st.markdown("**Supervised Learning**")
            st.progress(0.85)
        with ml_col4:
            st.markdown("**Feature Engineering**")
            st.progress(0.8)
        
        # Tools
        st.markdown("### Tools & Platforms")
        tool_col1, tool_col2, tool_col3, tool_col4 = st.columns(4)
        with tool_col1:
            st.markdown("**VS Code**")
            st.progress(0.9)
        with tool_col2:
            st.markdown("**Jupyter Notebook**")
            st.progress(0.95)
        with tool_col3:
            st.markdown("**Excel**")
            st.progress(0.8)
        with tool_col4:
            st.markdown("**Photoshop/Canva**")
            st.progress(0.75)
    
    with col2:
        st.markdown("## Soft Skills")
        soft_skills = ["Leadership", "Teamwork", "Communication", "Management", "Problem Solving", "Critical Thinking"]
        
        for skill in soft_skills:
            st.markdown(f"- {skill}")
            
        if lottie_data:
            st_lottie(lottie_data, height=300, key="data")
        else:
            st.image("https://via.placeholder.com/300x300.png?text=Skills", width=300)

elif nav_selection == "Experience":
    st.markdown("# Experience & Responsibilities")
    
    # Timeline without streamlit-timeline dependency
    st.markdown("## Leadership & Experience Timeline")
    
    # Manual timeline display
    experiences = [
        {
            "period": "November 2023 - February 2024",
            "title": "PR Executive | Kashiyatra'24",
            "description": """
            - Collaborated with a team of 25 individuals to successfully execute the Annual Socio-Cultural Festival of IIT(BHU)
            - Organized a series of 90+ Events in a span of 3 days involving a footfall of over 60,000+ people
            - Effectively managed multiple guests and coordinated prominent pronite events
            """
        },
        {
            "period": "August 2023 - May 2024",
            "title": "Induction Mentor | SCS IMP 2023-24",
            "description": """
            - Mentored 20+ freshers of the Mining Department on academics, extracurriculars, and overall career paths
            - Ensured prompt adjustment of freshers with the college culture by in-person Interaction
            - Made opportunities more accessible to freshers
            """
        },
        {
            "period": "January 2023 - March 2023",
            "title": "PR Coordinator | Technex'23",
            "description": """
            - Operated under the guidance of seniors to manage Technex'23, the annual Techno-Management Festival of IIT(BHU) Varanasi
            - Helped coordinate marketing and promotional activities
            """
        },
        {
            "period": "May 2023 - Present",
            "title": "Core Team Member - The Photography Club IIT(BHU)",
            "description": """
            - Organized various workshops to boost club offerings and member participations
            - Contributed to the club's growth
            - Planned and managed key activities for successful events
            """
        }
    ]
    
    for exp in experiences:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"### {exp['period']}")
            with col2:
                st.markdown(f"## {exp['title']}")
                st.markdown(exp['description'])
            st.markdown("---")
    
    # Achievements
    st.markdown("## Honors & Achievements")
    achievements = [
        "🥇 First Position in Online Theme Photography, Inter IIT Cultural Meet 6.0",
        "🥈 Second Position in Online Photostory Competition, Inter IIT Cultural Meet 6.0",
    ]
    
    for achievement in achievements:
        st.markdown(f"- {achievement}")

elif nav_selection == "Education":
    st.markdown("# Education")
    
    # Education timeline
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("## Timeline")
        st.markdown("### 2022 - 2026")
        st.markdown("### 2021")
        st.markdown("### 2019")
    
    with col2:
        st.markdown("## Degrees")
        
        # B.Tech
        st.markdown("### B.Tech Mining Engineering")
        st.markdown("**IIT (BHU), Varanasi**")
        st.markdown("CGPA: 8.13")
        st.markdown("Relevant coursework: Data Structures, Algorithms, Machine Learning")
        st.markdown("---")
        
        # Class XII
        st.markdown("### CBSE Class XII")
        st.markdown("**MJRP Public School, Ghazipur, U.P.**")
        st.markdown("Percentage: 96.00%")
        st.markdown("---")
        
        # Class X
        st.markdown("### CBSE Class X")
        st.markdown("**MJRP Public School, Ghazipur, U.P.**")
        st.markdown("Percentage: 95.40%")
    
    # Visualize academic performance
    st.markdown("## Academic Performance")
    
    academic_data = {
        "Education Level": ["B.Tech", "Class XII", "Class X"],
        "Score (%)": [81.3, 96.0, 95.4]
    }
    
    df_academic = pd.DataFrame(academic_data)
    
    fig = px.bar(df_academic, x="Education Level", y="Score (%)", 
                 color="Score (%)", 
                 text="Score (%)",
                 color_continuous_scale="Viridis",
                 title="Academic Performance Over Time")
    
    fig.update_layout(xaxis_title="Education Level", 
                     yaxis_title="Score (%)",
                     yaxis_range=[70, 100])
    
    st.plotly_chart(fig, use_container_width=True)

elif nav_selection == "Contact":
    st.markdown("# Contact Me")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## Get in Touch")
        
        # Simple contact form with Streamlit components instead of HTML
        st.markdown("### Contact Form")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.button("Send Message")
        
        if submit:
            st.success("Thanks for your message! I'll get back to you soon.")
    
    with col2:
        st.markdown("## Contact Information")
        
        st.markdown("📧 **Email**")
        st.markdown("justpuneetrai@gmail.com")
        
        st.markdown("📞 **Phone**")
        st.markdown("+91 9555230429")
        
        st.markdown("🏠 **Address**")
        st.markdown("Village: Chandani, Post: Kundesar")
        st.markdown("District: Ghazipur, Uttar Pradesh - 233227")
        
        st.markdown("## Connect")
        
        social_media = {
            "LinkedIn": "https://www.linkedin.com/",
            "GitHub": "https://github.com/",
            "Twitter": "https://twitter.com/"
        }
        
        for platform, link in social_media.items():
            st.markdown(f"[{platform}]({link})")
