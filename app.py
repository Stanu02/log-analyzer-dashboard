import streamlit as st

st.title("Log Analyzer Dashboard")

uploaded_file = st.file_uploader("Upload a log file")

if uploaded_file:

    content = uploaded_file.read().decode("utf-8")

    error_count = content.count("ERROR")
    warning_count = content.count("WARNING")
    info_count = content.count("INFO")

    st.write(f"ERROR count: {error_count}")
    st.write(f"WARNING count: {warning_count}")
    st.write(f"INFO count: {info_count}")