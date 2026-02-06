import streamlit as st

from modules.text_extraction import extract_text
from modules.preprocessing import clean_text
from modules.risk_analysis import analyze_risk
from modules.report_generator import generate_report

st.title("Contract Analysis & Risk Assessment Bot")

uploaded_file = st.file_uploader("Upload Contract Document",
                                 type=["pdf", "docx", "txt"])

if uploaded_file:

    st.info("Processing Document...")

    text = extract_text(uploaded_file)

    clean = clean_text(text)

    level, findings = analyze_risk(clean)

    report = generate_report(clean, level, findings)

    st.subheader("Overall Risk Level")
    st.success(level)

    st.subheader("Risk Findings")

    if len(findings) == 0:
        st.write("No major risk clauses detected.")
    else:
        for f in findings:
            st.write("• " + f)

    st.subheader("Report Summary")

    st.write("**Date:**", report["date"])
    st.write("**Risk Level:**", report["risk_level"])
    st.write("**Total Findings:**", report["total_findings"])

    st.subheader("Detailed Findings")

    for item in report["details"]:
        st.write("- " + item)

    st.success("Report saved successfully ")

