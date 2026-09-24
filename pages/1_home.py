# ==========================================================
# SMARTCART ANALYTICS
# Home.py
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

from db_connection import load_products

st.set_page_config(
    page_title="SmartCart Analytics",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ==========================================================
# LOAD DATA FROM SQLITE DATABASE
# ==========================================================
df = load_products()
# ==========================================================
# AMAZON COLOR PALETTE
# ==========================================================

AMAZON_ORANGE = "#FF9900"
AMAZON_NAVY = "#232F3E"
AMAZON_BLUE = "#146EB4"
LIGHT_BG = "#F4F6F9"
CARD_BG = "#FFFFFF"

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* ------------------------------
Main Background
------------------------------ */

.stApp{
    background-color:#F4F6F9;
}

/* ------------------------------
Hide Streamlit Branding
------------------------------ */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* ------------------------------
Main Container
------------------------------ */

.block-container{

padding-top:2rem;
padding-left:2.5rem;
padding-right:2.5rem;
padding-bottom:2rem;

}

/* ------------------------------
Sidebar
------------------------------ */

[data-testid="stSidebar"]{

background:linear-gradient(180deg,#232F3E,#146EB4);

}

[data-testid="stSidebar"] *{

color:white;

}

/* ------------------------------
Metric Cards
------------------------------ */

div[data-testid="metric-container"]{

background:white;
padding:18px;
border-radius:18px;
border-left:8px solid #FF9900;
box-shadow:0px 8px 20px rgba(0,0,0,0.15);

}

/* Hover Effect */

div[data-testid="metric-container"]:hover{

transform:translateY(-5px);
transition:.3s;

}

/* ------------------------------
Buttons
------------------------------ */

.stButton>button{

background:#FF9900;
color:white;
border:none;
border-radius:10px;
font-weight:bold;

}

.stButton>button:hover{

background:#232F3E;
color:white;

}

/* ------------------------------
Search Box
------------------------------ */

input{

border-radius:12px !important;

}

/* ------------------------------
DataFrame
------------------------------ */

[data-testid="stDataFrame"]{

border-radius:15px;

}

/* ------------------------------
Headers
------------------------------ */

h1{

color:#232F3E;

}

h2{

color:#232F3E;

}

h3{

color:#146EB4;

}

hr{

margin-top:25px;
margin-bottom:25px;

}

</style>
""", unsafe_allow_html=True)
# ==========================================================
# AMAZON LOGO (CENTER)
# ==========================================================

logo = Image.open("images/amazon_logo.png")

left, center, right = st.columns([1, 2, 1])

with center:
    st.image(logo, width=950)
st.markdown("---")

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🛒 SmartCart Analytics")

st.sidebar.markdown("---")

st.sidebar.success("Amazon E-Commerce Product Insights Dashboard")

st.sidebar.markdown("""
### 📂 Project Information

✔ Real Amazon Dataset

✔ Dataset Source : Kaggle

✔ Cleaned using Pandas

✔ Interactive Plotly Charts

✔ Business Intelligence Dashboard

✔ Streamlit Web Application
""")

st.sidebar.markdown("---")

st.sidebar.info("""
👈 Navigate through the pages using the menu above.

Explore:

• Dataset Overview

• Product Analysis

• Price Analysis

• Rating Analysis

• Sales Insights

• Business Recommendations
""")

# ==========================================================
# DASHBOARD HEADER
# ==========================================================

st.markdown("""
# 🛒 SmartCart Analytics

### Amazon E-Commerce Product Insights Dashboard

Analyze Amazon Products using Interactive Visualizations,
Business Intelligence and Data Analytics.

""")

st.markdown("---")
# ==========================================================
# SEARCH PRODUCT
# ==========================================================

st.markdown("""
<style>

/* Search Title */
.search-title{
    background:linear-gradient(90deg,#FF9900,#FFB84D);
    padding:16px;
    border-radius:16px;
    text-align:center;
    color:white;
    font-size:28px;
    font-weight:bold;
    box-shadow:0px 8px 20px rgba(0,0,0,.18);
    margin-bottom:18px;
}

/* Dashboard Title */
.dashboard-title{
    background:linear-gradient(90deg,#232F3E,#146EB4);
    padding:18px;
    border-radius:16px;
    text-align:center;
    color:white !important;
    box-shadow:0px 8px 20px rgba(0,0,0,.20);
    margin-top:20px;
    margin-bottom:25px;
}

/* KPI Cards */
.kpi-card{
    padding:18px;
    border-radius:18px;
    color:white;
    text-align:center;
    box-shadow:0px 8px 18px rgba(0,0,0,.18);
    transition:.35s;
    margin-bottom:15px;
}

.kpi-card:hover{
    transform:translateY(-8px);
}

.kpi-value{
    font-size:34px;
    font-weight:bold;
    margin-top:8px;
}

.kpi-label{
    font-size:17px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
'<div class="search-title">🔍 Search Amazon Products</div>',
unsafe_allow_html=True
)

search = st.text_input(
    "",
    placeholder="Type Product Name Here..."
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

# ==========================================================
# KPI CALCULATIONS
# ==========================================================

total_products = len(filtered_df)

average_rating = round(
    filtered_df["rating"].mean(),
    2
)

average_price = round(
    filtered_df["current/discounted_price"].mean(),
    2
)

total_reviews = int(
    filtered_df["number_of_reviews"].sum()
)

best_sellers = (
    filtered_df["is_best_seller"]
    .fillna("No")
    .astype(str)
    .str.lower()
    .eq("yes")
    .sum()
)

# ==========================================================
# DASHBOARD OVERVIEW
# ==========================================================

st.markdown("""
<div class="dashboard-title">

<h2 style="margin:0;color:white;">
📊 Dashboard Overview
</h2>

<p style="
margin-top:8px;
font-size:18px;
color:#F5F5F5;
">

Real-Time Amazon Product Performance Dashboard

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# KPI CARDS
# ==========================================================

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    st.markdown(f"""
    <div class="kpi-card"
    style="background:linear-gradient(135deg,#FF9900,#F39C12);">

    <div style="font-size:42px;">📦</div>

    <div class="kpi-label">Products</div>

    <div class="kpi-value">{total_products:,}</div>

    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-card"
    style="background:linear-gradient(135deg,#16A085,#1ABC9C);">

    <div style="font-size:42px;">⭐</div>

    <div class="kpi-label">Average Rating</div>

    <div class="kpi-value">{average_rating}</div>

    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card"
    style="background:linear-gradient(135deg,#146EB4,#2980B9);">

    <div style="font-size:42px;">💰</div>

    <div class="kpi-label">Average Price</div>

    <div class="kpi-value">${average_price:,.2f}</div>

    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="kpi-card"
    style="background:linear-gradient(135deg,#E74C3C,#C0392B);">

    <div style="font-size:42px;">📝</div>

    <div class="kpi-label">Reviews</div>

    <div class="kpi-value">{total_reviews:,}</div>

    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown(f"""
    <div class="kpi-card"
    style="background:linear-gradient(135deg,#8E44AD,#6C3483);">

    <div style="font-size:42px;">🏆</div>

    <div class="kpi-label">Best Sellers</div>

    <div class="kpi-value">{best_sellers}</div>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# ==========================================================
# PART 2B
# ABOUT DATASET & PROJECT INFORMATION
# ==========================================================

st.markdown("""
<style>

/* Information Cards */

.info-card{

background:white;
padding:28px;
border-radius:18px;
box-shadow:0px 8px 20px rgba(0,0,0,.15);
border-top:8px solid #FF9900;
height:100%;

}

.project-card{

background:linear-gradient(180deg,#232F3E,#146EB4);
padding:28px;
border-radius:18px;
box-shadow:0px 8px 20px rgba(0,0,0,.20);
color:white;
height:100%;

}

.small-card{

background:#F8F9FA;
padding:18px;
border-radius:15px;
text-align:center;
box-shadow:0px 5px 12px rgba(0,0,0,.12);
border-left:6px solid #FF9900;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# DATASET INFORMATION
# ==========================================================

left,right = st.columns([2,1])

with left:

    st.markdown(f"""
<div class="info-card">

<h2 style="color:#232F3E;">

📖 About Dataset

</h2>

<hr>

<p style="font-size:17px; line-height:1.8;">

This dashboard analyzes a <b>real Amazon Products Dataset</b>
downloaded from <span style="color:#146EB4;"><b>Kaggle</b></span>.

The dataset was cleaned using <b>Python (Pandas)</b>
and visualized using <b>Plotly</b> inside
a <b>Streamlit Dashboard</b>.

</p>

<h3 style="color:#FF9900;">

Dataset Includes

</h3>

✅ Product Ratings

<br>

✅ Discounted Prices

<br>

✅ Customer Reviews

<br>

✅ Best Seller Status

<br>

✅ Delivery Details

<br>

✅ Sustainability Badges

<br>

✅ Product Listings

<br>

✅ Product Categories

</div>

""", unsafe_allow_html=True)

with right:

    st.markdown(f"""
<div class="project-card">

<h2 style="text-align:center;color:white;">

📌 Project Information

</h2>

<hr>

<b>Project Name</b>

<br>

SmartCart Analytics

<br><br>

<b>Dashboard</b>

<br>

Amazon Product Insights

<br><br>

<b>Dataset Source</b>

<br>

Kaggle

<br><br>

<b>Programming Language</b>

<br>

Python

<br><br>

<b>Libraries Used</b>

<br>

Pandas

<br>

Plotly

<br>

Streamlit

<br><br>

<b>IDE</b>

<br>

Visual Studio Code

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# DATASET OVERVIEW
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:15px;
border-radius:15px;
text-align:center;
margin-bottom:20px;
box-shadow:0px 5px 15px rgba(0,0,0,.20);
">

<h2 style="color:white;">

📊 Dataset Overview

</h2>

</div>
""", unsafe_allow_html=True)

row1,row2,row3,row4 = st.columns(4)

with row1:

    st.markdown(f"""
<div class="small-card">

<h3>📦</h3>

<h4>Total Products</h4>

<h2 style="color:#FF9900;">
{len(df):,}
</h2>

</div>
""", unsafe_allow_html=True)

with row2:

    st.markdown(f"""
<div class="small-card">

<h3>📑</h3>

<h4>Total Columns</h4>

<h2 style="color:#146EB4;">
{df.shape[1]}
</h2>

</div>
""", unsafe_allow_html=True)

with row3:

    st.markdown(f"""
<div class="small-card">

<h3>⭐</h3>

<h4>Average Rating</h4>

<h2 style="color:#16A085;">
{average_rating}
</h2>

</div>
""", unsafe_allow_html=True)

with row4:

    st.markdown(f"""
<div class="small-card">

<h3>📝</h3>

<h4>Total Reviews</h4>

<h2 style="color:#E74C3C;">
{total_reviews:,}
</h2>

</div>
""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART 3
# LIVE DASHBOARD PREVIEW
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(135deg,#232F3E,#146EB4);
padding:25px;
border-radius:18px;
text-align:center;
">

<h2 style="color:#FFFFFF; margin-bottom:10px;">
📊 Live Dashboard Preview
</h2>

<p style="color:#FFFFFF; font-size:17px; margin:0;">
Preview of Interactive Charts Generated from the Amazon Products Dataset
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# TWO LARGE PREVIEW CHARTS
# ==========================================================

left, right = st.columns(2)

# ==========================================================
# CHART 1
# CUSTOMER RATING DISTRIBUTION
# ==========================================================

with left:

    st.markdown("### ⭐ Customer Rating Distribution")

    fig_rating = px.histogram(

        filtered_df,

        x="rating",

        nbins=20,

        title="Distribution of Customer Ratings",

        color_discrete_sequence=["royalblue"],

        template="plotly_white"

    )

    fig_rating.update_layout(

        height=620,

        title_x=0.5,

        xaxis_title="Customer Rating",

        yaxis_title="Number of Products",

        font=dict(size=15)

    )

    st.plotly_chart(
        fig_rating,
        use_container_width=True
    )

# ==========================================================
# CHART 2
# CURRENT PRICE DISTRIBUTION
# ==========================================================

with right:

    st.markdown("### 💰 Current Price Distribution")

    fig_price = px.box(

        filtered_df,

        y="current/discounted_price",

        color_discrete_sequence=["#FF9900"]

    )

    fig_price.update_layout(

        title="Current Product Price Distribution",

        template="plotly_white",

        title_x=0.5,

        height=620,

        yaxis_title="Current Price ($)",

        font=dict(size=15)

    )

    st.plotly_chart(
        fig_price,
        use_container_width=True
    )

st.markdown("---")
# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:15px;
border-radius:15px;
box-shadow:0px 5px 15px rgba(0,0,0,0.15);
margin-bottom:20px;
">

<h2 style="
text-align:center;
color:white;
">

💡 Business Insights

</h2>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.success("""

### ⭐ Customer Rating Analysis

• Most Amazon products have ratings between **4.0 and 5.0**.

• Higher-rated products generally build stronger customer trust.

• Only a small number of products have ratings below **3.5**.

• Customer ratings indicate overall product quality and satisfaction.

""")

with col2:

    st.info("""

### 💰 Price Distribution Analysis

• Most products belong to the affordable and medium price range.

• A few premium products appear as price outliers.

• The Box Plot clearly highlights the median price and outliers.

• Pricing analysis helps businesses optimize pricing strategies.

""")

st.markdown("---")