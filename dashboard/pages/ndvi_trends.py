import streamlit as st

st.title(
    "NDVI Trend Analysis"
)

st.write(
    "Monitor vegetation changes over time"
)

months = [
    "Jan",
    "Mar",
    "Jun",
    "Sep"
]

ndvi_values = [
    0.42,
    0.51,
    0.68,
    0.61
]

chart_data = {
    "Month": months,
    "NDVI": ndvi_values
}

st.line_chart(
    chart_data,
    x="Month",
    y="NDVI"
)