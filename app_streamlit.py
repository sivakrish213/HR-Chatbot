import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 🔹 Step 1: Load employee data
employees = [
    {"name": "Alice Johnson", "skills": ["Python", "AWS", "Docker"], "experience_years": 5, "past_projects": ["Healthcare Dashboard", "E-commerce Platform"], "availability": "available"},
    {"name": "Bob Lee", "skills": ["React Native", "Node.js", "MongoDB"], "experience_years": 4, "past_projects": ["Chatbot System", "Social Media App"], "availability": "available"},
    {"name": "Clara Mendes", "skills": ["Machine Learning", "TensorFlow", "PyTorch"], "experience_years": 6, "past_projects": ["Medical Diagnosis Platform", "AI Stock Predictor"], "availability": "unavailable"},
    {"name": "David Kim", "skills": ["Java", "Spring Boot", "MySQL"], "experience_years": 3, "past_projects": ["Banking API", "HR Management System"], "availability": "available"},
    {"name": "Eva Shah", "skills": ["Python", "NLP", "SpaCy"], "experience_years": 5, "past_projects": ["Resume Parser", "Sentiment Analyzer"], "availability": "available"},
    {"name": "Farhan Malik", "skills": ["React Native", "Firebase", "UI/UX"], "experience_years": 2, "past_projects": ["Fitness Tracker", "E-learning App"], "availability": "unavailable"},
    {"name": "Grace Lee", "skills": ["AWS", "Kubernetes", "CI/CD"], "experience_years": 7, "past_projects": ["Cloud Migration", "DevOps Pipeline"], "availability": "available"},
    {"name": "Henry Wu", "skills": ["Terraform", "GCP", "Docker"], "experience_years": 5, "past_projects": ["Infrastructure Automation", "Healthcare Cloud"], "availability": "unavailable"},
    {"name": "Isabella Gomes", "skills": ["SQL", "Power BI", "ETL"], "experience_years": 4, "past_projects": ["Retail Analytics", "Financial Dashboard"], "availability": "available"},
    {"name": "Jackie Tran", "skills": ["C++", "Robotics", "Computer Vision"], "experience_years": 6, "past_projects": ["Autonomous Drone", "Factory Robot Controller"], "availability": "unavailable"},
    {"name": "Karan Kapoor", "skills": ["Python", "Pandas", "Scikit-learn"], "experience_years": 3, "past_projects": ["Sales Prediction", "Customer Segmentation"], "availability": "available"},
    {"name": "Lena Park", "skills": ["JavaScript", "Next.js", "TypeScript"], "experience_years": 4, "past_projects": ["Landing Page Builder", "SaaS Dashboard"], "availability": "available"},
    {"name": "Mohan Raj", "skills": ["Azure", "PowerShell", "CI/CD"], "experience_years": 5, "past_projects": ["Infrastructure-as-Code", "Log Analytics"], "availability": "unavailable"},
    {"name": "Nina D'Souza", "skills": ["Machine Learning", "Healthcare", "OpenCV"], "experience_years": 4, "past_projects": ["X-ray Scanner AI", "Health Risk Monitor"], "availability": "available"},
    {"name": "Om Prakash", "skills": ["React", "GraphQL", "Redux"], "experience_years": 3, "past_projects": ["Job Portal", "Chat App"], "availability": "available"},
    {"name": "Pooja Reddy", "skills": ["Python", "Flask", "PostgreSQL"], "experience_years": 4, "past_projects": ["Inventory Management System", "Bug Tracker"], "availability": "available"},
    {"name": "Rajiv Bansal", "skills": ["Scala", "Apache Spark", "Kafka"], "experience_years": 6, "past_projects": ["Fraud Detection", "Ad Recommender"], "availability": "unavailable"},
    {"name": "Sneha Kulkarni", "skills": ["Data Engineering", "Airflow", "BigQuery"], "experience_years": 5, "past_projects": ["Healthcare ETL", "Data Lake Setup"], "availability": "available"},
    {"name": "Tarun Verma", "skills": ["Go", "Docker", "gRPC"], "experience_years": 4, "past_projects": ["Payment Gateway", "Container Orchestration"], "availability": "unavailable"},
    {"name": "Zara Khan", "skills": ["Python", "FastAPI", "LLMs"], "experience_years": 3, "past_projects": ["RAG System", "Chatbot API"], "availability": "available"}
]


# 🔹 Step 2: Generate text embeddings for employees
model = SentenceTransformer("all-MiniLM-L6-v2")
employee_texts = [
    f"{e['name']} {e['experience_years']} years experience. Skills: {', '.join(e['skills'])}. Projects: {', '.join(e['past_projects'])}. Availability: {e['availability']}"
    for e in employees
]
employee_embeddings = model.encode(employee_texts)
index = faiss.IndexFlatL2(employee_embeddings[0].shape[0])
index.add(np.array(employee_embeddings))

# 🔹 Step 3: Streamlit UI
st.set_page_config(page_title="AI HR Chatbot", layout="centered")
st.title("🤖 AI-Powered HR Chatbot (RAG System)")

user_query = st.text_input("Ask me: e.g. 'Find Python developers with 3+ years experience'")

if user_query:
    query_vector = model.encode([user_query])
    D, I = index.search(np.array(query_vector), 5)

    st.markdown("### 🔍 Top Candidates Found:")
    for i in I[0]:
        emp = employees[i]
        st.markdown(f"""
**👤 {emp['name']}**
- 🛠️ Skills: {', '.join(emp['skills'])}
- 🧪 Experience: {emp['experience_years']} years
- 📁 Projects: {', '.join(emp['past_projects'])}
- 🔓 Availability: **{emp['availability'].capitalize()}**
---
""")
