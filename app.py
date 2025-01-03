import streamlit as st
from cv_evaluator import profile
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

# Streamlit setup
st.header("CV Assistant for Recruiters & Applicants", divider="blue")

# User Type Selection
user_type = st.radio(
    "Are you a Recruiter or an Applicant?",
    options=["Recruiter", "Applicant"]
)

st.subheader("Upload your Resume (in PDF form)")
pdf_doc = st.file_uploader("Upload Resume in PDF format:", type=['pdf'])

st.subheader("Enter the Job Description 📋", divider=True)
job_desc = st.text_area("Copy-Paste the Job Description Below", max_chars=10000)

if st.button("Invoke CV Assistant"):
    try:
        if not pdf_doc:
            st.error("Please upload a resume.")
        elif not job_desc.strip():
            st.error("Please enter the job description.")
        else:
            # Call profile function with user_type
            result = profile(pdf_doc=pdf_doc, job_desc=job_desc, user_type=user_type)
            st.markdown(result)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
