# ==========================================================
# BUSINESS RECOMMENDATIONS
# PART A
# ==========================================================
import streamlit as st
from db_connection import load_products
st.set_page_config(
    page_title="Business Recommendations",
    page_icon="📈",
    layout="wide"
)
# ==========================================================
# LOAD DATA FROM SQLITE DATABASE
# ==========================================================

df = load_products()
#  existing Business Recommendations code
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

.intro-card{
background:white;
padding:25px;
border-radius:18px;
border-left:8px solid #FF9900;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
font-size:17px;
line-height:1.8;
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""

<div class="main-title">

📈 Business Recommendations

</div>

""", unsafe_allow_html=True)

st.markdown("""

<div class="intro-card">

<h3 style="color:#232F3E;">🎯 Overview</h3>

<p>

This section summarizes the major findings from the SmartCart Analytics
dashboard and provides practical business recommendations.

The recommendations are based on customer ratings, product pricing,
reviews, Best Seller performance, sustainability analysis,
delivery performance, and product popularity.

These insights help improve sales performance,
customer satisfaction, and business growth.

</p>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART B
# STRATEGIC BUSINESS RECOMMENDATIONS
# ==========================================================

st.markdown("""
<style>

.section-title{
background:linear-gradient(90deg,#146EB4,#232F3E);
padding:18px;
border-radius:15px;
text-align:center;
color:white;
font-size:28px;
font-weight:bold;
box-shadow:0px 8px 18px rgba(0,0,0,.20);
margin-bottom:25px;
}

.rec-card{
background:white;
padding:22px;
border-radius:18px;
border-top:6px solid #FF9900;
box-shadow:0px 6px 18px rgba(0,0,0,.15);
height:270px;
transition:0.3s;
margin-bottom:20px;
}

.rec-card:hover{
transform:translateY(-8px);
box-shadow:0px 12px 24px rgba(0,0,0,.25);
}

.rec-card h3{
color:#232F3E;
text-align:center;
margin-bottom:12px;
}

.rec-card p{
font-size:15px;
line-height:1.7;
text-align:justify;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""

<div class="section-title">

💡 Strategic Business Recommendations

</div>

""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# -----------------------
# Recommendation 1
# -----------------------

with col1:

    st.markdown("""

<div class="rec-card">

<h3>⭐ Improve Product Quality</h3>

<p>

Focus on improving products with ratings below 4.0.

Regularly analyze customer feedback and resolve quality issues.

Maintaining higher ratings increases customer trust and long-term sales.

</p>

</div>

""", unsafe_allow_html=True)

# -----------------------

with col2:

    st.markdown("""

<div class="rec-card">

<h3>📝 Encourage Customer Reviews</h3>

<p>

Invite verified buyers to leave product reviews.

Higher review counts improve customer confidence and increase product visibility.

Positive reviews also improve conversion rates.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================

col3, col4 = st.columns(2)

with col3:

    st.markdown("""

<div class="rec-card">

<h3>💰 Optimize Pricing Strategy</h3>

<p>

Use competitive pricing and seasonal discounts.

Monitor premium products separately and adjust prices according to customer demand.

Dynamic pricing helps maximize revenue.

</p>

</div>

""", unsafe_allow_html=True)

with col4:

    st.markdown("""

<div class="rec-card">

<h3>📦 Inventory Management</h3>

<p>

Maintain sufficient stock for products with high monthly purchases.

Reduce stock shortages by monitoring demand trends.

This improves customer satisfaction and avoids missed sales.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================

col5, col6 = st.columns(2)

with col5:

    st.markdown("""

<div class="rec-card">

<h3>🌱 Promote Sustainable Products</h3>

<p>

Increase products carrying Sustainability Badges.

Highlight eco-friendly products in marketing campaigns to attract environmentally conscious customers.

</p>

</div>

""", unsafe_allow_html=True)

with col6:

    st.markdown("""

<div class="rec-card">

<h3>🚚 Improve Delivery Experience</h3>

<p>

Expand same-day and next-day delivery services.

Faster delivery improves customer satisfaction, loyalty, and repeat purchases.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================

col7, col8 = st.columns(2)

with col7:

    st.markdown("""

<div class="rec-card">

<h3>🏆 Promote Best Sellers</h3>

<p>

Feature Best Seller products prominently on the homepage.

Use these products in advertisements and recommendation sections to maximize sales.

</p>

</div>

""", unsafe_allow_html=True)

with col8:

    st.markdown("""

<div class="rec-card">

<h3>📊 Data-Driven Decision Making</h3>

<p>

Use dashboard insights regularly to monitor pricing, customer engagement, reviews, and ratings.

Business intelligence enables faster and more informed strategic decisions.

</p>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART C
# IMPLEMENTATION ROADMAP
# ==========================================================

st.markdown("""
<style>

.roadmap-title{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:18px;

border-radius:15px;

text-align:center;

color:white;

font-size:28px;

font-weight:bold;

box-shadow:0px 8px 18px rgba(0,0,0,.25);

margin-bottom:25px;

}

.phase-card{

background:white;

padding:25px;

border-radius:18px;

border-top:8px solid #FF9900;

box-shadow:0px 6px 18px rgba(0,0,0,.15);

min-height: 430px;
height: auto;

transition:0.3s;

}

.phase-card:hover{

transform:translateY(-8px);

box-shadow:0px 12px 24px rgba(0,0,0,.25);

}

.phase-card h3{

text-align:center;

color:#232F3E;

margin-bottom:15px;

}

.phase-card ul{

line-height:2;

font-size:15px;

}

</style>
""", unsafe_allow_html=True)

st.markdown("""

<div class="roadmap-title">

🚀 Business Implementation Roadmap

</div>

""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# =======================================================
# Phase 1
# =======================================================

with col1:

    st.markdown("""

<div class="phase-card">

<h3>

🟢 Phase 1

<br>

Immediate Actions

</h3>

<ul>

<li>Improve low-rated products</li>

<li>Encourage verified customer reviews</li>

<li>Monitor customer ratings daily</li>

<li>Promote Best Seller products</li>

<li>Maintain stock for high-demand products</li>

</ul>

</div>

""", unsafe_allow_html=True)

# =======================================================
# Phase 2
# =======================================================

with col2:

    st.markdown("""

<div class="phase-card">

<h3>

🟡 Phase 2

<br>

Business Optimization

</h3>

<ul>

<li>Introduce dynamic pricing strategy</li>

<li>Improve delivery performance</li>

<li>Increase Buy Box availability</li>

<li>Expand sustainability-certified products</li>

<li>Enhance promotional campaigns</li>

</ul>

</div>

""", unsafe_allow_html=True)

# =======================================================
# Phase 3
# =======================================================

with col3:

    st.markdown("""

<div class="phase-card">

<h3>

🔵 Phase 3

<br>

Future Growth

</h3>

<ul>

<li>AI Product Recommendation System</li>

<li>Sales Forecasting using Machine Learning</li>

<li>Customer Sentiment Analysis</li>

<li>Real-Time Dashboard with APIs</li>

<li>Cloud-based Business Intelligence</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# IMPLEMENTATION SUMMARY
# ==========================================================

st.info("""

### 📌 Roadmap Summary

The implementation roadmap provides a structured approach for improving
customer satisfaction, increasing sales, optimizing pricing strategies,
enhancing sustainability initiatives, and supporting long-term business
growth through data-driven decision-making.

""")
# ==========================================================
# PART D
# EXPECTED BUSINESS BENEFITS
# ==========================================================

st.markdown("""
<style>

.benefit-title{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:18px;

border-radius:15px;

text-align:center;

color:white;

font-size:28px;

font-weight:bold;

box-shadow:0px 8px 18px rgba(0,0,0,.25);

margin-top:20px;

margin-bottom:25px;

}

.benefit-card{

background:white;

padding:22px;

border-radius:18px;

border-left:8px solid #FF9900;

box-shadow:0px 6px 18px rgba(0,0,0,.15);

height:240px;

transition:0.3s;

margin-bottom:20px;

}

.benefit-card:hover{

transform:translateY(-8px);

box-shadow:0px 12px 24px rgba(0,0,0,.25);

}

.benefit-card h3{

text-align:center;

color:#232F3E;

margin-bottom:12px;

}

.benefit-card p{

font-size:15px;

line-height:1.8;

text-align:justify;

}

.summary-box{

background:#F7FBFF;

padding:25px;

border-radius:18px;

border-left:8px solid #146EB4;

box-shadow:0px 6px 18px rgba(0,0,0,.15);

margin-top:25px;

line-height:1.9;

font-size:17px;

}

</style>
""", unsafe_allow_html=True)

st.markdown("""

<div class="benefit-title">

📊 Expected Business Benefits

</div>

""", unsafe_allow_html=True)

# =====================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""

<div class="benefit-card">

<h3>⭐ Customer Satisfaction</h3>

<p>

Improve customer satisfaction by maintaining high product ratings,
responding to customer feedback, and continuously improving product quality.

</p>

</div>

""", unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class="benefit-card">

<h3>💰 Revenue Growth</h3>

<p>

Optimize pricing strategies, promote Best Seller products,
and improve product visibility to increase sales and overall revenue.

</p>

</div>

""", unsafe_allow_html=True)

with col3:

    st.markdown("""

<div class="benefit-card">

<h3>📦 Inventory Efficiency</h3>

<p>

Analyze customer demand and purchase trends to maintain
optimal inventory levels and reduce stock shortages.

</p>

</div>

""", unsafe_allow_html=True)

# =====================================================

col4, col5, col6 = st.columns(3)

with col4:

    st.markdown("""

<div class="benefit-card">

<h3>🚚 Better Delivery</h3>

<p>

Improve delivery performance through faster shipping,
better logistics planning, and efficient order fulfillment.

</p>

</div>

""", unsafe_allow_html=True)

with col5:

    st.markdown("""

<div class="benefit-card">

<h3>🌱 Sustainability</h3>

<p>

Expand environmentally friendly products and increase
the adoption of sustainability badges to strengthen brand reputation.

</p>

</div>

""", unsafe_allow_html=True)

with col6:

    st.markdown("""

<div class="benefit-card">

<h3>📈 Data-Driven Decisions</h3>

<p>

Leverage dashboard insights to support smarter business decisions,
optimize product strategies, and improve long-term performance.

</p>

</div>

""", unsafe_allow_html=True)

# =====================================================

st.markdown("""

<div class="summary-box">

<h3 style="color:#146EB4;">

🎯 Expected Business Impact

</h3>

<ul>

<li>Increase customer trust through higher-rated products.</li>

<li>Boost sales by promoting high-performing products.</li>

<li>Improve inventory planning using purchase trends.</li>

<li>Strengthen pricing strategies through data analysis.</li>

<li>Enhance customer engagement with better reviews and recommendations.</li>

<li>Support sustainable business growth using Business Intelligence.</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("---")
# ==========================================================
# PART E
# FUTURE SCOPE & PROJECT CONCLUSION
# ==========================================================

st.markdown("""
<style>

.final-title{

background:linear-gradient(90deg,#146EB4,#232F3E);

padding:18px;

border-radius:15px;

text-align:center;

color:white;

font-size:28px;

font-weight:bold;

box-shadow:0px 8px 20px rgba(0,0,0,.20);

margin-bottom:25px;

}

.future-card{

background:white;

padding:22px;

border-radius:18px;

border-left:8px solid #FF9900;

box-shadow:0px 6px 18px rgba(0,0,0,.15);
min-height: 430px;
height: auto;

transition:.3s;

}

.future-card:hover{

transform:translateY(-8px);

box-shadow:0px 12px 24px rgba(0,0,0,.25);

}

.conclusion{

background:#F8FBFF;

padding:30px;

border-radius:18px;

border-left:8px solid #146EB4;

box-shadow:0px 6px 18px rgba(0,0,0,.18);

margin-top:30px;

font-size:16px;

line-height:1.9;

}

.end-box{

background:linear-gradient(90deg,#232F3E,#146EB4);

padding:25px;

border-radius:18px;

text-align:center;

color:white;

font-size:24px;

font-weight:bold;

margin-top:35px;

box-shadow:0px 8px 20px rgba(0,0,0,.20);

}

</style>
""", unsafe_allow_html=True)

st.markdown("""

<div class="final-title">

🚀 Future Scope & Project Conclusion

</div>

""", unsafe_allow_html=True)

# =======================================================

col1,col2=st.columns(2)

with col1:

    st.markdown("""

<div class="future-card">

<h3 style="color:#232F3E;text-align:center;">

🔮 Future Scope

</h3>

<ul>

<li>Build an AI-based Product Recommendation System.</li>

<li>Develop Machine Learning models for Sales Forecasting.</li>

<li>Perform Customer Sentiment Analysis using Review Text.</li>

<li>Integrate Live Amazon Product Data using APIs.</li>

<li>Deploy the dashboard on Streamlit Cloud.</li>

<li>Create Executive KPI Dashboards.</li>

<li>Use Cloud platforms for Big Data Analytics.</li>

<li>Implement Predictive Analytics for business growth.</li>

</ul>

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class="future-card">

<h3 style="color:#232F3E;text-align:center;">

🎯 Project Achievement

</h3>

<ul>

<li>Successfully cleaned and prepared Amazon product data.</li>

<li>Performed complete Exploratory Data Analysis (EDA).</li>

<li>Created professional interactive Plotly dashboards.</li>

<li>Generated meaningful business insights.</li>

<li>Analyzed pricing, ratings, reviews, delivery, and sustainability.</li>

<li>Designed a professional multi-page Streamlit application.</li>

<li>Supported business decision-making using data analytics.</li>

</ul>

</div>

""",unsafe_allow_html=True)

# =======================================================

st.markdown("""

<div class="conclusion">

<h2 style="color:#146EB4;">

📋 Project Conclusion

</h2>

<p>

The <b>SmartCart Analytics Dashboard</b> demonstrates how Data Analytics
can transform raw Amazon product data into meaningful business insights.

Using <b>Python, Pandas, NumPy, Plotly, Matplotlib, Seaborn, and
Streamlit</b>, the project successfully analyzed customer ratings,
pricing strategies, customer reviews, product popularity,
delivery performance, sustainability initiatives, and buying trends.

The dashboard enables businesses to make smarter decisions related to
pricing, inventory management, customer satisfaction, and product
performance through interactive visualizations and data-driven insights.

Overall, this project highlights the practical application of Business
Intelligence and Data Science techniques for improving e-commerce
performance and supporting strategic business growth.

</p>

</div>

""",unsafe_allow_html=True)

# =======================================================

st.markdown("""

<div class="end-box">

🎉 Thank You for Exploring SmartCart Analytics Dashboard

<br><br>

Turning Amazon Product Data into Actionable Business Intelligence 📊

</div>

""",unsafe_allow_html=True)

st.balloons()

st.markdown("---")