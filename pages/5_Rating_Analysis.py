# ==========================================================
# SMARTCART ANALYTICS
# Rating Analysis
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
    page_title="Rating Analysis",
    page_icon="⭐",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================

df = load_products()
# ==========================================================
# AMAZON THEME
# ==========================================================

AMAZON_ORANGE = "#FF9900"
AMAZON_BLUE = "#146EB4"
AMAZON_NAVY = "#232F3E"
LIGHT = "#F4F6F9"

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

.stApp{
    background:#F4F6F9;
}

/* Hide Streamlit */

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Main container */

.block-container{
    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* Header Card */

.header-box{
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:25px;
border-radius:18px;
box-shadow:0px 8px 20px rgba(0,0,0,.25);
margin-bottom:25px;
}

.header-title{
color:white;
font-size:36px;
font-weight:bold;
text-align:center;
}

.header-text{
color:white;
font-size:18px;
text-align:center;
margin-top:8px;
}

/* Intro Card */

.intro-card{
background:white;
padding:25px;
border-radius:18px;
box-shadow:0px 5px 15px rgba(0,0,0,.15);
border-left:8px solid #FF9900;
margin-bottom:20px;
}

/* KPI */

div[data-testid="metric-container"]{
background:white;
padding:20px;
border-radius:18px;
border-top:6px solid #FF9900;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
transition:0.3s;
}

div[data-testid="metric-container"]:hover{
transform:translateY(-6px);
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# PAGE HEADER
# ==========================================================

st.markdown("""
<div class="header-box">

<div class="header-title">
⭐ Customer Rating Analysis
</div>

<div class="header-text">

Analyze customer satisfaction, product ratings,
rating distribution and overall product quality
using interactive visualizations.

</div>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown("""
<div class="intro-card">

<h3 style="color:#232F3E;">
📖 About this Analysis
</h3>

<p style="font-size:17px;">

Customer ratings are one of the most important indicators of
product quality and customer satisfaction on Amazon.

This page analyzes how ratings are distributed across products,
helping identify customer satisfaction levels and product performance.

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# RATING KPIs
# ==========================================================

total_products = len(df)

average_rating = round(df["rating"].mean(),2)

highest_rating = round(df["rating"].max(),2)

lowest_rating = round(df["rating"].min(),2)

k1,k2,k3,k4 = st.columns(4)

with k1:
    st.metric(
        "📦 Total Products",
        f"{total_products:,}"
    )

with k2:
    st.metric(
        "⭐ Average Rating",
        average_rating
    )

with k3:
    st.metric(
        "🏆 Highest Rating",
        highest_rating
    )

with k4:
    st.metric(
        "📉 Lowest Rating",
        lowest_rating
    )

st.markdown("---")
# ==========================================================
# PART B
# CUSTOMER RATING DISTRIBUTION
# ==========================================================

st.markdown("""
<style>

.rating-title{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:18px;

border-radius:15px;

text-align:center;

color:white;

font-size:28px;

font-weight:bold;

box-shadow:0px 6px 18px rgba(0,0,0,.25);

margin-top:10px;

margin-bottom:15px;

}

.rating-card{

background:white;

padding:22px;

border-radius:15px;

border-left:8px solid #FF9900;

box-shadow:0px 5px 15px rgba(0,0,0,.15);

font-size:17px;

margin-bottom:25px;

}

.insight-card{

background:#F8FBFF;

padding:22px;

border-radius:15px;

border-left:8px solid #146EB4;

box-shadow:0px 5px 15px rgba(0,0,0,.12);

margin-top:20px;

}

</style>
""", unsafe_allow_html=True)


st.markdown("""

<div class="rating-title">

⭐ Customer Rating Distribution

</div>

""", unsafe_allow_html=True)


st.markdown("""

<div class="rating-card">

<h4 style="color:#232F3E;">📖 Graph Introduction</h4>

<p>

Customer ratings are one of the strongest indicators of customer satisfaction.

This interactive histogram shows how Amazon product ratings are distributed across the entire dataset.

The visualization helps identify whether most products receive positive or negative feedback from customers.

</p>

</div>

""", unsafe_allow_html=True)
fig = px.histogram(

    df,

    x="rating",

    nbins=20,

    title="⭐ Distribution of Customer Ratings",

    color_discrete_sequence=["royalblue"],

    template="plotly_white"

)

fig.update_layout(

    title_x=0.5,

    height=700,

    xaxis_title="Customer Rating",

    yaxis_title="Number of Products",

    font=dict(size=15)

)

st.plotly_chart(

    fig,

    use_container_width=True

)
st.markdown("""

<div class="insight-card">

<h3 style="color:#146EB4;">

📈 Graph Overview

</h3>

<ul>

<li>Most Amazon products are rated between <b>4.0 and 5.0</b>.</li>

<li>The histogram shows a strong concentration of highly rated products.</li>

<li>Only a small percentage of products have ratings below 3.5.</li>

<li>The distribution is positively skewed toward higher ratings.</li>

</ul>

<hr>

<h3 style="color:#146EB4;">

💡 Business Insights

</h3>

<ul>

<li>⭐ High ratings indicate strong customer satisfaction.</li>

<li>🛒 Highly rated products attract greater customer trust.</li>

<li>📈 Products with better ratings generally perform better in the marketplace.</li>

<li>🎯 Businesses should continuously monitor customer ratings to improve product quality.</li>

<li>🚀 Maintaining ratings above 4.0 helps improve sales and brand reputation.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART C
# CUSTOMER REVIEWS DISTRIBUTION
# ==========================================================

st.markdown("""
<style>

.review-title{

background:linear-gradient(90deg,#146EB4,#232F3E);

padding:18px;

border-radius:15px;

text-align:center;

color:white;

font-size:28px;

font-weight:bold;

box-shadow:0px 8px 18px rgba(0,0,0,.25);

margin-top:15px;

margin-bottom:18px;

}

.review-card{

background:white;

padding:22px;

border-radius:15px;

border-left:8px solid #FF9900;

box-shadow:0px 5px 15px rgba(0,0,0,.15);

margin-bottom:20px;

font-size:17px;

line-height:1.7;

}

.review-insight{

background:#F7FBFF;

padding:22px;

border-radius:15px;

border-left:8px solid #146EB4;

box-shadow:0px 5px 15px rgba(0,0,0,.15);

margin-top:20px;

}

</style>
""", unsafe_allow_html=True)


st.markdown("""

<div class="review-title">

📝 Customer Reviews Distribution

</div>

""", unsafe_allow_html=True)


st.markdown("""

<div class="review-card">

<h4 style="color:#232F3E;">📖 Graph Introduction</h4>

<p>

Customer reviews represent customer engagement and product popularity.

Since review counts vary from a few reviews to millions of reviews,
a logarithmic transformation has been applied to better visualize the
distribution.

The smooth curve highlights how customer reviews are distributed
across Amazon products.

</p>

</div>

""", unsafe_allow_html=True)
import numpy as np
import plotly.graph_objects as go

reviews = df["number_of_reviews"].dropna()

log_reviews = np.log1p(reviews)

counts, bins = np.histogram(
    log_reviews,
    bins=40
)

centers = (bins[:-1] + bins[1:]) / 2

fig = go.Figure()

fig.add_trace(

    go.Scatter(

        x=centers,

        y=counts,

        mode="lines",

        line=dict(

            color="royalblue",

            width=5,

            shape="spline"

        ),

        fill="tozeroy",

        fillcolor="rgba(65,105,225,0.25)",

        name="Customer Reviews"

    )

)

fig.update_layout(

    title={

        "text":"<b>Distribution of Customer Reviews (Log Scale)</b>",

        "x":0.5

    },

    template="plotly_white",

    height=700,

    xaxis_title="Log(Number of Reviews)",

    yaxis_title="Number of Products",

    font=dict(size=15),

    hovermode="x unified"

)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.markdown("""

<div class="review-insight">

<h3 style="color:#146EB4;">

📈 Graph Overview

</h3>

<ul>

<li>The smooth curve shows the distribution of customer reviews after applying a logarithmic transformation.</li>

<li>Most products have relatively fewer customer reviews.</li>

<li>A small number of products receive exceptionally high review counts.</li>

<li>The log transformation improves readability by reducing the effect of extremely large values.</li>

</ul>

<hr>

<h3 style="color:#146EB4;">

💡 Business Insights

</h3>

<ul>

<li>📝 Products with more customer reviews generally gain greater visibility on Amazon.</li>

<li>⭐ High review counts increase customer trust and purchase confidence.</li>

<li>📦 Popular products tend to accumulate reviews much faster than regular products.</li>

<li>📈 Customer engagement can be improved by encouraging verified buyers to leave reviews.</li>

<li>🚀 Businesses should monitor review trends to identify top-performing products and improve customer satisfaction.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART D
# TOP 10 HIGHEST RATED PRODUCTS
# ==========================================================

st.markdown("""
<style>

.top-title{
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:18px;
border-radius:15px;
text-align:center;
color:white;
font-size:28px;
font-weight:bold;
box-shadow:0px 8px 18px rgba(0,0,0,.25);
margin-top:20px;
margin-bottom:20px;
}

.top-card{
background:white;
padding:22px;
border-radius:15px;
border-left:8px solid #FF9900;
box-shadow:0px 5px 15px rgba(0,0,0,.15);
margin-bottom:20px;
font-size:17px;
}

.top-insight{
background:#F8FBFF;
padding:22px;
border-radius:15px;
border-left:8px solid #146EB4;
box-shadow:0px 5px 15px rgba(0,0,0,.15);
margin-top:20px;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""

<div class="top-title">

🏆 Top 10 Highest Rated Products

</div>

""", unsafe_allow_html=True)


st.markdown("""

<div class="top-card">

<h4 style="color:#232F3E;">

📖 Graph Introduction

</h4>

<p>

This visualization ranks the Top 10 highest-rated Amazon products.

Each horizontal bar represents one product, allowing quick comparison
of customer ratings.

This chart helps identify products with exceptional customer satisfaction.

</p>

</div>

""", unsafe_allow_html=True)
df["rating"] = pd.to_numeric(
    df["rating"],
    errors="coerce"
)

top10 = (
    df[["title","rating"]]
    .dropna()
    .nlargest(10,"rating")
)

top10["Product"] = top10["title"].apply(
    lambda x: x[:45]+"..." if len(x)>45 else x
)

fig = px.bar(

    top10,

    x="rating",

    y="Product",

    orientation="h",

    color="rating",

    text="rating",

    color_continuous_scale="Plasma",

    title="Top 10 Highest Rated Products"

)

fig.update_traces(

    textposition="outside",

    marker_line_width=1,

    marker_line_color="black",

    hovertemplate="<b>%{y}</b><br>Rating : %{x}<extra></extra>"

)

fig.update_layout(

    template="plotly_white",

    title_x=0.5,

    height=700,

    xaxis_title="Customer Rating",

    yaxis_title="Product Name",

    font=dict(size=15),

    bargap=0.30

)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.markdown("""

<div class="top-insight">

<h3 style="color:#146EB4;">

📈 Graph Overview

</h3>

<ul>

<li>Displays the ten highest-rated Amazon products.</li>

<li>Products are ranked according to customer ratings.</li>

<li>Color intensity represents higher rating values.</li>

<li>Interactive hover displays exact rating and product name.</li>

</ul>

<hr>

<h3 style="color:#146EB4;">

💡 Business Insights

</h3>

<ul>

<li>⭐ Top-rated products generate greater customer trust.</li>

<li>🏆 Products with excellent ratings often perform better in sales.</li>

<li>📈 Businesses should study these products to understand quality standards.</li>

<li>🛒 Promoting highly rated products can improve customer engagement.</li>

<li>🚀 Maintaining consistently high ratings strengthens brand reputation.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART E
# ADVANCED PRODUCT RELATIONSHIP ANALYSIS
# ==========================================================

st.markdown("""
<style>

.scatter3d-title{
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:18px;
border-radius:15px;
text-align:center;
color:white;
font-size:28px;
font-weight:bold;
box-shadow:0px 8px 18px rgba(0,0,0,.25);
margin-top:20px;
margin-bottom:20px;
}

.scatter3d-card{
background:white;
padding:22px;
border-radius:15px;
border-left:8px solid #FF9900;
box-shadow:0px 5px 15px rgba(0,0,0,.15);
margin-bottom:20px;
font-size:17px;
line-height:1.7;
}

.scatter3d-insight{
background:#F8FBFF;
padding:22px;
border-radius:15px;
border-left:8px solid #146EB4;
box-shadow:0px 5px 15px rgba(0,0,0,.15);
margin-top:20px;
line-height:1.8;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""

<div class="scatter3d-title">

🌐 Product Popularity vs Price vs Customer Satisfaction

</div>

""", unsafe_allow_html=True)


st.markdown("""

<div class="scatter3d-card">

<h4 style="color:#232F3E;">

📖 Graph Introduction

</h4>

<p>

This interactive 3D Scatter Plot analyzes the relationship between
product price, customer reviews and customer ratings.

Each point represents one Amazon product.

The visualization helps identify whether expensive products receive
higher ratings and larger customer engagement.

Users can rotate, zoom and inspect the graph from different angles.

</p>

</div>

""", unsafe_allow_html=True)
scatter_df = df.dropna(
    subset=[
        "current/discounted_price",
        "number_of_reviews",
        "rating"
    ]
)

fig = px.scatter_3d(

    scatter_df,

    x="current/discounted_price",

    y="number_of_reviews",

    z="rating",

    color="rating",

    size="number_of_reviews",

    color_continuous_scale="Viridis",

    opacity=0.75,

    hover_data=["title"],

    title="🌐 Product Popularity vs Price vs Customer Satisfaction"

)

fig.update_traces(

    marker=dict(
        line=dict(
            width=0.5,
            color="white"
        )
    ),

    hovertemplate=

    "<b>%{customdata[0]}</b><br>" +

    "Price : $%{x}<br>" +

    "Reviews : %{y}<br>" +

    "Rating : %{z}<extra></extra>"

)

fig.update_layout(

    title=dict(

        x=0.5,

        font=dict(size=24)

    ),

    template="plotly_white",

    height=800,

    scene=dict(

        xaxis_title="💰 Current Price",

        yaxis_title="📝 Number of Reviews",

        zaxis_title="⭐ Rating",

        bgcolor="white"

    ),

    font=dict(size=14),

    coloraxis_colorbar=dict(

        title="Rating"

    )

)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.markdown("""

<div class="scatter3d-insight">

<h3 style="color:#146EB4;">

📈 Graph Overview

</h3>

<ul>

<li>Each point represents an individual Amazon product.</li>

<li>The X-axis displays the current selling price.</li>

<li>The Y-axis represents the total number of customer reviews.</li>

<li>The Z-axis represents the average customer rating.</li>

<li>Bubble size reflects customer engagement based on review count.</li>

<li>Bubble color indicates the rating level.</li>

</ul>

<hr>

<h3 style="color:#146EB4;">

💡 Business Insights

</h3>

<ul>

<li>⭐ Products with higher ratings generally attract more customer reviews.</li>

<li>🛒 Highly reviewed products usually gain greater visibility and customer trust.</li>

<li>💰 Premium-priced products do not always receive the highest ratings.</li>

<li>📦 Products combining competitive pricing, strong ratings and many reviews perform best in the marketplace.</li>

<li>📈 This analysis helps businesses identify benchmark products and improve pricing, quality and customer engagement strategies.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART F
# RATING ANALYSIS SUMMARY
# ==========================================================

st.markdown("""
<style>

.summary-title{
background:linear-gradient(90deg,#232F3E,#146EB4);
padding:18px;
border-radius:15px;
text-align:center;
color:white;
font-size:28px;
font-weight:bold;
box-shadow:0px 8px 18px rgba(0,0,0,.25);
margin-top:20px;
margin-bottom:20px;
}

.summary-card{
background:white;
padding:25px;
border-radius:18px;
border-left:8px solid #FF9900;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
margin-bottom:20px;
line-height:1.9;
}

.recommend-card{
background:#F8FBFF;
padding:25px;
border-radius:18px;
border-left:8px solid #146EB4;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
line-height:1.9;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""

<div class="summary-title">

📋 Rating Analysis Summary

</div>

""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""

<div class="summary-card">

<h3 style="color:#232F3E;">
📊 Key Findings
</h3>

✅ Most Amazon products have ratings between <b>4.0 – 5.0</b>.

<br><br>

✅ Products with higher ratings usually receive more customer reviews.

<br><br>

✅ Customer reviews indicate strong customer engagement and product popularity.

<br><br>

✅ Premium-priced products do not always receive the highest ratings.

<br><br>

✅ Products with high ratings and many reviews are generally the best-performing products.

</div>

""", unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class="recommend-card">

<h3 style="color:#146EB4;">
💡 Business Recommendations
</h3>

📈 Improve product quality to maintain ratings above <b>4.0</b>.

<br><br>

⭐ Encourage verified buyers to leave product reviews.

<br><br>

🛒 Promote highly-rated products in recommendation sections.

<br><br>

📦 Monitor low-rated products and improve customer experience.

<br><br>

🚀 Use customer ratings together with reviews for better product ranking strategies.

</div>

""", unsafe_allow_html=True)

st.markdown("")

st.success("""

### 🎯 Final Conclusion

The Rating Analysis demonstrates that customer satisfaction on Amazon is generally very high.

Products with strong ratings and large numbers of customer reviews consistently perform better and build greater customer trust.

Monitoring customer ratings, review trends, and product quality enables businesses to improve customer experience, optimize product performance, and make better data-driven decisions.

""")

st.markdown("---")