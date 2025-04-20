import streamlit as st
from resume_parser import extract_text
from match_score import calculate_similarity, extract_top_keywords
from report_generator import generate_pdf_report

st.set_page_config(page_title="AI Resume Scanner", layout="centered")

st.title("📄 AI Resume Scanner")
st.markdown("Upload your resume and paste a job description to see how well you match.")

# Upload Resume
resume_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=['pdf', 'docx'])

# Job Description Text Area
job_description = st.text_area("Paste Job Description Here", height=200)

# On click
if st.button("Scan Resume"):
    if resume_file and job_description:
        # Extract resume text
        resume_text = extract_text(resume_file)

        # Calculate similarity
        match_score = calculate_similarity(resume_text, job_description)
        top_keywords = extract_top_keywords(job_description, top_n=10)

        # Output
        st.subheader("📊 Match Results")
        st.write(f"**Match Score:** {match_score} %")

        st.subheader("🔑 Top Keywords in Job Description")
        st.write(", ".join(top_keywords))

        st.subheader("📄 Extracted Resume Text (for reference)")

    with st.spinner("Generating PDF Report..."):
        report_file = generate_pdf_report("User", match_score, top_keywords)
        with open(report_file, "rb") as f:
            st.download_button(
                label="📥 Download Report as PDF",
                data=f,
                file_name=report_file,
                mime="application/pdf"
            )


