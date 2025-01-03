import streamlit as st
from cv_evaluator import profile

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")


# Lets setup streamlit front end and read the pdf document

st.header(" CV Assistant for Recruiters & Applicants ", divider = "blue")
st.subheader(" ")
# notes = f'''
# st.write(notes)

st.subheader(body="Upload your Resume ( in PDF form )")
pdf_doc = st.file_uploader("Please upload the Resume in pdf format here : ",type =['pdf'])

st.subheader("Enter the Job Description 📋", divider = True)
job_desc= st.text_area(label = " Copy-Paste the Job Description Below ", max_chars=10000)

submit = st.button(label="Invoke CV Assistent")
if submit:
    st.markdown(profile(pdf_doc=pdf_doc, job_desc=job_desc))
