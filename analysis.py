import streamlit as st
import google.generativeai as genai
from pdf import read_pdf

import os
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel("gemini-1.5-flash") # Initiate Model

# Read the PDF and store it into pdf_doc.
def profile(pdf_doc, job_desc):
    if pdf_doc is not None:
        pdf = read_pdf(pdf_doc)
        st.markdown("The Resume has been Uploaded ✅️ 👍") 
    else:
        st.warning("👈 Upload your Resume")
    ats_score = model.generate_content(f"Compare the resume '{pdf}' with the job description '{job_desc}' & suggest the ATS(Applicant Tracking System) Score(in pecentage) of the resume. Just mention only the score in integer ")
    fittment = model.generate_content(f"Compare the resume '{pdf}' with the job description '{job_desc}' & mention clearly if the candidate will be a good fit for this Job role. Just in one line/scentance of maxmimum 20 tokens")
    improvement_tips = model.generate_content(f"Suggest improvements to the resume '{pdf}' to better align with the job description and mention the comments in bold  '{job_desc}'")
    resume_narrative = model.generate_content(f"Rewrite the resume '{pdf}' to highlight relevant skills and experience accordng to the job description '{job_desc}'")
        
    # Display Results
    return{#st.subheader(body = "Resume ATS Score"),
           st.write("The ATS score of the candidate is  : ",ats_score.text),
           st.write("Is candidate a good fit for the JD : ",fittment.text),
           st.subheader( " ", divider = True),
           st.subheader(body = "Suggestion for improvement in CV ", divider = True),
           st.write(improvement_tips.text),
           st.subheader(" ", divider = True),
           st.subheader("Suggested Resume :", divider = True),
           st.write(resume_narrative.text)}    
    
    
    
    
    
