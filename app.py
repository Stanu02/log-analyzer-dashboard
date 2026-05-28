import streamlit as st

st.set_page_config(page_title="Log Analyzer", layout="wide")

st.title("📊 Log Analyzer Dashboard")

uploaded_file = st.file_uploader("Upload a log file")

if uploaded_file:

    content = uploaded_file.read().decode("utf-8")

    # Counts
    error_count = content.count("ERROR")
    warning_count = content.count("WARNING")
    info_count = content.count("INFO")

    # Alerts
    if error_count > 3:
        st.error("🚨 High number of ERRORS detected!")
    elif error_count > 0:
        st.warning("⚠ Some errors found in logs")
    else:
        st.success("✅ System looks healthy")

    # Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ERRORS", error_count)

    with col2:
        st.metric("WARNINGS", warning_count)

    with col3:
        st.metric("INFO", info_count)

    # Chart
    st.subheader("Log Distribution Chart")

    st.bar_chart({
        "ERROR": [error_count],
        "WARNING": [warning_count],
        "INFO": [info_count]
    })

    # Filter logs
    st.subheader("🔍 Filter Logs")

    log_type = st.selectbox(
        "Select log type",
        ["ALL", "ERROR", "WARNING", "INFO"]
    )

    lines = content.split("\n")

    if log_type == "ALL":
        filtered_logs = lines
    else:
        filtered_logs = [line for line in lines if log_type in line]

    st.text("\n".join(filtered_logs))

    # Export report
    report = f"""
Log Analysis Report

ERRORS: {error_count}
WARNINGS: {warning_count}
INFO: {info_count}
"""

    st.download_button(
        "📥 Download Report",
        report,
        file_name="log_report.txt"
    )