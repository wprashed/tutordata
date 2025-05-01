import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSV file
df = pd.read_csv("plugin_support_data.csv")
df["Thread Title"] = df["Thread Title"].fillna("").astype(str)

# Define categories
categories = {
    "Akismet Issues": ["akismet", "spam", "comment", "registration", "captcha", "contact form", "redirect", "block", "error", "fatal", "api", "false positive", "recheck", "bypass", "plugin"],
    "PHP/Version Compatibility": ["php", "version", "fatal error", "upgrade", "compatibility", "mysql"],
    "Plugin Compatibility": ["plugin", "theme", "wordpress", "conflict", "contact form", "woocommerce", "gravity form", "piotnet forms"],
    "Spam Detection & Filtering": ["spam", "comments", "queue", "misdiagnosis", "filter", "false positive", "block", "learnpress", "site", "queue"],
    "User Access & Registration": ["user", "registration", "login", "access", "email", "password", "account"],
    "Error Handling & Debugging": ["error", "debug", "warning", "problem", "issue", "fatal", "exception", "bug", "crash", "missing", "not working"],
    "API & Server Issues": ["api", "server", "offline", "connection", "request", "error code", "response", "status"],
    "Performance & Speed": ["performance", "load", "speed", "response time", "optimization"],
    "Translation & Localization": ["translation", "text domain", "language", "locale", "localization"],
    "Feature Requests & Suggestions": ["feature", "suggestion", "improvement", "request", "change", "enhancement"],
    "Security & Protection": ["security", "protection", "xml-rpc", "honeypot", "bypass", "validation", "vulnerability"],
    "Others": []  # To capture everything that doesn't fit into the above categories
}

# Classify threads
def classify_title(title):
    title_lower = title.lower()
    for category, keywords in categories.items():
        if category == "Others":
            continue
        for keyword in keywords:
            if keyword in title_lower:
                return category
    return "Others"

df["Issue Category"] = df["Thread Title"].apply(classify_title)

# Reorder to have Others last
category_order = list(categories.keys())
category_counts = df["Issue Category"].value_counts().reindex(category_order, fill_value=0)

# Color mapping
category_colors = {
    "Akismet Issues": "#FF5733",
    "PHP/Version Compatibility": "#33FF57",
    "Plugin Compatibility": "#3357FF",
    "Spam Detection & Filtering": "#FF33A1",
    "User Access & Registration": "#A133FF",
    "Error Handling & Debugging": "#33FFF7",
    "API & Server Issues": "#F7FF33",
    "Performance & Speed": "#FF8C33",
    "Translation & Localization": "#8C33FF",
    "Feature Requests & Suggestions": "#33FF91",
    "Security & Protection": "#FF3333",
    "Others": "#57FF33"
}

# Bar chart
bar_fig = px.bar(
    x=category_counts.index,
    y=category_counts.values,
    labels={"y": "Issue Category", "x": "Number of Threads"},
    title="Issue Categorization",
    color=category_counts.index,
    color_discrete_map=category_colors
)
bar_fig.update_layout(xaxis_tickangle=-30, template="plotly_dark")

# Pie chart
pie_fig = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    title="Distribution of Issues",
    color=category_counts.index,
    color_discrete_map=category_colors
)
pie_fig.update_layout(template="plotly_dark")

# Streamlit app layout
st.set_page_config(page_title="WP Plugin Issues Tracker", layout="wide")
st.title("WP Plugin Issues Tracker")

# Initialize session state for pagination
if "page" not in st.session_state:
    st.session_state.page = 1

# Display bar chart
col1, col2 = st.columns([2, 1])

with col1:
    st.plotly_chart(bar_fig, use_container_width=True)

with col2:
    st.plotly_chart(pie_fig, use_container_width=True)

# Dropdown for category selection beside the pie chart
with col2:
    st.markdown("#### 🔎 Filter & View Threads by Category")
    selected_category = st.selectbox("", category_order)

# Pagination setup
rows_per_page = 10
max_page = (len(df) // rows_per_page) + 1
current_page = st.session_state.page

# Filter data based on category
filtered_df = df[df["Issue Category"] == selected_category]

# Calculate page-specific data
start_idx = (current_page - 1) * rows_per_page
end_idx = min(start_idx + rows_per_page, len(filtered_df))
threads_on_page = filtered_df.iloc[start_idx:end_idx]["Thread Title"]

# Display threads
st.write(f"**Threads in '{selected_category}' (Page {current_page})**")

for thread in threads_on_page:
    st.markdown(f"- {thread}")

# Pagination buttons (simple)
col1, col2, col3 = st.columns(3)
with col1:
    if current_page > 1:
        if st.button("Previous Page"):
            st.session_state.page -= 1
with col2:
    st.write(f"Page {current_page}")
with col3:
    if current_page < max_page:
        if st.button("Next Page"):
            st.session_state.page += 1

if __name__ == "__main__":
    st.write("WP Plugin Issues Tracker")