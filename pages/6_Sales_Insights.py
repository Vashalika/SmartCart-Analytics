# ==========================================================
# SALES ANALYSIS
# SmartCart Analytics
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
    page_title="Sales Analysis",
    page_icon="📈",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================

df = load_products()
# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.stApp{
    background:#F4F6F9;
}

/* Hide Streamlit */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Title Card */

.title-box{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:25px;

border-radius:18px;

box-shadow:0px 8px 20px rgba(0,0,0,.25);

margin-bottom:25px;

}

.title-box h1{

color:white;

text-align:center;

font-size:38px;

margin-bottom:10px;

}

.title-box p{

color:white;

text-align:center;

font-size:18px;

}

/* KPI Cards */

div[data-testid="metric-container"]{

background:white;

padding:18px;

border-radius:15px;

border-left:7px solid #FF9900;

box-shadow:0px 6px 15px rgba(0,0,0,.15);

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# PAGE HEADER
# ==========================================================

st.markdown("""
<div class="title-box">

<h1>📈 Sales Analysis Dashboard</h1>

<p>
Analyze Amazon Product Performance, Customer Ratings,
Reviews, Pricing Strategy and Sales Trends using
interactive visualizations.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# INTRODUCTION
# ==========================================================

st.info("""
### 📌 About this Page

This dashboard analyzes Amazon product sales data using
interactive charts created with Plotly.

The visualizations help understand

• Customer Ratings

• Product Prices

• Reviews

• Product Demand

• Best Seller Products

• Sustainability

• Buy Box Availability

• Delivery Performance

Every chart is generated from the cleaned Kaggle dataset.
""")

# ==========================================================
# SEARCH PRODUCT
# ==========================================================

search = st.text_input(
    "🔍 Search Product",
    placeholder="Enter Product Name..."
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

# ==========================================================
# KPI SECTION
# ==========================================================

st.markdown("## 📊 Sales Dashboard Summary")

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(
        "📦 Products",
        f"{total_products:,}"
    )

with c2:

    st.metric(
        "⭐ Avg Rating",
        average_rating
    )

with c3:

    st.metric(
        "💰 Avg Price",
        f"${average_price:,.2f}"
    )

with c4:

    st.metric(
        "📝 Reviews",
        f"{total_reviews:,}"
    )

st.markdown("---")
# ==========================================================
# CUSTOMER RATING DISTRIBUTION
# ==========================================================

st.markdown("""
<style>

/* Section Title */

.chart-title{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:18px;

border-radius:16px;

margin-top:15px;

margin-bottom:18px;

box-shadow:0px 6px 15px rgba(0,0,0,.20);

}

.chart-title h2{

color:white;

text-align:center;

margin:0;

font-size:30px;

}

.chart-title p{

color:#F8F9FA;

text-align:center;

margin-top:8px;

font-size:16px;

}

/* Insight Card */

.insight{

background:white;

padding:22px;

border-left:8px solid #FF9900;

border-radius:15px;

box-shadow:0px 6px 15px rgba(0,0,0,.15);

margin-top:20px;

margin-bottom:35px;

}

.insight h3{

color:#146EB4;

margin-bottom:15px;

}

.insight ul{

font-size:17px;

line-height:2;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SECTION HEADER
# ==========================================================

st.markdown("""

<div class="chart-title">

<h2>⭐ Customer Rating Distribution</h2>

<p>
Analyze how Amazon product ratings are distributed across the
entire dataset to understand customer satisfaction.
</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# CHART
# ==========================================================

fig = px.histogram(

    filtered_df,

    x="rating",

    nbins=20,

    color_discrete_sequence=["#146EB4"],

    template="plotly_white"

)

fig.update_layout(

    title="⭐ Distribution of Customer Ratings",

    title_x=0.5,

    height=650,

    xaxis_title="Customer Rating",

    yaxis_title="Number of Products",

    font=dict(size=16)

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# BUSINESS INSIGHT
# ==========================================================

st.markdown("""

<div class="insight">

<h3>💡 Business Insights</h3>

<ul>

<li>⭐ Most Amazon products have ratings between <b>4.0 and 5.0</b>, indicating strong customer satisfaction.</li>

<li>📦 Higher-rated products build greater customer trust and improve purchase decisions.</li>

<li>📈 Only a small number of products have ratings below 3.5, showing that low-rated products are uncommon.</li>

<li>🛒 Businesses can use customer ratings to identify top-performing products and improve product quality.</li>

<li>🚀 The dataset is positively skewed because it mainly contains active and popular Amazon products.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# BOUGHT IN LAST MONTH ANALYSIS
# ==========================================================

st.markdown("""
<style>

/* Section Header */

.analysis-header{
    background:linear-gradient(90deg,#232F3E,#146EB4);
    padding:18px;
    border-radius:16px;
    margin-top:20px;
    margin-bottom:20px;
    box-shadow:0px 8px 18px rgba(0,0,0,.20);
}

.analysis-header h2{
    color:white;
    text-align:center;
    margin:0;
    font-size:30px;
}

.analysis-header p{
    color:#F8F9FA;
    text-align:center;
    font-size:16px;
    margin-top:8px;
}

/* Business Insight */

.business-box{

background:white;

padding:25px;

border-left:8px solid #FF9900;

border-radius:15px;

box-shadow:0px 6px 15px rgba(0,0,0,.15);

margin-top:25px;

margin-bottom:35px;

}

.business-box h3{

color:#146EB4;

margin-bottom:15px;

}

.business-box li{

font-size:17px;

line-height:1.9;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# TITLE
# ==========================================================

st.markdown("""

<div class="analysis-header">

<h2>📦 Products Bought in Last Month</h2>

<p>

Analyze customer purchasing trends and identify
high-demand Amazon products.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# CREATE PURCHASE CATEGORIES
# ==========================================================

purchase_category = pd.cut(

    filtered_df["bought_in_last_month"],

    bins=[0,50,100,200,500,1000,2000,
          filtered_df["bought_in_last_month"].max()+1],

    labels=[

        "1-50",

        "51-100",

        "101-200",

        "201-500",

        "501-1K",

        "1K-2K",

        "2K+"

    ],

    include_lowest=True

)

purchase_counts = (

    purchase_category

    .value_counts()

    .sort_index()

    .reset_index()

)

purchase_counts.columns=[

    "Purchase Category",

    "Number of Products"

]

# ==========================================================
# FUNNEL CHART
# ==========================================================

fig = px.funnel(

    purchase_counts,

    y="Purchase Category",

    x="Number of Products",

    color="Purchase Category",

    text="Number of Products",

    color_discrete_sequence=px.colors.qualitative.Set2

)

fig.update_traces(

    texttemplate="%{value:,}",

    textposition="inside"

)

fig.update_layout(

    title="📦 Products Bought in Last Month",

    title_x=0.5,

    height=700,

    template="plotly_white",

    font=dict(size=16)

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ==========================================================
# BUSINESS INSIGHT
# ==========================================================

st.markdown("""

<div class="business-box">

<h3>💡 Business Insights</h3>

<ul>

<li>📦 Most Amazon products fall into the <b>50+ and 100+ purchases</b> category, indicating moderate customer demand.</li>

<li>🚀 Only a small percentage of products reach <b>2K+ monthly purchases</b>, making them top-performing products.</li>

<li>📈 The funnel becomes narrower at higher purchase levels, showing that only a few products become best sellers.</li>

<li>🛒 Products with lower purchase counts may require promotions, discounts, or better product visibility.</li>

<li>🎯 High-demand products should be prioritized for inventory planning and stock management.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# CURRENT PRICE DISTRIBUTION ANALYSIS
# ==========================================================

st.markdown("""
<style>

/* Section Header */

.price-header{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:18px;

border-radius:15px;

margin-top:20px;

margin-bottom:20px;

box-shadow:0px 8px 18px rgba(0,0,0,.20);

}

.price-header h2{

color:white;

text-align:center;

margin:0;

font-size:30px;

}

.price-header p{

color:#F8F9FA;

text-align:center;

font-size:16px;

margin-top:8px;

}

/* Business Insight Card */

.price-insight{

background:white;

padding:22px;

border-left:8px solid #FF9900;

border-radius:15px;

box-shadow:0px 6px 15px rgba(0,0,0,.15);

margin-top:25px;

margin-bottom:35px;

}

.price-insight h3{

color:#146EB4;

margin-bottom:15px;

}

.price-insight li{

font-size:17px;

line-height:1.9;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# TITLE
# ==========================================================

st.markdown("""

<div class="price-header">

<h2>💰 Current Price Distribution</h2>

<p>

Analyze how discounted product prices are distributed across
Amazon products and identify pricing trends.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# BOXPLOT
# ==========================================================

fig = px.box(

    filtered_df,

    y="current/discounted_price",

    color_discrete_sequence=["mediumseagreen"],

    template="plotly_white"

)

fig.update_layout(

    title="💰 Current Price Distribution",

    title_x=0.5,

    height=700,

    yaxis_title="Current Price ($)",

    font=dict(size=16)

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ==========================================================
# GRAPH OVERVIEW
# ==========================================================

st.markdown("""

<div class="price-insight">

<h3>📊 Graph Overview</h3>

<ul>

<li>📦 This box plot shows the distribution of discounted prices across Amazon products.</li>

<li>📈 The middle horizontal line represents the median product price.</li>

<li>📊 The box contains the middle 50% of all product prices (Interquartile Range).</li>

<li>📍 Points outside the whiskers represent price outliers.</li>

<li>💰 The visualization helps identify budget-friendly and premium-priced products.</li>

</ul>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.markdown("""

<div class="price-insight">

<h3>💡 Business Insights</h3>

<ul>

<li>💰 Most Amazon products fall within the low-to-medium price range.</li>

<li>🛍️ A small number of premium products appear as outliers with significantly higher prices.</li>

<li>📈 Competitive pricing plays an important role in attracting customers.</li>

<li>🏷️ Discounted pricing helps improve customer engagement and purchase decisions.</li>

<li>🚀 Businesses can use this analysis to optimize pricing strategies and identify opportunities for promotional campaigns.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# CUSTOMER REVIEWS DISTRIBUTION
# ==========================================================

import numpy as np

st.markdown("""
<style>

/* Section Header */

.review-header{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:18px;

border-radius:15px;

margin-top:20px;

margin-bottom:20px;

box-shadow:0px 8px 18px rgba(0,0,0,.20);

}

.review-header h2{

color:white;

text-align:center;

margin:0;

font-size:30px;

}

.review-header p{

color:#F8F9FA;

text-align:center;

font-size:16px;

margin-top:8px;

}

/* Insight Card */

.review-card{

background:white;

padding:22px;

border-left:8px solid #FF9900;

border-radius:15px;

box-shadow:0px 6px 15px rgba(0,0,0,.15);

margin-top:25px;

margin-bottom:35px;

}

.review-card h3{

color:#146EB4;

margin-bottom:15px;

}

.review-card li{

font-size:17px;

line-height:1.9;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# TITLE
# ==========================================================

st.markdown("""

<div class="review-header">

<h2>📝 Customer Reviews Distribution</h2>

<p>

Analyze customer engagement by studying the distribution of
product reviews using a logarithmic scale.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# PREPARE DATA
# ==========================================================

reviews = filtered_df["number_of_reviews"].dropna()

log_reviews = np.log1p(reviews)

counts, bins = np.histogram(log_reviews, bins=40)

centers = (bins[:-1] + bins[1:]) / 2

# ==========================================================
# PLOTLY CHART
# ==========================================================

fig = go.Figure()

fig.add_trace(

    go.Scatter(

        x=centers,

        y=counts,

        mode="lines",

        line=dict(

            color="royalblue",

            width=4,

            shape="spline"

        ),

        fill="tozeroy",

        fillcolor="rgba(65,105,225,0.25)",

        name="Customer Reviews"

    )

)

fig.update_layout(

    title="📝 Distribution of Customer Reviews (Log Scale)",

    title_x=0.5,

    xaxis_title="Log(Number of Reviews)",

    yaxis_title="Number of Products",

    template="plotly_white",

    height=650,

    font=dict(size=16)

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ==========================================================
# GRAPH OVERVIEW
# ==========================================================

st.markdown("""

<div class="review-card">

<h3>📊 Graph Overview</h3>

<ul>

<li>📝 Displays the distribution of customer review counts across Amazon products.</li>

<li>📈 Log transformation improves visualization by reducing the impact of extremely large review counts.</li>

<li>📦 Most products have relatively fewer customer reviews.</li>

<li>⭐ A small number of products receive exceptionally high customer engagement.</li>

<li>🔍 The smooth curve highlights the overall review distribution pattern.</li>

</ul>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.markdown("""

<div class="review-card">

<h3>💡 Business Insights</h3>

<ul>

<li>⭐ Products with more reviews generally gain higher customer trust.</li>

<li>🛍️ Highly reviewed products usually have greater visibility on Amazon.</li>

<li>📈 Customer reviews strongly influence purchasing decisions.</li>

<li>🚀 Businesses should encourage verified buyers to leave product reviews.</li>

<li>🎯 Review analysis helps identify products with strong customer engagement.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART F
# LISTED PRICE VS CURRENT PRICE ANALYSIS
# ==========================================================

st.markdown("""
<style>

.price-title{
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:18px;
border-radius:15px;
text-align:center;
color:white;
font-size:28px;
font-weight:bold;
margin-top:25px;
margin-bottom:10px;
box-shadow:0px 6px 18px rgba(0,0,0,.25);
}

.price-desc{
background:white;
padding:18px;
border-radius:12px;
border-left:6px solid #FF9900;
font-size:16px;
box-shadow:0px 5px 12px rgba(0,0,0,.12);
margin-bottom:20px;
}

.insight-box{
background:#E8F4FD;
padding:20px;
border-radius:12px;
border-left:7px solid #146EB4;
font-size:16px;
box-shadow:0px 5px 12px rgba(0,0,0,.10);
margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="price-title">

💰 Listed Price vs Current Price Analysis

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="price-desc">

This interactive Scatter Plot compares the original listed price with the
current discounted selling price of Amazon products.

It helps understand discount strategies,
pricing patterns,
premium products,
and customer pricing behavior.

</div>
""", unsafe_allow_html=True)
fig = px.scatter(
    df,
    x="listed_price",
    y="current/discounted_price",
    color="rating",
    hover_data=["title"],
    opacity=0.75,
    template="plotly_white",
    color_continuous_scale="Viridis",
    height=700
)

fig.update_layout(

    title="💰 Listed Price vs Current Price",

    title_x=0.5,

    xaxis_title="Listed Price ($)",

    yaxis_title="Current Price ($)",

    font=dict(size=15)

)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.markdown("""
<div class="insight-box">

<h3>📊 Graph Overview</h3>

<ul>

<li>Each point represents one Amazon product.</li>

<li>X-axis shows the original listed price.</li>

<li>Y-axis shows the discounted selling price.</li>

<li>Colors represent customer ratings.</li>

<li>Products below the diagonal indicate higher discounts.</li>

</ul>

<h3>💡 Business Insight</h3>

<ul>

<li>Most products are sold below their listed price.</li>

<li>Discount pricing is one of Amazon's major selling strategies.</li>

<li>Premium-priced products appear as outliers in the dataset.</li>

<li>Products with competitive discounts generally receive better customer engagement.</li>

<li>This visualization helps businesses optimize pricing and promotional strategies.</li>

</ul>

</div>
""", unsafe_allow_html=True)