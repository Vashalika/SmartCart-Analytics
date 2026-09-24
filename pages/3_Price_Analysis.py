import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from db_connection import load_products
# ===========================
# AMAZON THEME COLORS
# ===========================

AMAZON_ORANGE = "#FF9900"
AMAZON_BLUE = "#146EB4"
AMAZON_NAVY = "#232F3E"
LIGHT_BG = "#F7F9FC"
CARD_BG = "#FFFFFF"
TEXT = "#2D3436"

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Price Analysis",
    page_icon="💰",
    layout="wide"
)

# -------------------------------------------------------
# LOAD DATA
# -------------------------------------------------------

df = load_products()

df["current/discounted_price"] = pd.to_numeric(
    df["current/discounted_price"],
    errors="coerce"
)

df = df.dropna(subset=["current/discounted_price"])
# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#F7F9FC;
}

h1,h2,h3{
    color:#232F3E;
}

.card{
    background:white;
    padding:18px;
    border-radius:15px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.15);
    text-align:center;
}

.metric{
    font-size:34px;
    font-weight:bold;
    color:#FF9900;
}

.label{
    font-size:18px;
    color:gray;
}

.summary{
    background:#232F3E;
    color:white;
    border-radius:15px;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.markdown("""
# 💰 Price Analysis Dashboard

Analyze Amazon India product pricing, identify expensive products,
and explore pricing trends interactively using Indian Rupees (₹).
""")

st.markdown("---")

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

st.sidebar.title("🎛 Filters")

price_range = st.sidebar.slider(
    "Price Range (₹)",
    float(df["current/discounted_price"].min()),
    float(df["current/discounted_price"].max()),
    (
        float(df["current/discounted_price"].min()),
        float(df["current/discounted_price"].max())
    )
)

rating = st.sidebar.slider(
    "Minimum Rating",
    0.0,
    5.0,
    4.0,
    0.1
)

filtered_df = df[
    (df["current/discounted_price"] >= price_range[0]) &
    (df["current/discounted_price"] <= price_range[1]) &
    (df["rating"] >= rating)
]

# -------------------------------------------------------
# KPI VALUES
# -------------------------------------------------------

avg_price = filtered_df["current/discounted_price"].mean()

max_price = filtered_df["current/discounted_price"].max()

min_price = filtered_df["current/discounted_price"].min()

products = len(filtered_df)

# -------------------------------------------------------
# KPI CARDS
# -------------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
<div class="card">
<div class="label">💲 Average Price</div>
<div class="metric">₹ {avg_price:,.2f}</div>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown(f"""
<div class="card">
<div class="label">📈 Highest Price</div>
<div class="metric">₹ {max_price:,.2f}</div>
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown(f"""
<div class="card">
<div class="label">📉 Lowest Price</div>
<div class="metric">₹ {min_price:,.2f}</div>
</div>
""", unsafe_allow_html=True)

with c4:
    st.markdown(f"""
<div class="card">
<div class="label">📦 Products</div>
<div class="metric">{products:,}</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# -------------------------------------------------------
# TWO COLUMN LAYOUT
# -------------------------------------------------------

left, right = st.columns([2,1])

# -------------------------------------------------------
# AVERAGE PRICE GAUGE CHART
# -------------------------------------------------------

with left:

    st.subheader("📈 Average Price Gauge")

    gauge = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=avg_price,

            number={
                "prefix":"₹ ",
                "valueformat":",.2f"
            },

            title={
                "text":"Average Price (₹)"
            },

            gauge={

                "axis":{
                    "range":[0,max_price]
                },

                "bar":{
                    "color":"#FF9900"
                },

                "steps":[

                    {
                        "range":[0,max_price*0.50],
                        "color":"#d4edda"
                    },

                    {
                        "range":[max_price*0.50,max_price*0.80],
                        "color":"#ffeeba"
                    },

                    {
                        "range":[max_price*0.80,max_price],
                        "color":"#f8d7da"
                    }

                ]

            }

        )
    )

    gauge.update_layout(
        height=450,
        margin=dict(l=20,r=20,t=50,b=20)
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

# -------------------------------------------------------
# SUMMARY PANEL
# -------------------------------------------------------

with right:

    st.markdown("""
<div class="summary">

<h3>📋 Quick Summary</h3>

<ul>

<li>Interactive Price Dashboard</li>

<li>Average Product Price (₹)</li>

<li>Highest & Lowest Product Price</li>

<li>Dynamic Price Filters</li>

<li>Professional KPI Cards</li>

<li>Interactive Gauge Visualization</li>

</ul>

</div>
""", unsafe_allow_html=True)

    st.write("")

    st.info(f"""

### 📦 Selected Products

**{products:,} Products**

Matching your selected filters.

""")

# -------------------------------------------------------
# PRICE SUMMARY TABLE
# -------------------------------------------------------

st.markdown("---")

st.subheader("📋 Price Summary")

summary = filtered_df[[
    "title",
    "current/discounted_price",
    "rating",
    "number_of_reviews"
]].sort_values(
    by="current/discounted_price",
    ascending=False
)

st.dataframe(
    summary,
    use_container_width=True,
    height=500
)

st.success("""
✅ Price Analysis Completed Successfully

The dashboard provides insights into:

✔ Product Pricing

✔ Price Distribution

✔ Highest Priced Products

✔ Interactive Price Filters

✔ KPI Summary

✔ Professional Business Insights
""")
    # ==========================================================
# 💰 PART A : LISTED PRICE vs CURRENT PRICE
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#146EB4,#FF9900);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0px 6px 18px rgba(0,0,0,.20);
margin-top:20px;
margin-bottom:25px;
">

<h2>💰 Listed Price vs Current Price</h2>

<p style="font-size:17px;">
Compare Original Product Price with Current Discounted Price
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# DATA
# ----------------------------------------------------------

price_df = filtered_df.copy()

price_df = price_df.dropna(
    subset=[
        "listed_price",
        "current/discounted_price"
    ]
)

# ----------------------------------------------------------
# SCATTER CHART
# ----------------------------------------------------------

fig = px.scatter(

    price_df,

    x="listed_price",

    y="current/discounted_price",

    color="rating",

    hover_data=[
        "title"
    ],

    opacity=0.70,

    color_continuous_scale="Turbo",

    title="Listed Price vs Current Price"

)

fig.update_layout(

    template="plotly_white",

    width=1300,

    height=750,

    title=dict(

        x=0.5,

        font=dict(size=24)

    ),

    xaxis_title="Listed Price ($)",

    yaxis_title="Current / Discounted Price ($)",

    font=dict(size=15)

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
background:white;
padding:22px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.12);
border-left:7px solid #146EB4;
margin-top:20px;
">

<h3>📊 Graph Overview</h3>

<p style="font-size:16px;line-height:1.9;color:#333;">

Each point represents an Amazon product.

The X-axis shows the original listed price,
while the Y-axis represents the current discounted price.

Different colors indicate customer ratings,
making it easier to compare pricing with product quality.

</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# BUSINESS INSIGHTS
# ----------------------------------------------------------

st.markdown("""
<div style="
background:white;
padding:22px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.12);
border-left:7px solid #FF9900;
margin-top:20px;
margin-bottom:25px;
">

<h3>💡 Business Insights</h3>

<ul style="font-size:16px;line-height:2;color:#333;">

<li>💰 Most products are sold below their listed price through discounts.</li>

<li>📈 Competitive pricing helps attract more customers.</li>

<li>⭐ Higher-rated products are available across different price ranges.</li>

<li>🛒 Premium-priced products form a smaller portion of the catalog.</li>

<li>🎯 Price comparison helps businesses evaluate discount strategies and market positioning.</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# 💰 PART B : CURRENT PRICE DISTRIBUTION
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#FF9900,#00B894);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0px 6px 18px rgba(0,0,0,.20);
margin-top:20px;
margin-bottom:25px;
">

<h2>💰 Current Price Distribution</h2>

<p style="font-size:17px;">
Distribution of Current / Discounted Product Prices
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# BOX PLOT
# ----------------------------------------------------------

fig = px.box(

    filtered_df,

    y="current/discounted_price",

    color_discrete_sequence=["mediumseagreen"],

    title="Current Price Distribution",

    template="plotly_white"

)

fig.update_layout(

    title=dict(
        x=0.5,
        font=dict(size=24)
    ),

    width=1300,

    height=720,

    yaxis_title="Current Price ($)",

    font=dict(size=15)

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
background:white;
padding:22px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.12);
border-left:7px solid #00B894;
margin-top:20px;
">

<h3>📊 Graph Overview</h3>

<p style="font-size:16px;line-height:1.8;color:#333;">

The Box Plot illustrates the overall distribution of current product prices.

It highlights the median price, price spread, interquartile range (IQR),
and identifies unusually high or low-priced products as outliers.

</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# BUSINESS INSIGHTS
# ----------------------------------------------------------

st.markdown("""
<div style="
background:white;
padding:22px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.12);
border-left:7px solid #FF9900;
margin-top:20px;
margin-bottom:25px;
">

<h3>💡 Business Insights</h3>

<ul style="font-size:16px;line-height:2;color:#333;">

<li>💰 Most Amazon products are concentrated in the low-to-medium price range.</li>

<li>📦 A few premium products appear as outliers with significantly higher prices.</li>

<li>🛍️ Competitive pricing improves product accessibility for customers.</li>

<li>📈 The price spread helps businesses understand overall pricing strategy.</li>

<li>🎯 Identifying price outliers supports better pricing and promotional decisions.</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# 💰 PART C : PRICE ON VARIANT DISTRIBUTION
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#00B894,#146EB4);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0px 6px 18px rgba(0,0,0,.20);
margin-top:20px;
margin-bottom:25px;
">

<h2>🎻 Price on Variant Distribution</h2>

<p style="font-size:17px;">
Analyze the Distribution of Product Variant Prices
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# DATA
# ----------------------------------------------------------

variant_df = filtered_df.dropna(subset=["price_on_variant"])

# ----------------------------------------------------------
# VIOLIN PLOT
# ----------------------------------------------------------

fig = px.violin(

    variant_df,

    y="price_on_variant",

    box=True,

    points=False,

    color_discrete_sequence=["mediumseagreen"],

    template="plotly_white",

    title="Price on Variant Distribution"

)

fig.update_layout(

    title=dict(
        x=0.5,
        font=dict(size=24)
    ),

    width=1300,

    height=720,

    yaxis_title="Price on Variant ($)",

    font=dict(size=15)

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
background:white;
padding:22px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.12);
border-left:7px solid #146EB4;
margin-top:20px;
">

<h3>📊 Graph Overview</h3>

<p style="font-size:16px;line-height:1.9;color:#333;">

The violin plot combines a box plot with a density curve to illustrate the
distribution of product variant prices.

The wider sections indicate price ranges where more products are concentrated,
while the embedded box plot displays the median and interquartile range (IQR).

This visualization makes it easier to understand pricing variation across
different product variants.

</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# BUSINESS INSIGHTS
# ----------------------------------------------------------

st.markdown("""
<div style="
background:white;
padding:22px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.12);
border-left:7px solid #00B894;
margin-top:20px;
margin-bottom:25px;
">

<h3>💡 Business Insights</h3>

<ul style="font-size:16px;line-height:2;color:#333;">

<li>🎻 Most product variants are concentrated within a specific price range.</li>

<li>💰 Premium-priced variants are relatively fewer and appear as outliers.</li>

<li>📦 Price variation reflects differences in product models, configurations, and features.</li>

<li>🛍️ Understanding variant pricing helps businesses design competitive pricing strategies.</li>

<li>📈 This analysis supports better product positioning and inventory planning.</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# 📊 PART D : PRICE ANALYSIS SUMMARY
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

<h2>📊 Price Analysis Summary</h2>

<p style="font-size:17px;">
Key Findings from Amazon Product Pricing Analysis
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# SUMMARY
# ----------------------------------------------------------

st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.12);
border-left:7px solid #146EB4;
">

<h3>📌 Summary</h3>

<p style="font-size:16px;line-height:1.9;color:#333;">

The pricing analysis provides a clear understanding of how Amazon products
are priced across different categories. By comparing listed prices,
discounted prices, and variant prices, businesses can better understand
pricing strategies, identify premium products, and evaluate the impact of
discounts on customer purchasing decisions.

</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# KEY FINDINGS
# ----------------------------------------------------------

st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.12);
border-left:7px solid #FF9900;
margin-top:20px;
">

<h3>📈 Key Findings</h3>

<ul style="font-size:16px;line-height:2;color:#333;">

<li>💰 Most products are available at discounted prices.</li>

<li>🛒 Affordable and mid-range products dominate the marketplace.</li>

<li>🎻 Product variants show noticeable price differences based on features.</li>

<li>📦 Only a limited number of products belong to the premium price segment.</li>

<li>📈 Pricing strategies play an important role in improving product competitiveness.</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# 🎯 PART E : BUSINESS RECOMMENDATIONS & CONCLUSION
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#FF9900,#146EB4);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0px 6px 18px rgba(0,0,0,.20);
margin-top:20px;
margin-bottom:25px;
">

<h2>🚀 Business Recommendations</h2>

<p style="font-size:17px;">
Strategic Pricing Recommendations Based on Product Analysis
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# BUSINESS RECOMMENDATIONS
# ----------------------------------------------------------

st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.12);
border-left:7px solid #FF9900;
">

<h3>💡 Business Recommendations</h3>

<ul style="font-size:16px;line-height:2;color:#333;">

<li>💰 Maintain competitive pricing to attract more customers.</li>

<li>🏷️ Offer discounts on selected products to increase sales.</li>

<li>📦 Focus inventory on products with strong customer demand.</li>

<li>⭐ Promote highly rated products through featured listings.</li>

<li>🎯 Monitor premium-priced products and adjust pricing based on market trends.</li>

<li>📈 Regularly analyze pricing data to improve business performance.</li>

</ul>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# CONCLUSION
# ----------------------------------------------------------

st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.12);
border-left:7px solid #146EB4;
margin-top:20px;
">

<h3>📌 Conclusion</h3>

<p style="font-size:16px;line-height:1.9;color:#333;">

The Price Analysis Dashboard provides valuable insights into Amazon product pricing,
discount strategies, and product value. By analyzing listed prices, discounted prices,
and variant pricing, businesses can understand pricing patterns, improve product
positioning, and make better pricing decisions.

These insights support data-driven strategies that enhance customer satisfaction,
increase sales performance, and strengthen overall business competitiveness.

</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# SUCCESS MESSAGE
# ----------------------------------------------------------

st.success("✅ Price Analysis Completed Successfully!")

st.info("""
This dashboard helps businesses understand pricing behavior,
optimize discounts, and improve product pricing strategies
using interactive visualizations and business insights.
""")

st.markdown("---")