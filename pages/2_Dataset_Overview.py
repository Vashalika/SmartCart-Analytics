# ==========================================================
# SMARTCART ANALYTICS
# DATASET OVERVIEW
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from db_connection import load_products

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Dataset Overview | SmartCart Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD DATASET
# ==========================================================

df = load_products()
# ==========================================================
# AMAZON COLOR THEME
# ==========================================================

AMAZON_ORANGE = "#FF9900"
AMAZON_NAVY   = "#232F3E"
AMAZON_BLUE   = "#146EB4"
LIGHT_BG      = "#F4F6F9"
CARD_BG       = "#FFFFFF"
TEXT_COLOR    = "#232F3E"
# ==========================================================
# PROFESSIONAL CSS
# ==========================================================

st.markdown("""
<style>

/* ---------------- Background ---------------- */

.stApp{
    background:#F4F6F9;
}

/* Hide Streamlit Menu */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* Main Container */

.block-container{
    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;
    padding-bottom:2rem;
}

/* ---------------- Sidebar ---------------- */

[data-testid="stSidebar"]{

    background:linear-gradient(180deg,#232F3E,#146EB4);
}

[data-testid="stSidebar"] *{

    color:white;
}

/* ---------------- Headers ---------------- */

h1{

    color:#232F3E;
    font-weight:700;
}

h2{

    color:#232F3E;
    font-weight:700;
}

h3{

    color:#146EB4;
}

/* ---------------- Metric Cards ---------------- */

div[data-testid="metric-container"]{

    background:white;
    border-radius:18px;
    border-left:7px solid #FF9900;
    padding:18px;

    box-shadow:0px 8px 18px rgba(0,0,0,.12);

    transition:all .35s ease;
}

div[data-testid="metric-container"]:hover{

    transform:translateY(-6px);

    box-shadow:0px 14px 28px rgba(0,0,0,.18);
}

/* Metric Label */

div[data-testid="metric-container"] label{

    color:#232F3E !important;

    font-weight:bold;

    font-size:16px;
}

/* Metric Value */

div[data-testid="metric-container"] [data-testid="stMetricValue"]{

    color:#146EB4;

    font-size:32px;

    font-weight:bold;
}

/* ---------------- DataFrame ---------------- */

div[data-testid="stDataFrame"]{

    border-radius:15px;

    overflow:hidden;

    box-shadow:0px 8px 20px rgba(0,0,0,.10);
}

/* ---------------- Buttons ---------------- */

.stButton>button{

    background:#FF9900;

    color:white;

    border:none;

    border-radius:10px;

    font-weight:bold;

    transition:.3s;
}

.stButton>button:hover{

    background:#E68A00;

    color:white;
}

/* ---------------- Search Box ---------------- */

.stTextInput input{

    border-radius:12px;

    border:2px solid #146EB4;

    padding:10px;
}

.stTextInput input:focus{

    border:2px solid #FF9900;
}

/* ---------------- Plotly Charts ---------------- */

.js-plotly-plot{

    border-radius:18px;

    background:white;

    box-shadow:0px 8px 18px rgba(0,0,0,.10);

    padding:10px;
}

</style>
""", unsafe_allow_html=True)
# ==========================================================
# PAGE HEADER
# ==========================================================
st.markdown("""
<style>
.white-text{
    color:#FFFFFF !important;
}
</style>

<div style="
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:30px;
border-radius:20px;
box-shadow:0px 10px 25px rgba(0,0,0,0.20);
margin-bottom:25px;
text-align:center;
">

<h1 class="white-text" style="
font-size:42px;
font-weight:700;
margin-bottom:15px;
">
📊 Dataset Overview
</h1>

<span class="white-text" style="
font-size:20px;
font-weight:500;
line-height:1.8;
display:block;
">
Explore, understand and summarize the cleaned Amazon Products dataset used in the SmartCart Analytics Dashboard.
</span>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

left, right = st.columns([2,1])

with left:

    st.markdown("""
<div style="
background:white;
padding:22px;
border-radius:18px;
border-left:8px solid #FF9900;
box-shadow:0px 8px 20px rgba(0,0,0,.10);
">

<h3 style="color:#232F3E;">
📂 About This Dataset
</h3>

<p style="font-size:16px;color:#444;line-height:1.8;">

This dashboard uses a cleaned Amazon Products dataset collected from
Kaggle. The dataset contains product ratings, prices, customer reviews,
delivery information, best seller status and sustainability details.

</p>

</div>
""", unsafe_allow_html=True)

with right:

    st.markdown("""
<div style="
background:linear-gradient(180deg,#FF9900,#F7B733);
padding:20px;
border-radius:18px;
box-shadow:0px 8px 20px rgba(0,0,0,.15);
">

<h3 style="color:white;text-align:center;">
📌 Dataset Source
</h3>

<p style="color:white;font-size:16px;text-align:center;line-height:1.8;">

<b>Source:</b> Kaggle

<br><br>

<b>Project:</b><br>

SmartCart Analytics

<br><br>

<b>Tools Used</b>

<br>

Python • Pandas • Plotly • Streamlit

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# ==========================================================
# PART B
# SEARCH PRODUCT
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:15px;
border-radius:15px;
margin-bottom:20px;
">

<h2 style="
color:white;
text-align:center;
margin:0;
">

🔍 Search Product

</h2>

</div>
""", unsafe_allow_html=True)

search = st.text_input(
    "",
    placeholder="Type Product Name..."
)

filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["title"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# KPI CALCULATIONS
# ==========================================================

total_products = len(filtered_df)

total_columns = filtered_df.shape[1]

average_rating = round(
    filtered_df["rating"].mean(),
    2
)

total_reviews = int(
    filtered_df["number_of_reviews"].sum()
)

# ==========================================================
# DATASET STATISTICS HEADER
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#FF9900,#F7B733);
padding:15px;
border-radius:15px;
margin-bottom:20px;
">

<h2 style="
color:white;
text-align:center;
margin:0;
">

📈 Dataset Statistics

</h2>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# KPI CARDS
# ==========================================================

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "📦 Total Products",
        f"{total_products:,}"
    )

with k2:
    st.metric(
        "📑 Total Columns",
        total_columns
    )

with k3:
    st.metric(
        "⭐ Average Rating",
        average_rating
    )

with k4:
    st.metric(
        "📝 Total Reviews",
        f"{total_reviews:,}"
    )

st.markdown("---")

# ==========================================================
# DATASET PREVIEW
# ==========================================================

st.markdown("""
<div style="
background:#FF9900;
padding:12px;
border-radius:12px;
margin-bottom:10px;
">

<h3 style="
color:white;
text-align:center;
margin:0;
">

📄 Dataset Preview

</h3>

</div>
""", unsafe_allow_html=True)

st.dataframe(
    filtered_df.head(10),
    use_container_width=True,
    height=420
)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# SHAPE & DATA TYPES
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div style="
    background:white;
    padding:20px;
    border-radius:15px;
    border-left:8px solid #146EB4;
    box-shadow:0px 6px 15px rgba(0,0,0,.12);
    ">

    <h3 style="color:#146EB4;">
    📐 Dataset Shape
    </h3>

    </div>
    """, unsafe_allow_html=True)

    st.metric("Rows", f"{filtered_df.shape[0]:,}")
    st.metric("Columns", filtered_df.shape[1])

with col2:

    st.markdown("""
    <div style="
    background:white;
    padding:20px;
    border-radius:15px;
    border-left:8px solid #FF9900;
    box-shadow:0px 6px 15px rgba(0,0,0,.12);
    ">

    <h3 style="color:#FF9900;">
    🔢 Data Types
    </h3>

    </div>
    """, unsafe_allow_html=True)

    dtype_df = pd.DataFrame({
        "Column": filtered_df.columns,
        "Data Type": filtered_df.dtypes.astype(str)
    })

    st.dataframe(
        dtype_df,
        use_container_width=True,
        height=350
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# MISSING VALUES
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#E74C3C,#C0392B);
padding:15px;
border-radius:15px;
margin-bottom:15px;
">

<h2 style="
color:white;
text-align:center;
margin:0;
">

❌ Missing Values Summary

</h2>

</div>
""", unsafe_allow_html=True)

missing = filtered_df.isnull().sum().reset_index()

missing.columns = [
    "Column",
    "Missing Values"
]

missing = missing.sort_values(
    by="Missing Values",
    ascending=False
)

fig = px.bar(

    missing,

    x="Column",

    y="Missing Values",

    color="Missing Values",

    text="Missing Values",

    height=650,

    color_continuous_scale="Reds",

    title="Missing Values by Column"

)

fig.update_layout(

    title_x=0.5,

    font_size=15,

    xaxis_title="Dataset Columns",

    yaxis_title="Missing Values",

    plot_bgcolor="white",

    paper_bgcolor="white"

)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# BUSINESS INSIGHT
# ==========================================================

st.markdown("""
<div style="
background:#FFFFFF;
padding:22px;
border-left:8px solid #16A085;
border-radius:15px;
box-shadow:0px 8px 18px rgba(0,0,0,.12);
">

<h3 style="color:#16A085;">
💡 Business Insight
</h3>

<p style="
font-size:17px;
line-height:1.9;
color:#444;
">

• The dataset contains structured information about Amazon products including ratings, reviews, prices and delivery details.

<br><br>

• Missing values are concentrated in only a few columns, indicating that most product information is complete and suitable for business analytics.

<br><br>

• The cleaned dataset is ready for further analysis such as Rating Analysis, Price Analysis, Customer Review Analysis and Product Performance Dashboard.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART D
# SUMMARY STATISTICS
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:18px;
border-radius:15px;
margin-bottom:20px;
">

<h2 style="
color:white;
text-align:center;
margin:0;
">

📊 Summary Statistics

</h2>

</div>
""", unsafe_allow_html=True)

st.dataframe(
    filtered_df.describe(include="all"),
    use_container_width=True,
    height=450
)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# DOWNLOAD DATASET
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#FF9900,#F7B733);
padding:15px;
border-radius:15px;
margin-bottom:20px;
">

<h2 style="
color:white;
text-align:center;
margin:0;
">

📥 Download Cleaned Dataset

</h2>

</div>
""", unsafe_allow_html=True)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Amazon Cleaned Dataset",
    data=csv,
    file_name="amazon_products_sales_data_cleaned.csv",
    mime="text/csv",
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# DATASET INFORMATION
# ==========================================================

left, right = st.columns(2)

with left:

    st.markdown("""
<div style="
background:white;
padding:22px;
border-radius:15px;
border-left:8px solid #146EB4;
box-shadow:0px 8px 18px rgba(0,0,0,.12);
">

<h3 style="color:#146EB4;">
📂 Dataset Information
</h3>

<ul style="font-size:16px; line-height:2; color:#444;">
<li><b>Dataset :</b> Amazon Products Sales Dataset</li>
<li><b>Source :</b> Kaggle</li>
<li><b>Rows :</b> 42,675</li>
<li><b>Columns :</b> 16</li>
<li><b>Domain :</b> E-Commerce</li>
<li><b>Type :</b> Cleaned Dataset</li>
</ul>

</div>
""", unsafe_allow_html=True)

with right:

    st.markdown("""
<div style="
background:white;
padding:22px;
border-radius:15px;
border-left:8px solid #FF9900;
box-shadow:0px 8px 18px rgba(0,0,0,.12);
">

<h3 style="color:#FF9900;">
🛠 Technologies Used
</h3>

<ul style="font-size:16px; line-height:2; color:#444;">
<li>🐍 Python</li>
<li>🐼 Pandas</li>
<li>📊 Plotly Express</li>
<li>📈 Plotly Graph Objects</li>
<li>🎨 Streamlit</li>
<li>💻 VS Code</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# BUSINESS SUMMARY
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#16A085,#1ABC9C);
padding:22px;
border-radius:18px;
box-shadow:0px 8px 20px rgba(0,0,0,.15);
">

<h2 style="
color:white;
text-align:center;
">

🏆 Dataset Summary

</h2>

<p style="
color:white;
font-size:18px;
line-height:2;
text-align:justify;
">

The cleaned Amazon Products dataset provides comprehensive information
about product pricing, ratings, customer reviews, delivery details,
best seller status and sustainability features.

The dataset has been cleaned and prepared using Python and Pandas,
making it suitable for interactive dashboards, business intelligence,
exploratory data analysis and data visualization.

This dataset forms the foundation of the SmartCart Analytics Dashboard
and supports meaningful business insights through interactive Plotly
visualizations.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("""
<hr>

<div style="text-align:center;">

<h4 style="color:#232F3E;">

SmartCart Analytics

</h4>

<p style="color:gray;">

Developed using Python • Pandas • Plotly • Streamlit

</p>

<p style="color:#146EB4;">

Amazon Products Sales Dataset • Kaggle

</p>

</div>
""", unsafe_allow_html=True)