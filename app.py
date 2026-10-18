import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

st.set_page_config(page_title="Reporting Dashboard", page_icon="📊", layout="wide")

# DEMO LOGIN ONLY: replace with a proper authentication system before using sensitive data.
st.sidebar.title("📊 ReportHub")
st.sidebar.caption("Starter dashboard")
st.sidebar.info("Demo login: admin / ChangeMe123!")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if st.sidebar.button("Sign in"):
    st.session_state.authenticated = username == "admin" and password == "ChangeMe123!"
if not st.session_state.authenticated:
    st.title("📊 Reporting Dashboard")
    st.warning("Sign in with the demo credentials shown in the sidebar.")
    st.markdown("This is a starter template. Do not upload confidential or customer-identifiable data.")
    st.stop()

st.title("📊 Reporting Dashboard")
st.write("Upload an Excel or CSV report to explore its data, search records, and create charts.")
uploaded = st.file_uploader("Upload Excel or CSV", type=["csv", "xlsx", "xls"])
if uploaded:
    try:
        if uploaded.name.lower().endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            df = pd.read_excel(uploaded)
    except Exception as exc:
        st.error(f"Could not read this file: {exc}")
        st.stop()
else:
    df = pd.DataFrame({
        "Agent": ["Agent A", "Agent B", "Agent C", "Agent A", "Agent B"],
        "Disposition": ["Resolved", "Follow-up", "Resolved", "Transfer", "Resolved"],
        "Repeat Call": ["No", "Yes", "No", "Yes", "No"],
        "Call Count": [24, 18, 31, 12, 27]
    })
    st.info("Showing sample data. Upload a file to replace it.")

if df.empty:
    st.warning("The uploaded file contains no rows.")
    st.stop()

st.subheader("Overview")
c1, c2, c3 = st.columns(3)
c1.metric("Rows", f"{len(df):,}")
c2.metric("Columns", f"{len(df.columns):,}")
c3.metric("Missing cells", f"{int(df.isna().sum().sum()):,}")

st.subheader("Search records")
search = st.text_input("Search across all columns")
filtered = df
if search.strip():
    mask = df.astype(str).apply(lambda col: col.str.contains(search, case=False, na=False))
    filtered = df[mask.any(axis=1)]
st.caption(f"Showing {len(filtered):,} of {len(df):,} rows")
st.dataframe(filtered, use_container_width=True, hide_index=True)

st.subheader("Create a chart")
columns = list(df.columns)
left, right = st.columns(2)
with left:
    chart_type = st.selectbox("Chart type", ["Bar chart", "Line chart", "Pie chart", "Scatter plot"])
    x_col = st.selectbox("Category / X-axis", columns, index=0)
with right:
    numeric_cols = list(df.select_dtypes(include="number").columns)
    y_options = ["(count rows)"] + numeric_cols
    y_col = st.selectbox("Value / Y-axis", y_options, index=1 if numeric_cols else 0)
if chart_type == "Pie chart":
    counts = df[x_col].fillna("(blank)").astype(str).value_counts().rename_axis(x_col).reset_index(name="Count")
    fig = px.pie(counts, names=x_col, values="Count", title=f"Distribution by {x_col}")
elif y_col == "(count rows)":
    counts = df[x_col].fillna("(blank)").astype(str).value_counts().rename_axis(x_col).reset_index(name="Count")
    fig = px.line(counts, x=x_col, y="Count", title=f"Record count by {x_col}") if chart_type == "Line chart" else px.bar(counts, x=x_col, y="Count", title=f"Record count by {x_col}")
else:
    if chart_type == "Line chart":
        fig = px.line(df, x=x_col, y=y_col, title=f"{y_col} by {x_col}")
    elif chart_type == "Scatter plot":
        fig = px.scatter(df, x=x_col, y=y_col, title=f"{y_col} by {x_col}")
    else:
        grouped = df.groupby(x_col, dropna=False)[y_col].sum().reset_index()
        fig = px.bar(grouped, x=x_col, y=y_col, title=f"{y_col} by {x_col}")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Download filtered data")
out = filtered.to_csv(index=False).encode("utf-8-sig")
st.download_button("Download filtered CSV", out, "filtered_report.csv", "text/csv")

st.divider()
st.subheader("Contact")
st.write("For questions, contact the dashboard administrator.")
st.link_button("Contact by WhatsApp", "https://wa.me/94770000000")
st.caption("Replace the example WhatsApp number with your own number in international format.")
