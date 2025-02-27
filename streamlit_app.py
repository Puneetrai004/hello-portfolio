import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Puneet Kumar Rai's Data Science Portfolio",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
def add_custom_css():
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem !important;
        font-weight: 600;
    }
    .subheader {
        font-size: 1.5rem !important;
    }
    .project-card {
        border-radius: 5px;
        padding: 20px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

add_custom_css()

# Header section
col1, col2 = st.columns([1, 2])

with col1:
    # Replace with your own image - using a placeholder for now
    st.image("/api/placeholder/400/400", width=230)

with col2:
    st.markdown('<p class="main-header">Puneet Kumar Rai</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Data Scientist | Machine Learning Engineer | IIT (BHU) Student</p>', unsafe_allow_html=True)
    
    # Add contact links
    cols = st.columns(4)
    with cols[0]:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/puneet-rai)")
    with cols[1]:
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/puneetrai)")
    with cols[2]:
        st.markdown("[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:justpuneetrai@gmail.com)")
    with cols[3]:
        st.markdown("[![Phone](https://img.shields.io/badge/Phone-4285F4?style=for-the-badge&logo=google-voice&logoColor=white)](tel:+919555230429)")

# About Me section
st.markdown("## About Me")
st.write("""
I'm a B.Tech Mining Engineering student at IIT (BHU), Varanasi, graduating in 2026. I'm passionate about applying 
machine learning and data science to solve real-world problems. My areas of interest include Computer Vision, 
Natural Language Processing, and Predictive Analytics.

Throughout my academic journey, I've developed strong technical foundations in Python, data analysis, and 
machine learning. I'm currently seeking opportunities to apply my skills and gain industry experience in 
data science projects.
""")

# Education section
st.markdown("## Education")
st.markdown("""
### B.Tech Mining Engineering
**Indian Institute of Technology (BHU), Varanasi | 2022-2026**
- CGPA: 8.13/10

### CBSE Class XII
**MJRP Public School, Ghazipur, U.P. | 2021**
- Percentage: 96.00%

### CBSE Class X
**MJRP Public School, Ghazipur, U.P. | 2019**
- Percentage: 95.40%
""")

# Skills section
st.markdown("## Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Programming")
    st.markdown("- Python\n- C++\n- C\n- MySQL")

with col2:
    st.markdown("### Data Science & ML")
    st.markdown("- Pandas & NumPy\n- Scikit-learn\n- Computer Vision\n- Natural Language Processing")

with col3:
    st.markdown("### Tools & Technologies")
    st.markdown("- Jupyter Notebook\n- VS Code\n- Excel\n- Matplotlib & Seaborn")

# Projects section
st.markdown("## Featured Projects")

# Project 1 - Mineral Classification
with st.container():
    st.markdown("""
    <div class="project-card" style="background-color: #f5f5f5;">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("/api/placeholder/400/300", use_column_width=True)
    
    with col2:
        st.markdown("### Mineral Classification using Machine Learning")
        st.markdown("**Technologies:** Python, OpenCV, CNN, EfficientNet")
        st.markdown("""
        Researched and implemented image segmentation, classification, and object detection techniques to create a 
        robust machine learning model for mineral classification. Using the CNN EfficientNet architecture, the model 
        achieved an impressive 94% accuracy in correctly identifying various mineral types.
        
        This project was conducted under the supervision of Dr. Amarendra Kumar and demonstrates practical applications 
        of computer vision techniques in the mining industry.
        """)
        
        demo_col, code_col = st.columns(2)
        with demo_col:
            st.button("Live Demo", key="demo1", on_click=lambda: st.session_state.update({"page": "mineral_classification"}))
        with code_col:
            st.markdown("[GitHub Code](https://github.com/puneetrai/mineral-classification)")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Project 2 - Twitter Sentiment Analysis
with st.container():
    st.markdown("""
    <div class="project-card" style="background-color: #f5f5f5;">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("/api/placeholder/400/300", use_column_width=True)
    
    with col2:
        st.markdown("### Twitter Sentiment Analysis")
        st.markdown("**Technologies:** Python, NLP, Machine Learning, TF-IDF")
        st.markdown("""
        Preprocessed tweets through multiple techniques including stemming, lemmatization, and feature extraction
        using Bag-of-Words and TF-IDF methods. The sentiment classification model achieved an F1-score of 0.55.
        
        Developed and evaluated multiple classification models using diverse text representations, optimizing 
        accuracy through advanced preprocessing techniques to effectively analyze social media sentiment.
        """)
        
        demo_col, code_col = st.columns(2)
        with demo_col:
            st.button("Live Demo", key="demo2", on_click=lambda: st.session_state.update({"page": "twitter_sentiment"}))
        with code_col:
            st.markdown("[GitHub Code](https://github.com/puneetrai/twitter-sentiment)")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Project 3 - Employee Performance 
with st.container():
    st.markdown("""
    <div class="project-card" style="background-color: #f5f5f5;">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("/api/placeholder/400/300", use_column_width=True)
    
    with col2:
        st.markdown("### Predicting Employee Performance Index")
        st.markdown("**Technologies:** Python, Feature Engineering, Random Forest, GridSearchCV")
        st.markdown("""
        Conducted detailed exploratory data analysis, applied label encoding, and standardized features to prepare 
        the dataset for modeling. Identified key performance predictors through comprehensive correlation analysis.
        
        Trained and evaluated multiple predictive models including Logistic Regression, Random Forest, SVM, and XGBoost. 
        Through hyperparameter tuning with GridSearchCV, achieved 93% accuracy with the Random Forest classifier.
        """)
        
        demo_col, code_col = st.columns(2)
        with demo_col:
            st.button("Live Demo", key="demo3", on_click=lambda: st.session_state.update({"page": "employee_performance"}))
        with code_col:
            st.markdown("[GitHub Code](https://github.com/puneetrai/employee-performance)")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Experience/Positions section
st.markdown("## Leadership Experience")
st.markdown("""
### PR Executive | Kashiyatra'24
**Nov 2023 - Feb 2024**

- Collaborated with a team of 25 individuals to successfully execute the Annual Socio-Cultural Festival of IIT(BHU)
- Organized 90+ events over a 3-day period with a footfall exceeding 60,000 people
- Managed VIP guests and coordinated prominent "pronite" events

### Induction Mentor | SCS IMP 2023-24
**Aug 2023 - May 2024**

- Mentored 20+ freshers in the Mining Department, providing guidance on academics, extracurriculars, and career paths
- Facilitated smooth adjustment to college culture through personal interactions
- Made campus opportunities more accessible to new students

### PR Coordinator | Technex'23
**Jan 2023 - Mar 2023**

- Assisted in managing Technex'23, the annual Techno-Management Festival of IIT(BHU) Varanasi
- Worked under senior guidance to ensure successful execution of the event
""")

# Achievements section
st.markdown("## Honors and Achievements")
st.markdown("""
- First Position in Online Theme Photography, Inter IIT Cultural Meet 6.0
- Second Position in Online Photostory Competition, Inter IIT Cultural Meet 6.0
- Core Team Member of The Photography Club IIT(BHU) (May 2023 - Present)
  - Organized workshops to boost club participation
  - Contributed to club growth through strategic planning
  - Managed key activities for successful events
""")

# Footer
st.markdown("---")
st.markdown("""
<p style="text-align: center;">© 2025 Puneet Kumar Rai - Built with Streamlit</p>
""", unsafe_allow_html=True)

# Navigation logic
if "page" in st.session_state:
    if st.session_state.page == "mineral_classification":
        # Import and run Mineral Classification Project
        import apps.mineral_classification
        apps.mineral_classification.app()
    elif st.session_state.page == "twitter_sentiment":
        # Import and run Twitter Sentiment Project
        import apps.twitter_sentiment
        apps.twitter_sentiment.app()
    elif st.session_state.page == "employee_performance":
        # Import and run Employee Performance Project
        import apps.employee_performance
        apps.employee_performance.app()
