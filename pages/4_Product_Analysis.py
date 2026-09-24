# ==========================================================
# 📦 PRODUCT ANALYSIS DASHBOARD
# PART A
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Product Analysis",
    page_icon="📦",
    layout="wide"
)

# ==========================================================
# LOAD DATASET
# ==========================================================

from db_connection import load_products

df = load_products()
# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""

<style>

.main{
    background:#F4F7FC;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Header */

.header-box{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:25px;

border-radius:18px;

text-align:center;

color:white;

box-shadow:0px 10px 25px rgba(0,0,0,.20);

margin-bottom:25px;

}

/* KPI Cards */

.metric-card{

background:white;

padding:22px;

border-radius:16px;

box-shadow:0px 8px 18px rgba(0,0,0,.12);

border-left:8px solid #FF9900;

text-align:center;

}

.metric-title{

font-size:18px;

color:#555;

font-weight:bold;

}

.metric-value{

font-size:34px;

font-weight:bold;

color:#146EB4;

}

/* Overview Box */

.info-box{

background:white;

padding:22px;

border-radius:16px;

box-shadow:0px 6px 18px rgba(0,0,0,.12);

margin-top:25px;

margin-bottom:25px;

border-left:8px solid #146EB4;

}

.info-box h3{

color:#232F3E;

}

.info-box p{

font-size:17px;

text-align:justify;

line-height:1.8;

}

</style>

""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="header-box">

<h1>

📦 Amazon Product Analysis Dashboard

</h1>

<h4>

SmartCart Analytics

</h4>

<p>

Analyze Amazon products using interactive visualizations,
customer ratings, purchasing trends,
best seller performance and sustainability insights.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.header("🎛 Dashboard Filters")

rating = st.sidebar.slider(
    "⭐ Minimum Rating",
    0.0,
    5.0,
    4.0,
    0.1
)

bestseller = st.sidebar.selectbox(
    "🏆 Best Seller Status",
    ["All","Yes","No"]
)

filtered_df = df[df["rating"] >= rating]

if bestseller != "All":
    filtered_df = filtered_df[
        filtered_df["is_best_seller"] == bestseller
    ]

# ==========================================================
# KPI CALCULATIONS
# ==========================================================

total_products = len(filtered_df)

average_rating = round(
    filtered_df["rating"].mean(),
    2
)

total_reviews = int(
    filtered_df["number_of_reviews"].sum()
)

# ==========================================================
# KPI CARDS
# ==========================================================

col1,col2,col3 = st.columns(3)

with col1:

    st.markdown(f"""

    <div class="metric-card">

    <div class="metric-title">

    📦 Total Products

    </div>

    <div class="metric-value">

    {total_products:,}

    </div>

    </div>

    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""

    <div class="metric-card">

    <div class="metric-title">

    ⭐ Average Rating

    </div>

    <div class="metric-value">

    {average_rating}

    </div>

    </div>

    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""

    <div class="metric-card">

    <div class="metric-title">

    📝 Total Reviews

    </div>

    <div class="metric-value">

    {total_reviews:,}

    </div>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# PAGE INTRODUCTION
# ==========================================================

st.markdown("""

<div class="info-box">

<h3>

📖 Product Analysis Overview

</h3>

<p>

This page provides a comprehensive analysis of Amazon products
using interactive visualizations from the SmartCart Analytics project.
The analysis focuses on customer ratings, product popularity,
best seller performance, sustainability badges,
and purchasing behaviour.

Use the filters available in the sidebar to dynamically
explore different product groups and gain meaningful
business insights.

</p>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# ⭐ PART B : CUSTOMER RATING DISTRIBUTION
# ==========================================================

st.markdown("""
<style>

.section-header{

background:linear-gradient(90deg,#FF9900,#232F3E);

padding:18px;

border-radius:15px;

text-align:center;

color:white;

margin-top:20px;

margin-bottom:20px;

box-shadow:0px 8px 18px rgba(0,0,0,.20);

}

.info-card{

background:white;

padding:22px;

border-radius:15px;

box-shadow:0px 6px 16px rgba(0,0,0,.12);

border-left:7px solid #FF9900;

margin-top:20px;

margin-bottom:20px;

}

.info-card h4{

color:#232F3E;

}

.info-card p{

font-size:16px;

line-height:1.8;

text-align:justify;

}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------

st.markdown("""

<div class="section-header">

<h2>⭐ Customer Rating Distribution</h2>

<p>
Explore how customer ratings are distributed across Amazon products.
</p>

</div>

""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Plotly Histogram (Same as Notebook)
# ----------------------------------------------------------

fig = px.histogram(

    filtered_df,

    x="rating",

    nbins=20,

    title="⭐ Distribution of Customer Ratings",

    color_discrete_sequence=["royalblue"],

    template="plotly_white"

)

fig.update_layout(

    title_x=0.5,

    width=1200,

    height=700,

    xaxis_title="Customer Rating",

    yaxis_title="Number of Products",

    font=dict(size=16)

)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------------
# Graph Overview
# ----------------------------------------------------------

st.markdown("""

<div class="info-card">

<h4>📊 Graph Overview</h4>

<p>

This histogram displays the distribution of customer ratings across
Amazon products.

Each bar represents the number of products that fall within a
particular rating range.

A higher bar indicates that more products received ratings in that
range.

</p>

</div>

""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Business Insights
# ----------------------------------------------------------

st.markdown("""

<div class="info-card">

<h4>💡 Business Insights</h4>

<ul>

<li>⭐ Most Amazon products have ratings between <b>4.0 and 5.0</b>, indicating strong customer satisfaction.</li>

<li>📈 Products with higher ratings are more likely to gain customer trust and improve sales.</li>

<li>📦 Only a small number of products have ratings below <b>3.5</b>, showing that lower-rated products are relatively uncommon.</li>

<li>🛍️ Businesses should prioritize maintaining product quality to achieve consistently high customer ratings.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# 🏆 PART C : BEST SELLER STATUS ANALYSIS
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#232F3E,#FF9900);
padding:18px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0px 8px 18px rgba(0,0,0,.20);
margin-top:25px;
margin-bottom:20px;">

<h2>🏆 Best Seller Status Analysis</h2>

<p>
Analyze the distribution of Best Seller and Non-Best Seller
products available on Amazon.
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Count Best Seller Products
# ----------------------------------------------------------

best_seller = (
    filtered_df["is_best_seller"]
    .value_counts()
    .reset_index()
)

best_seller.columns = [
    "Best Seller Status",
    "Number of Products"
]

# ----------------------------------------------------------
# Interactive Plotly Bar Chart
# ----------------------------------------------------------

fig = px.bar(

    best_seller,

    x="Best Seller Status",

    y="Number of Products",

    color="Best Seller Status",

    text="Number of Products",

    template="plotly_white",

    color_discrete_sequence=[
        "#FF9900",
        "#146EB4"
    ]

)

fig.update_layout(

    title=dict(

        text="🏆 Distribution of Best Seller Products",

        x=0.5,

        font=dict(size=24)

    ),

    width=1200,

    height=700,

    xaxis_title="Best Seller Status",

    yaxis_title="Number of Products",

    showlegend=False,

    font=dict(size=16)

)

fig.update_traces(

    textposition="outside",

    textfont_size=16

)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------------
# Graph Overview
# ----------------------------------------------------------

st.markdown("""
<div style="
background:white;
padding:20px;
border-radius:15px;
border-left:7px solid #FF9900;
box-shadow:0px 6px 16px rgba(0,0,0,.12);
margin-top:20px;">

<h4>📊 Graph Overview</h4>

<p>

This interactive bar chart compares the number of
Best Seller and Non-Best Seller products available in the
Amazon product dataset.

Each bar represents the total count of products
belonging to each category.

</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Business Insights
# ----------------------------------------------------------

st.markdown("""
<div style="
background:white;
padding:20px;
border-radius:15px;
border-left:7px solid #146EB4;
box-shadow:0px 6px 16px rgba(0,0,0,.12);
margin-top:20px;
margin-bottom:25px;">

<h4>💡 Business Insights</h4>

<ul>

<li>🏆 Only a small proportion of products achieve the <b>Best Seller</b> badge.</li>

<li>📦 Most products belong to the <b>Non-Best Seller</b> category.</li>

<li>⭐ Best Seller products generally receive greater customer visibility and trust.</li>

<li>📈 Businesses can study Best Seller products to improve marketing strategies and inventory planning.</li>

<li>🎯 Identifying the characteristics of Best Seller products helps improve product performance and customer engagement.</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# 🌱 PART D : SUSTAINABILITY BADGE DISTRIBUTION
# ==========================================================

import pandas as pd
import plotly.express as px
import streamlit as st

# ----------------------------------------------------------
# SECTION HEADER
# ----------------------------------------------------------

st.markdown("""
<div style="
background:linear-gradient(90deg,#198754,#146EB4);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0px 6px 18px rgba(0,0,0,0.20);
margin-top:20px;
margin-bottom:25px;
">

<h2>🌱 Sustainability Badge Distribution</h2>

<p style="font-size:17px;">
Explore sustainability certifications available across Amazon products.
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# PREPARE DATA
# ----------------------------------------------------------

badge_counts = (
    filtered_df["sustainability_badges"]
    .fillna("No Sustainability Badge")
    .value_counts()
)

no_badge = badge_counts.get("No Sustainability Badge", 0)
small_business = badge_counts.get("Small Business", 0)
carbon_impact = badge_counts.get("Carbon impact", 0)

others = badge_counts.sum() - (
    no_badge +
    small_business +
    carbon_impact
)

badge_df = pd.DataFrame({

    "Badge":[
        "No Sustainability Badge",
        "Small Business",
        "Carbon Impact",
        "Others"
    ],

    "Count":[
        no_badge,
        small_business,
        carbon_impact,
        others
    ]

})

badge_df = badge_df[
    badge_df["Count"] > 0
]

# ----------------------------------------------------------
# PIE CHART
# ----------------------------------------------------------

fig = px.pie(

    badge_df,

    names="Badge",

    values="Count",

    hole=0.45,

    color="Badge",

    color_discrete_map={

        "No Sustainability Badge":"#66c2a5",

        "Small Business":"#fc8d62",

        "Carbon Impact":"#8da0cb",

        "Others":"#ffd92f"

    }

)

fig.update_traces(

    textposition="inside",

    textinfo="percent",

    marker=dict(
        line=dict(
            color="white",
            width=3
        )
    ),

    hovertemplate=
    "<b>%{label}</b><br>"
    "Products: %{value}<br>"
    "Percentage: %{percent}<extra></extra>"

)

fig.update_layout(

    title=dict(

        text="🌱 Sustainability Badge Distribution",

        x=0.5,

        font=dict(size=24)

    ),

    width=1200,

    height=700,

    template="plotly_white",

    legend=dict(

        title="Badge Type",

        font=dict(size=15)

    ),

    font=dict(size=16)

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------------------------------
# GRAPH OVERVIEW
# ----------------------------------------------------------

st.markdown(
"""
<div style="
background:#ffffff;
padding:22px;
border-radius:15px;
border-left:7px solid #198754;
box-shadow:0px 5px 15px rgba(0,0,0,0.12);
margin-top:25px;
">

<h3>📊 Graph Overview</h3>

<p style="font-size:16px; line-height:1.8; color:#333333;">

This interactive Pie Chart illustrates the proportion of Amazon
products with different sustainability badges.

Each slice represents the percentage share of products
belonging to a specific sustainability category.

The chart highlights whether products carry
environmental certifications or no badge at all.

</p>

</div>
""",
unsafe_allow_html=True
)

# ----------------------------------------------------------
# BUSINESS INSIGHTS
# ----------------------------------------------------------

st.markdown(
"""
<div style="
background:#ffffff;
padding:22px;
border-radius:15px;
border-left:7px solid #146EB4;
box-shadow:0px 5px 15px rgba(0,0,0,0.12);
margin-top:20px;
margin-bottom:30px;
">

<h3>💡 Business Insights</h3>

<ul style="font-size:16px; line-height:2; color:#333333;">

<li>🌱 Most Amazon products do not have a Sustainability Badge.</li>

<li>🏪 Only a small percentage belong to the Small Business category.</li>

<li>🌍 Carbon Impact badges appear on only a limited number of products.</li>

<li>📈 Sustainability certifications help increase customer trust and brand reputation.</li>

<li>🎯 Businesses should encourage sellers to adopt eco-friendly certifications.</li>

</ul>

</div>
""",
unsafe_allow_html=True
)

st.markdown("---")
# ==========================================================
# 🛒 PART E : TOP 10 MOST PURCHASED PRODUCTS
# ==========================================================

import plotly.graph_objects as go

# ----------------------------------------------------------
# SECTION HEADER
# ----------------------------------------------------------

st.markdown("""
<div style="
background:linear-gradient(90deg,#FF9900,#146EB4);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0px 6px 18px rgba(0,0,0,0.20);
margin-top:20px;
margin-bottom:25px;
">

<h2>🛒 Top 10 Most Purchased Products</h2>

<p style="font-size:17px;">
Products with the highest customer purchases during the last month.
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# CLEAN PURCHASE COLUMN
# ----------------------------------------------------------

purchase_df = filtered_df.copy()

purchase_df["bought_in_last_month"] = (
    purchase_df["bought_in_last_month"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace("+", "", regex=False)
    .str.replace("K", "000", regex=False)
)

purchase_df["bought_in_last_month"] = pd.to_numeric(
    purchase_df["bought_in_last_month"],
    errors="coerce"
)

top10 = (
    purchase_df[
        ["title", "bought_in_last_month"]
    ]
    .dropna()
    .sort_values(
        "bought_in_last_month",
        ascending=False
    )
    .head(10)
)

top10["Product"] = top10["title"].apply(
    lambda x: x[:30] + "..." if len(x) > 30 else x
)

# ----------------------------------------------------------
# RADAR CHART
# ----------------------------------------------------------

fig = go.Figure()

fig.add_trace(

    go.Scatterpolar(

        r=top10["bought_in_last_month"],

        theta=top10["Product"],

        fill="toself",

        line=dict(
            color="royalblue",
            width=4
        ),

        marker=dict(
            size=8,
            color="crimson"
        ),

        hovertemplate=
        "<b>%{theta}</b><br>"
        "Purchased : %{r}<extra></extra>"

    )

)

fig.update_layout(

    title=dict(

        text="🛒 Top 10 Most Purchased Products",

        x=0.5,

        font=dict(size=24)

    ),

    template="plotly_white",

    width=1200,

    height=800,

    polar=dict(

        radialaxis=dict(

            visible=True,

            gridcolor="lightgray"

        )

    ),

    showlegend=False

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------------------------------
# GRAPH OVERVIEW
# ----------------------------------------------------------

st.markdown("""
<div style="
background:#FFFFFF;
padding:22px;
border-radius:15px;
border-left:7px solid #FF9900;
box-shadow:0px 5px 15px rgba(0,0,0,0.12);
margin-top:20px;
">

<h3>📊 Graph Overview</h3>

<p style="font-size:16px; line-height:1.8; color:#333333;">

This interactive Radar Chart displays the Top 10 most purchased
Amazon products based on the <b>Bought in Last Month</b> column.

Products extending farther from the center represent
higher purchase counts and stronger customer demand.

The chart provides an easy comparison of product popularity.

</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# BUSINESS INSIGHTS
# ----------------------------------------------------------

st.markdown("""
<div style="
background:#FFFFFF;
padding:22px;
border-radius:15px;
border-left:7px solid #146EB4;
box-shadow:0px 5px 15px rgba(0,0,0,0.12);
margin-top:20px;
margin-bottom:25px;
">

<h3>💡 Business Insights</h3>

<ul style="font-size:16px; line-height:2; color:#333333;">

<li>🛒 Products with higher purchase counts represent strong customer demand.</li>

<li>📦 Highly purchased products should receive inventory priority.</li>

<li>⭐ Popular products can be promoted further through advertising campaigns.</li>

<li>📈 Purchase trends help businesses understand customer preferences.</li>

<li>🎯 Monitoring top-selling products supports better sales planning and inventory management.</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# 🎯 FINAL SUMMARY
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#146EB4,#00B894);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0px 6px 18px rgba(0,0,0,.20);
margin-top:20px;
margin-bottom:25px;
">

<h2>🎯 Product Analysis Summary</h2>

<p style="font-size:17px;">
Final Business Insights from Amazon Product Analysis
</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------

st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.10);
border-left:6px solid #146EB4;
">

<h3>📌 Key Insights</h3>

<ul style="font-size:16px;line-height:2;">

<li>⭐ Most products have ratings above <b>4.0</b>.</li>

<li>🏆 Best Seller products receive higher customer engagement.</li>

<li>🛒 Popular products show higher monthly purchases.</li>

<li>🌱 Sustainability badges are available for only a small number of products.</li>

<li>📦 Most products have Buy Box availability.</li>

<li>💰 Competitive pricing improves product popularity.</li>

</ul>

</div>
""", unsafe_allow_html=True)

# -----------------------------

st.success("✅ Product Analysis Completed Successfully.")

st.info(
"""
This analysis provides valuable insights into customer ratings,
product popularity, pricing, sustainability, and Buy Box availability,
helping businesses make better product decisions.
"""
)