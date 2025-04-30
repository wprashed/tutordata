import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSV file
df = pd.read_csv("tutor_plugin_support_data.csv")
df["Thread Title"] = df["Thread Title"].fillna("").astype(str)

# Define categories
categories = {
    "Course Issues": ["course", "lesson", "content", "add course"],
    "Checkout Problems": ["checkout", "payment", "cart", "pay"],
    "Login/User Access": ["login", "register", "access", "account"],
    "Quiz/Assignment Issues": ["quiz", "question", "assignment", "grade"],
    "Error/Bug Reports": ["error", "bug", "problem", "crash", "not working"],
    "Plugin Related": ["plugin", "wordpress", "shortcode", "theme compatibility"],
    "Video/Audio Issues": ["video", "audio", "playback", "streaming"],
    "Mobile/Tablet Support": ["mobile", "tablet", "ios", "android"],
    "Others": []
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
    "Course Issues": "#1f77b4",
    "Checkout Problems": "#2ca02c",
    "Login/User Access": "#17becf",
    "Quiz/Assignment Issues": "#ff7f0e",
    "Error/Bug Reports": "#d62728",
    "Plugin Related": "#8c564b",
    "Video/Audio Issues": "#e377c2",
    "Mobile/Tablet Support": "#7f7f7f",
    "Others": "#777777"
}

# Bar chart
bar_fig = px.bar(
    x=category_counts.index,
    y=category_counts.values,
    labels={"x": "Issue Category", "y": "Number of Threads"},
    title="Issue Categorization",
    color=category_counts.index,
    color_discrete_map=category_colors
)
bar_fig.update_layout(xaxis_tickangle=-45, template="plotly_dark")

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
st.set_page_config(page_title="Issue Dashboard for Tutor LMS", layout="wide")
st.title("Issue Dashboard for Tutor LMS")

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
    st.write("Issue Dashboard for Tutor LMS")