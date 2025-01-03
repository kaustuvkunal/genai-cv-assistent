import streamlit as st
import google.generativeai as genai
from pdf_reader import read_pdf
import os

# Configure the Generative AI model
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(prompt):
    """Generate content using the Generative AI model."""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"

def profile(pdf_doc, job_desc, user_type):
    try:
        if not pdf_doc or not job_desc.strip():
            raise ValueError("Missing resume or job description.")
        
        pdf = read_pdf(pdf_doc)
        st.markdown("Resume Upload Finished!")
        
        ats_score = generate_response(
            f"Compare the resume '{pdf}' with the job description '{job_desc}' and & suggest the ATS(Applicant Tracking System) Score(in pecentage) of the resume. Just mention only the score in integer. Nothing else"
        )
        fittment = generate_response(
            f"Assess if the candidate is a good fit for the job role based on the resume '{pdf}' and job description '{job_desc}'. mention clearly if the candidate will be a good fit for this Job role(Yes/NO).Followed by justification in Just one line/scentance of maxmimum 15 tokens."
        )
        
        # Results for Applicants
        if user_type == "Applicant":
            improvement_tips = generate_response(
                f"Suggest improvements to the resume '{pdf}' to better align with the job description '{job_desc}'. Provide comments in bullet points. Total not more than 300 words"
            )
            resume_narrative = generate_response(
                f"Rewrite the resume '{pdf}' to highlight relevant skills and experience accordng to the job description'{job_desc}'.Total not more than 500 tokens"
            )
            return f"""
            ### ATS Score: {ats_score}
            **Fit for the Role:** {fittment}
            
            ---
            ### Suggestions for Improvement
            {improvement_tips}
            
            ---
            ### Suggested Resume
            {resume_narrative}
            """
        
        # Results for Recruiters
        elif user_type == "Recruiter":
            return f"""
            ### ATS Score: {ats_score}
            **Fit for the Role:** {fittment}
            """
        
        else:
            raise ValueError("Invalid user type selected.")
    
    except ValueError as ve:
        st.warning(str(ve))
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
