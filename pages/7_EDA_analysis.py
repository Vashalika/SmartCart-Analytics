# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from db_connection import load_products
# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="EDA Analysis",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# LOAD DATASET
# ==========================================================

df = load_products()

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main-title{
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:22px;
border-radius:18px;
text-align:center;
color:white;
font-size:34px;
font-weight:bold;
box-shadow:0px 8px 20px rgba(0,0,0,.25);
margin-bottom:20px;
}

.sub-title{
text-align:center;
font-size:18px;
color:white;
margin-top:8px;
}

.intro-box{
background:white;
padding:25px;
border-radius:18px;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
border-left:8px solid #FF9900;
margin-top:20px;
margin-bottom:20px;
}

.intro-box h3{
color:#232F3E;
}

.intro-box p{
font-size:16px;
line-height:1.9;
text-align:justify;
}

.metric-card{
background:white;
padding:22px;
border-radius:18px;
text-align:center;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
border-top:6px solid #146EB4;
transition:0.3s;
}

.metric-card:hover{
transform:translateY(-8px);
box-shadow:0px 12px 24px rgba(0,0,0,.25);
}

.metric-title{
font-size:18px;
font-weight:bold;
color:#555;
}

.metric-value{
font-size:34px;
font-weight:bold;
color:#146EB4;
margin-top:10px;
}

.section-title{
background:#232F3E;
padding:14px;
border-radius:12px;
color:white;
font-size:24px;
text-align:center;
margin-top:30px;
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="main-title">

📊 Exploratory Data Analysis (EDA)

<div class="sub-title">

SmartCart Analytics • Amazon Products Dashboard

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown("""

<div class="intro-box">

<h3>📖 About Exploratory Data Analysis</h3>

<p>

Exploratory Data Analysis (EDA) is one of the most important stages of any
Data Science project. It helps understand the dataset by identifying
patterns, trends, relationships, distributions, and hidden insights before
performing advanced analysis or machine learning.

In this project, EDA has been performed on the Amazon Products dataset to
analyze customer behaviour, pricing strategies, product popularity,
delivery performance, Buy Box availability, sponsored products, and
overall marketplace trends using interactive Plotly visualizations.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# OBJECTIVES
# ==========================================================

st.markdown('<div class="section-title">🎯 Objectives of EDA</div>',
unsafe_allow_html=True)

st.markdown("""

✅ Understand the structure of the Amazon Products dataset.

✅ Identify customer purchasing behaviour.

✅ Explore Best Seller and Sponsored Products.

✅ Analyze Buy Box Availability.

✅ Study Delivery Performance.

✅ Analyze Product Popularity.

✅ Discover hidden business patterns.

✅ Generate meaningful business insights.

""")

# ==========================================================
# KPI CARDS
# ==========================================================

total_products = len(df)
total_columns = df.shape[1]
avg_rating = round(df["rating"].mean(),2)

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.markdown(f"""

<div class="metric-card">

<div class="metric-title">

📦 Products

</div>

<div class="metric-value">

{total_products:,}

</div>

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown(f"""

<div class="metric-card">

<div class="metric-title">

📑 Columns

</div>

<div class="metric-value">

{total_columns}

</div>

</div>

""",unsafe_allow_html=True)

with col3:

    st.markdown(f"""

<div class="metric-card">

<div class="metric-title">

⭐ Average Rating

</div>

<div class="metric-value">

{avg_rating}

</div>

</div>

""",unsafe_allow_html=True)

with col4:

    st.markdown(f"""

<div class="metric-card">

<div class="metric-title">

🏆 Best Sellers

</div>

<div class="metric-value">

</div>

</div>

""",unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART B
# BUY BOX AVAILABILITY ANALYSIS
# ==========================================================

st.markdown("""
<style>

.chart-title{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:18px;

border-radius:15px;

text-align:center;

color:white;

font-size:28px;

font-weight:bold;

margin-top:20px;

margin-bottom:20px;

box-shadow:0px 6px 18px rgba(0,0,0,.20);

}

.info-box{

background:white;

padding:22px;

border-radius:15px;

border-left:8px solid #FF9900;

box-shadow:0px 5px 15px rgba(0,0,0,.15);

margin-bottom:25px;

font-size:16px;

line-height:1.8;

}

.insight-box{

background:#F7FBFF;

padding:22px;

border-radius:15px;

border-left:8px solid #146EB4;

box-shadow:0px 5px 15px rgba(0,0,0,.15);

margin-top:20px;

line-height:1.8;

font-size:16px;

}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------

st.markdown("""

<div class="chart-title">

🛒 Buy Box Availability Analysis

</div>

""", unsafe_allow_html=True)

# ----------------------------------------------------------

st.markdown("""

<div class="info-box">

<h3>📖 Graph Overview</h3>

<p>

The <b>Amazon Buy Box</b> is the section where customers directly purchase a
product using the <b>"Buy Now"</b> or <b>"Add to Cart"</b> button.

This interactive Donut Chart compares products that have the Buy Box
available with those that do not. High Buy Box availability generally
indicates better product accessibility and higher sales potential.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# DONUT CHART
# ==========================================================

buybox_counts = df["buy_box_availability"].value_counts().reset_index()
buybox_counts.columns = ["Availability","Count"]

fig = px.pie(
    buybox_counts,
    names="Availability",
    values="Count",
    hole=0.60,
    color="Availability",
    color_discrete_sequence=["#00CC96","#EF553B"]
)

fig.update_traces(

    textinfo="percent+label",

    textfont_size=18,

    marker=dict(
        line=dict(color="white",width=3)
    ),

    hovertemplate=
    "<b>%{label}</b><br>"
    "Products : %{value:,}<br>"
    "Percentage : %{percent}<extra></extra>"

)

fig.add_annotation(

    text="<b>Buy Box</b><br><span style='color:green'>Availability</span>",

    showarrow=False,

    font=dict(size=20)

)

fig.update_layout(

    title=dict(

        text="🛒 Buy Box Availability Distribution",

        x=0.5,

        font=dict(size=26)

    ),

    template="plotly_white",

    width=1050,

    height=700,

    legend=dict(

        title="Availability",

        font=dict(size=15)

    )

)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# BUSINESS INSIGHT
# ==========================================================

st.markdown("""

<div class="insight-box">

<h3 style="color:#146EB4;">

💡 Business Insight

</h3>

<ul>

<li>🛒 Most Amazon products have the <b>Buy Box available</b>, making them immediately accessible for customers.</li>

<li>📦 Products with Buy Box availability generally enjoy higher visibility and improved conversion rates.</li>

<li>🚀 A smaller percentage of products do not have Buy Box access, which may reduce customer purchases.</li>

<li>📈 Maintaining high Buy Box availability improves customer experience and supports better sales performance.</li>

<li>🎯 Sellers should optimize inventory, pricing, and fulfillment to maximize Buy Box eligibility.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART C
# 🚚 DELIVERY DETAILS ANALYSIS
# ==========================================================

st.markdown("""
<style>

.chart-header{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:18px;

border-radius:15px;

text-align:center;

color:white;

font-size:28px;

font-weight:bold;

box-shadow:0px 8px 20px rgba(0,0,0,.20);

margin-top:20px;

margin-bottom:20px;

}

.graph-box{

background:white;

padding:22px;

border-radius:18px;

box-shadow:0px 6px 18px rgba(0,0,0,.15);

border-left:8px solid #FF9900;

margin-bottom:25px;

}

.insight-box{

background:#F7FBFF;

padding:22px;

border-radius:18px;

border-left:8px solid #146EB4;

box-shadow:0px 6px 18px rgba(0,0,0,.15);

margin-top:20px;

}

</style>

""", unsafe_allow_html=True)

# --------------------------------------------------------

st.markdown("""

<div class="chart-header">

🚚 Delivery Details Analysis

</div>

""", unsafe_allow_html=True)

# --------------------------------------------------------

st.markdown("""

<div class="graph-box">

<h3 style="color:#232F3E;">

📖 Graph Overview

</h3>

<p style="font-size:16px; line-height:1.8;">

Delivery speed and availability play an important role in customer
satisfaction. This interactive Treemap visualizes the
<b>Top 15 Delivery Details</b> available across Amazon products.

Each rectangle represents a delivery option, where the size indicates
how many products belong to that delivery schedule.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# TREEMAP
# ==========================================================

delivery_count = (

    df["delivery_details"]

    .value_counts()

    .head(15)

    .reset_index()

)

delivery_count.columns = ["Delivery Details","Count"]

fig = px.treemap(

    delivery_count,

    path=["Delivery Details"],

    values="Count",

    color="Count",

    color_continuous_scale="Blues",

    title="🚚 Top 15 Delivery Details"

)

fig.update_layout(

    width=1150,

    height=720,

    title_x=0.5,

    margin=dict(t=60,l=20,r=20,b=20),

    font=dict(size=16),

    template="plotly_white"

)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# BUSINESS INSIGHT
# ==========================================================

st.markdown("""

<div class="insight-box">

<h3 style="color:#146EB4;">

💡 Business Insight

</h3>

<ul>

<li>🚚 Larger rectangles indicate delivery schedules available for the highest number of products.</li>

<li>📦 Fast delivery options dominate the Amazon marketplace, improving customer satisfaction.</li>

<li>⭐ Efficient delivery increases customer trust and encourages repeat purchases.</li>

<li>📈 Sellers offering faster shipping gain better visibility and competitive advantage.</li>

<li>🎯 Businesses should continue improving logistics and fulfillment to maintain excellent delivery performance.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART D
# 💰 PRICE ON VARIANT DISTRIBUTION
# ==========================================================

st.markdown("""
<style>

.section-header{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:18px;

border-radius:16px;

text-align:center;

color:white;

font-size:28px;

font-weight:bold;

margin-top:20px;

margin-bottom:20px;

box-shadow:0px 8px 18px rgba(0,0,0,.20);

}

.graph-info{

background:white;

padding:22px;

border-radius:18px;

border-left:8px solid #FF9900;

box-shadow:0px 5px 15px rgba(0,0,0,.15);

margin-bottom:25px;

}

.insight-card{

background:#F5FAFF;

padding:22px;

border-radius:18px;

border-left:8px solid #146EB4;

box-shadow:0px 5px 15px rgba(0,0,0,.15);

margin-top:20px;

}

</style>

""", unsafe_allow_html=True)

# ----------------------------------------------------------

st.markdown("""

<div class="section-header">

💰 Price on Variant Distribution Analysis

</div>

""", unsafe_allow_html=True)

# ----------------------------------------------------------

st.markdown("""

<div class="graph-info">

<h3 style="color:#232F3E;">

📖 Graph Overview

</h3>

<p style="font-size:16px; line-height:1.8;">

This Violin Plot visualizes the distribution of
<b>Product Variant Prices</b> available in the Amazon dataset.

Unlike a normal Box Plot, a Violin Plot displays both the
price distribution and data density, making it easier to
identify where most product prices are concentrated.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# VIOLIN PLOT
# ==========================================================

fig = px.violin(

    df,

    y="price_on_variant",

    box=True,

    points=False,

    title="💰 Price on Variant Distribution",

    color_discrete_sequence=["mediumseagreen"],

    template="plotly_white"

)

fig.update_layout(

    title_x=0.5,

    width=1100,

    height=700,

    yaxis_title="Price on Variant ($)",

    font=dict(size=15)

)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# BUSINESS INSIGHT
# ==========================================================

st.markdown("""

<div class="insight-card">

<h3 style="color:#146EB4;">

💡 Business Insight

</h3>

<ul>

<li>💰 The violin plot highlights where most Amazon product variant prices are concentrated.</li>

<li>📦 Wider sections of the violin indicate price ranges containing a larger number of products.</li>

<li>📈 The embedded box plot displays the median price and interquartile range (IQR).</li>

<li>🚀 Outliers represent premium or unusually low-priced product variants.</li>

<li>🎯 This analysis helps businesses understand pricing patterns and identify opportunities for competitive pricing strategies.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# 🏆 PART E : BEST SELLER STATUS ANALYSIS
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:15px;
border-radius:12px;
text-align:center;
margin-top:20px;
margin-bottom:20px;">

<h2 style="color:white;">
🏆 Best Seller Status Analysis
</h2>

<p style="color:white;font-size:16px;">
Compare the number of Best Seller and Non-Best Seller products.
</p>

</div>
""", unsafe_allow_html=True)

import plotly.express as px

# -------------------------------
# Clean Best Seller column
# -------------------------------
best_df = df.copy()

best_df["is_best_seller"] = (
    best_df["is_best_seller"]
    .astype(str)
    .str.strip()
)

# Convert values into two categories
best_df["Best Seller Status"] = best_df["is_best_seller"].apply(
    lambda x: "Best Seller"
    if "Best Seller" in x
    else "Non Best Seller"
)

# Count products
best_counts = (
    best_df["Best Seller Status"]
    .value_counts()
    .reset_index()
)

best_counts.columns = [
    "Status",
    "Number of Products"
]

# -------------------------------
# Interactive Bar Chart
# -------------------------------
fig = px.bar(
    best_counts,
    x="Status",
    y="Number of Products",
    color="Status",
    text="Number of Products",
    color_discrete_sequence=["#FF9900", "#146EB4"],
    template="plotly_white"
)

fig.update_traces(
    textposition="outside",
    textfont_size=16
)

fig.update_layout(
    title=dict(
        text="🏆 Distribution of Best Seller Products",
        x=0.5,
        font=dict(size=24)
    ),
    width=1100,
    height=650,
    xaxis_title="Product Status",
    yaxis_title="Number of Products",
    font=dict(size=15),
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.markdown("""
<div style="
background:#F8F9FA;
padding:18px;
border-left:8px solid #FF9900;
border-radius:10px;
margin-top:15px;">

<h4>💡 Business Insights</h4>

<ul>
<li>🏆 Only a small percentage of products achieve <b>Best Seller</b> status.</li>

<li>📦 Most products belong to the <b>Non Best Seller</b> category.</li>

<li>⭐ Best Seller products generally receive higher customer attention and stronger visibility.</li>

<li>📈 Businesses can analyze Best Seller products to improve pricing, promotions, and marketing strategies.</li>

<li>🎯 Understanding Best Seller patterns helps identify successful products and future growth opportunities.</li>
</ul>

</div>
""", unsafe_allow_html=True)
# ==========================================================
# PART F
# 🍭 SPONSORED VS NON-SPONSORED PRODUCTS
# ==========================================================

st.markdown("""
<style>

.section-header{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:18px;

border-radius:16px;

text-align:center;

color:white;

font-size:28px;

font-weight:bold;

margin-top:20px;

margin-bottom:20px;

box-shadow:0px 8px 18px rgba(0,0,0,.20);

}

.graph-box{

background:white;

padding:22px;

border-radius:18px;

border-left:8px solid #FF9900;

box-shadow:0px 6px 18px rgba(0,0,0,.15);

margin-bottom:25px;

}

.insight-box{

background:#F7FBFF;

padding:22px;

border-radius:18px;

border-left:8px solid #146EB4;

box-shadow:0px 6px 18px rgba(0,0,0,.15);

margin-top:20px;

}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------

st.markdown("""

<div class="section-header">

🍭 Sponsored vs Non-Sponsored Products

</div>

""", unsafe_allow_html=True)

# ----------------------------------------------------------

st.markdown("""

<div class="graph-box">

<h3 style="color:#232F3E;">

📖 Graph Overview

</h3>

<p style="font-size:16px; line-height:1.8;">

This visualization compares the number of
<b>Sponsored</b> and <b>Non-Sponsored</b> products
available in the Amazon dataset.

The Lollipop Chart provides a clean and visually attractive
alternative to a traditional bar chart while making comparison easier.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# LOLLIPOP CHART
# ==========================================================

import plotly.graph_objects as go

counts = df["is_sponsored"].value_counts().reset_index()
counts.columns = ["Status", "Count"]

counts["Status"] = counts["Status"].replace(
    {"Organic":"Non-Sponsored"}
)

fig = go.Figure()

# Lollipop Stem
fig.add_trace(go.Scatter(

    x=counts["Status"],

    y=counts["Count"],

    mode="lines",

    line=dict(
        color="lightgray",
        width=5,
        dash="dash"
    ),

    hoverinfo="skip",

    showlegend=False

))

# Lollipop Head
fig.add_trace(go.Scatter(

    x=counts["Status"],

    y=counts["Count"],

    mode="markers+text",

    marker=dict(

        size=28,

        color=["royalblue","crimson"],

        line=dict(color="black",width=2)

    ),

    text=counts["Count"],

    textposition="top center",

    textfont=dict(size=16),

    hovertemplate="<b>%{x}</b><br>Products : %{y:,}<extra></extra>",

    showlegend=False

))

fig.update_layout(

    title=dict(

        text="🍭 Sponsored vs Non-Sponsored Products",

        x=0.5,

        font=dict(size=24)

    ),

    template="plotly_white",

    width=1150,

    height=700,

    paper_bgcolor="#F8F9FA",

    plot_bgcolor="#F8F9FA",

    xaxis=dict(

        title="Sponsored Status",

        showgrid=False,

        tickfont=dict(size=15)

    ),

    yaxis=dict(

        title="Number of Products",

        gridcolor="lightgray",

        tickfont=dict(size=15)

    )

)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.markdown("""

<div class="insight-box">

<h3 style="color:#146EB4;">

💡 Business Insights

</h3>

<ul>

<li>🍭 The chart compares Sponsored and Non-Sponsored product listings available in the dataset.</li>

<li>📦 Sponsored products receive additional visibility through Amazon advertisements.</li>

<li>🛍️ Non-Sponsored (Organic) products rely primarily on customer ratings, reviews, and search rankings.</li>

<li>📈 Businesses can improve product visibility by combining sponsored advertising with high-quality product listings.</li>

<li>🚀 A balanced advertising strategy can increase customer engagement and overall sales performance.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART G
# ⭐ TOP 10 HIGHEST RATED PRODUCTS
# ==========================================================

st.markdown("""
<style>

.section-header{

background:linear-gradient(90deg,#232F3E,#146EB4);
padding:18px;
border-radius:16px;
text-align:center;
color:white;
font-size:28px;
font-weight:bold;
margin-top:20px;
margin-bottom:20px;
box-shadow:0px 8px 18px rgba(0,0,0,.20);

}

.graph-box{

background:white;
padding:22px;
border-radius:18px;
border-left:8px solid #FF9900;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
margin-bottom:25px;

}

.insight-box{

background:#F7FBFF;
padding:22px;
border-radius:18px;
border-left:8px solid #146EB4;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
margin-top:20px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="section-header">

⭐ Top 10 Highest Rated Products

</div>

""", unsafe_allow_html=True)

# ==========================================================
# GRAPH OVERVIEW
# ==========================================================

st.markdown("""

<div class="graph-box">

<h3 style="color:#232F3E;">

📖 Graph Overview

</h3>

<p style="font-size:16px; line-height:1.8;">

This chart ranks the <b>Top 10 Highest Rated Amazon Products</b>
based on customer ratings.

Each horizontal bar represents a product, making it easy to compare
customer satisfaction levels across the highest-performing products.

The interactive chart allows users to hover over each product to
view its exact rating.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# DATA PREPARATION
# ==========================================================

df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

top10 = (

    df[["title","rating"]]

    .dropna()

    .nlargest(10,"rating")

)

top10["title"] = top10["title"].str[:45] + "..."

# ==========================================================
# HORIZONTAL BAR CHART
# ==========================================================

fig = px.bar(

    top10,

    x="rating",

    y="title",

    orientation="h",

    color="rating",

    text="rating",

    color_continuous_scale="Plasma",

    title="⭐ Top 10 Highest Rated Products"

)

fig.update_traces(

    textposition="outside",

    marker_line_color="black",

    marker_line_width=1.2,

    hovertemplate="<b>%{y}</b><br>Rating : %{x}<extra></extra>"

)

fig.update_layout(

    template="plotly_white",

    title_x=0.5,

    width=1200,

    height=720,

    bargap=0.35,

    xaxis_title="Customer Rating",

    yaxis_title="Product Name",

    font=dict(size=15)

)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# BUSINESS INSIGHT
# ==========================================================

st.markdown("""

<div class="insight-box">

<h3 style="color:#146EB4;">

💡 Business Insights

</h3>

<ul>

<li>⭐ These products have received the highest customer ratings, indicating exceptional customer satisfaction.</li>

<li>📦 High-rated products generally build greater customer trust and improve purchase decisions.</li>

<li>🚀 Products with consistently excellent ratings are more likely to become Best Sellers.</li>

<li>📈 Businesses should analyze these products to understand the factors contributing to their success, such as pricing, quality, and customer experience.</li>

<li>🎯 Promoting highly rated products can increase sales, strengthen brand reputation, and improve overall marketplace performance.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART H
# 🕸️ TOP 10 MOST PURCHASED PRODUCTS
# ==========================================================

st.markdown("""
<style>

.section-header{

background:linear-gradient(90deg,#232F3E,#146EB4);
padding:18px;
border-radius:16px;
text-align:center;
color:white;
font-size:28px;
font-weight:bold;
margin-top:20px;
margin-bottom:20px;
box-shadow:0px 8px 18px rgba(0,0,0,.20);

}

.graph-box{

background:white;
padding:22px;
border-radius:18px;
border-left:8px solid #FF9900;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
margin-bottom:25px;

}

.insight-box{

background:#F7FBFF;
padding:22px;
border-radius:18px;
border-left:8px solid #146EB4;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
margin-top:20px;

}

</style>

""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="section-header">

🕸️ Top 10 Most Purchased Products

</div>

""", unsafe_allow_html=True)

# ==========================================================
# GRAPH OVERVIEW
# ==========================================================

st.markdown("""

<div class="graph-box">

<h3 style="color:#232F3E;">

📖 Graph Overview

</h3>

<p style="font-size:16px; line-height:1.8;">

This Radar (Spider) Chart visualizes the <b>Top 10 Most Purchased Products</b>
based on the <b>bought_in_last_month</b> column.

Each axis represents one product, while the distance from the center
shows its purchase count. Products farther from the center have
higher customer demand and stronger market popularity.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# DATA PREPARATION
# ==========================================================

purchase_df = df.copy()

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

    purchase_df[["title","bought_in_last_month"]]

    .dropna()

    .sort_values(

        "bought_in_last_month",

        ascending=False

    )

    .head(10)

)

top10["Product"] = top10["title"].apply(

    lambda x: x[:28]+"..." if len(x)>28 else x

)

# ==========================================================
# RADAR CHART
# ==========================================================

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

            size=9,

            color="crimson"

        ),

        hovertemplate="<b>%{theta}</b><br>Purchased : %{r:,}<extra></extra>"

    )

)

fig.update_layout(

    title=dict(

        text="🕸️ Top 10 Most Purchased Products",

        x=0.5,

        font=dict(size=24)

    ),

    template="plotly_white",

    width=950,

    height=850,

    showlegend=False,

    polar=dict(

        radialaxis=dict(

            visible=True,

            showline=True,

            gridcolor="lightgray",

            tickfont=dict(size=12)

        )

    )

)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.markdown("""

<div class="insight-box">

<h3 style="color:#146EB4;">

💡 Business Insights

</h3>

<ul>

<li>🛒 The radar chart highlights the <b>Top 10 most purchased Amazon products</b>, making it easy to compare customer demand.</li>

<li>📦 Products extending farther from the center represent significantly higher purchase volumes.</li>

<li>⭐ High purchase frequency usually reflects strong customer trust, competitive pricing, and positive product reputation.</li>

<li>📈 These products are excellent candidates for promotional campaigns, inventory prioritization, and recommendation systems.</li>

<li>🚀 Businesses can study the characteristics of these products to improve sales strategies and replicate their success across similar categories.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART I
# 🌐 PRODUCT POPULARITY VS PRICE VS CUSTOMER SATISFACTION
# ==========================================================

st.markdown("""
<style>

.section-header{

background:linear-gradient(90deg,#232F3E,#146EB4);
padding:18px;
border-radius:16px;
text-align:center;
color:white;
font-size:28px;
font-weight:bold;
margin-top:20px;
margin-bottom:20px;
box-shadow:0px 8px 18px rgba(0,0,0,.20);

}

.graph-box{

background:white;
padding:22px;
border-radius:18px;
border-left:8px solid #FF9900;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
margin-bottom:25px;

}

.insight-box{

background:#F7FBFF;
padding:22px;
border-radius:18px;
border-left:8px solid #146EB4;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
margin-top:20px;

}

</style>

""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="section-header">

🌐 Product Popularity vs Price vs Customer Satisfaction

</div>

""", unsafe_allow_html=True)

# ==========================================================
# GRAPH OVERVIEW
# ==========================================================

st.markdown("""

<div class="graph-box">

<h3 style="color:#232F3E;">

📖 Graph Overview

</h3>

<p style="font-size:16px; line-height:1.8;">

This interactive <b>3D Scatter Plot</b> simultaneously analyzes three
important business metrics:

<b>Current Price</b>,
<b>Number of Reviews</b>,
and
<b>Customer Rating</b>.

Each bubble represents one Amazon product.
The visualization helps identify popular, premium and highly-rated
products while revealing hidden relationships between price,
customer engagement and customer satisfaction.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# PREPARE DATA
# ==========================================================

scatter_df = df.dropna(

    subset=[
        "current/discounted_price",
        "number_of_reviews",
        "rating"
    ]

)

# ==========================================================
# 3D SCATTER PLOT
# ==========================================================

fig = px.scatter_3d(

    scatter_df,

    x="current/discounted_price",

    y="number_of_reviews",

    z="rating",

    color="rating",

    size="number_of_reviews",

    color_continuous_scale="Viridis",

    opacity=0.75,

    title="🌐 Product Popularity vs Price vs Customer Satisfaction"

)

fig.update_traces(

    marker=dict(

        line=dict(

            color="white",

            width=0.5

        )

    ),

    hovertemplate=

    "<b>Current Price :</b> $%{x}<br>"

    "<b>Reviews :</b> %{y:,}<br>"

    "<b>Rating :</b> %{z}<extra></extra>"

)

fig.update_layout(

    width=1200,

    height=760,

    title=dict(

        x=0.5,

        font=dict(size=24)

    ),

    template="plotly_white",

    paper_bgcolor="white",

    font=dict(size=15),

    scene=dict(

        xaxis_title="💰 Current Price",

        yaxis_title="📝 Number of Reviews",

        zaxis_title="⭐ Rating",

        bgcolor="white"

    ),

    coloraxis_colorbar=dict(

        title="Rating"

    )

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.markdown("""

<div class="insight-box">

<h3 style="color:#146EB4;">

💡 Business Insights

</h3>

<ul>

<li>⭐ Products with higher ratings generally receive a larger number of customer reviews, indicating stronger customer trust.</li>

<li>💰 Premium-priced products do not always receive the highest ratings, showing that product quality matters more than price alone.</li>

<li>📈 Products with both high ratings and high review counts represent the strongest-performing products in the Amazon marketplace.</li>

<li>🛒 Highly reviewed products demonstrate greater customer engagement and market visibility.</li>

<li>🎯 Businesses can use this analysis to optimize pricing strategies, improve customer satisfaction, and identify products with the greatest sales potential.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART J
# 📋 EDA SUMMARY, CONCLUSION & FUTURE SCOPE
# ==========================================================

st.markdown("""
<style>

.summary-header{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:20px;

border-radius:16px;

text-align:center;

color:white;

font-size:30px;

font-weight:bold;

box-shadow:0px 8px 18px rgba(0,0,0,.20);

margin-top:25px;

margin-bottom:25px;

}

.card{

background:white;

padding:25px;

border-radius:18px;

box-shadow:0px 6px 18px rgba(0,0,0,.15);

border-left:8px solid #FF9900;

margin-bottom:25px;

}

.card h3{

color:#232F3E;

}

.card p{

font-size:16px;

line-height:1.8;

text-align:justify;

}

.final-box{

background:#F5FAFF;

padding:25px;

border-radius:18px;

border-left:8px solid #146EB4;

box-shadow:0px 6px 18px rgba(0,0,0,.15);

margin-bottom:25px;

}

.quote-box{

background:linear-gradient(90deg,#146EB4,#232F3E);

padding:22px;

border-radius:18px;

color:white;

text-align:center;

font-size:22px;

font-weight:bold;

margin-top:30px;

box-shadow:0px 8px 18px rgba(0,0,0,.25);

}

</style>

""", unsafe_allow_html=True)

# ---------------------------------------------------------

st.markdown("""

<div class="summary-header">

📋 Exploratory Data Analysis Summary

</div>

""", unsafe_allow_html=True)

# ---------------------------------------------------------

st.markdown("""

<div class="card">

<h3>📊 Major Findings</h3>

<ul>

<li>⭐ Most Amazon products have customer ratings between <b>4.0 and 5.0</b>, indicating excellent customer satisfaction.</li>

<li>📝 Products with more reviews generally receive greater customer trust and visibility.</li>

<li>💰 Most products belong to affordable and medium price ranges, while premium products form only a small percentage.</li>

<li>🏆 Best Seller products represent a limited group but contribute significantly to marketplace performance.</li>

<li>🌱 Sustainability badges are available for only a small number of products, creating opportunities for future growth.</li>

<li>🚚 Fast delivery and Buy Box availability improve customer experience and increase purchase potential.</li>

</ul>

</div>

""", unsafe_allow_html=True)

# ---------------------------------------------------------

st.markdown("""

<div class="final-box">

<h3 style="color:#146EB4;">

💡 Business Recommendations

</h3>

<ul>

<li>📈 Promote highly rated products through personalized recommendations.</li>

<li>🛒 Increase Buy Box availability by improving pricing and inventory management.</li>

<li>💰 Maintain competitive pricing strategies for high-demand products.</li>

<li>🌱 Encourage sellers to adopt sustainability certifications.</li>

<li>🚚 Continue improving logistics to provide faster delivery services.</li>

<li>⭐ Improve products with lower ratings using customer feedback.</li>

</ul>

</div>

""", unsafe_allow_html=True)

# ---------------------------------------------------------

st.markdown("""

<div class="card">

<h3>📌 Project Conclusion</h3>

<p>

The <b>SmartCart Analytics Dashboard</b> successfully transformed raw Amazon
product data into meaningful business insights through data cleaning,
exploratory data analysis, and interactive visualizations.

The analysis highlighted customer behaviour, pricing strategies,
product popularity, sustainability, delivery performance,
and marketplace trends using Python, Pandas, Plotly,
Matplotlib and Seaborn.

These insights help businesses make data-driven decisions,
improve customer satisfaction, optimize pricing,
and increase overall business performance.

</p>

</div>

""", unsafe_allow_html=True)

# ---------------------------------------------------------

st.markdown("""

<div class="final-box">

<h3 style="color:#146EB4;">

🚀 Future Scope

</h3>

<ul>

<li>🤖 Build an AI-powered Product Recommendation System.</li>

<li>📈 Develop Machine Learning models for Sales Forecasting.</li>

<li>💬 Perform Customer Sentiment Analysis using Reviews.</li>

<li>🌐 Integrate Live Amazon Product Data using APIs.</li>

<li>☁ Deploy the dashboard on Streamlit Cloud for real-time access.</li>

<li>📊 Add Executive KPI Dashboards and Predictive Analytics.</li>

</ul>

</div>

""", unsafe_allow_html=True)

# ---------------------------------------------------------

st.markdown("""

<div class="quote-box">

📊 "Turning Raw Amazon Product Data into Meaningful Business Insights Through Data Analytics."

</div>

""", unsafe_allow_html=True)

st.success("✅ Exploratory Data Analysis Completed Successfully.")