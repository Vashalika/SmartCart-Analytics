import streamlit as st
import pandas as pd
import sqlite3

# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="Database | SmartCart Analytics",
    page_icon="🗄️",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #eef6ff 0%,
        #ffffff 50%,
        #fff4e6 100%
    );
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* HEADER */

.database-header {
    background: linear-gradient(
        135deg,
        #1565c0,
        #4527a0,
        #7b1fa2
    );
    padding: 32px;
    border-radius: 22px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.18);
}

.database-header h1 {
    color: white;
    font-size: 38px;
    margin: 0 0 8px 0;
}

.database-header p {
    color: white;
    font-size: 17px;
    margin: 0;
    opacity: 0.9;
}

/* SECTION TITLE */

.section-title {
    background: linear-gradient(
        90deg,
        #1976d2,
        #7b1fa2
    );
    color: white;
    padding: 15px 22px;
    border-radius: 14px;
    font-size: 22px;
    font-weight: 700;
    margin-top: 28px;
    margin-bottom: 18px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.12);
}

/* CONNECTION */

.status-box {
    background: linear-gradient(
        135deg,
        #e8f5e9,
        #f1f8e9
    );
    border-left: 7px solid #2e7d32;
    padding: 18px 22px;
    border-radius: 14px;
    color: #1b5e20;
    font-size: 17px;
    font-weight: 600;
    margin-bottom: 25px;
}

/* INFORMATION CARD */

.info-card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    border-left: 7px solid #1976d2;
    box-shadow: 0 7px 20px rgba(0,0,0,0.10);
    min-height: 170px;
}

.info-card h3 {
    color: #1565c0;
    font-size: 21px;
    margin-top: 0;
}

.info-card p {
    color: #555;
    font-size: 15px;
    line-height: 1.7;
}

/* METRIC CARDS */

.metric-card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 7px 20px rgba(0,0,0,0.10);
    border-top: 6px solid #1976d2;
}

.metric-icon {
    font-size: 34px;
}

.metric-value {
    font-size: 30px;
    font-weight: 700;
    color: #1565c0;
    margin: 8px 0;
}

.metric-label {
    color: #666;
    font-size: 15px;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #666;
    margin-top: 45px;
    padding: 20px;
    border-top: 1px solid #ddd;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# MAIN HEADER
# IMPORTANT: HTML TAGS START FROM LEFT SIDE
# =====================================================

st.markdown("""
<div class="database-header">
<h1>🗄️ SmartCart Database</h1>
<p>SQLite Database Management & Product Data Explorer</p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# DATABASE
# =====================================================

DATABASE_FILE = "smartcart.db"

try:

    conn = sqlite3.connect(
        DATABASE_FILE,
        check_same_thread=False
    )

    # =================================================
    # CONNECTION STATUS
    # =================================================

    st.markdown("""
<div class="status-box">
🟢 SQLite Database Connected Successfully!
</div>
""", unsafe_allow_html=True)


    # =================================================
    # DATABASE TABLES
    # =================================================

    st.markdown("""
<div class="section-title">
📋 Database Tables
</div>
""", unsafe_allow_html=True)

    tables = pd.read_sql_query(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        """,
        conn
    )

    col1, col2 = st.columns([1.5, 1])

    with col1:

        st.dataframe(
            tables,
            use_container_width=True,
            hide_index=True
        )

    with col2:

        st.markdown("""
<div class="info-card">
<h3>📁 Database Information</h3>
<p>
This section displays the tables available
inside the SmartCart SQLite database.
</p>
<p>
The main product information is stored
in the <b>products</b> table.
</p>
</div>
""", unsafe_allow_html=True)


    # =================================================
    # PRODUCT STATISTICS
    # =================================================

    st.markdown("""
<div class="section-title">
📊 Product Database Statistics
</div>
""", unsafe_allow_html=True)

    count = pd.read_sql_query(
        """
        SELECT COUNT(*) AS total_records
        FROM products
        """,
        conn
    )

    total_records = int(count.iloc[0]["total_records"])

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(f"""
<div class="metric-card">
<div class="metric-icon">📦</div>
<div class="metric-value">{total_records:,}</div>
<div class="metric-label">Total Product Records</div>
</div>
""", unsafe_allow_html=True)

    with col2:

        st.markdown("""
<div class="metric-card">
<div class="metric-icon">🗄️</div>
<div class="metric-value">SQLite</div>
<div class="metric-label">Database Engine</div>
</div>
""", unsafe_allow_html=True)

    with col3:

        st.markdown("""
<div class="metric-card">
<div class="metric-icon">⚡</div>
<div class="metric-value">Active</div>
<div class="metric-label">Database Status</div>
</div>
""", unsafe_allow_html=True)


    # =================================================
    # PRODUCT PREVIEW
    # =================================================

    st.markdown("""
<div class="section-title">
🔍 Product Data Preview
</div>
""", unsafe_allow_html=True)

    preview = pd.read_sql_query(
        """
        SELECT *
        FROM products
        LIMIT 10
        """,
        conn
    )

    st.dataframe(
        preview,
        use_container_width=True,
        hide_index=True
    )


    # =================================================
    # ABOUT DATABASE
    # =================================================

    st.markdown("""
<div class="info-card">
<h3>💡 About SmartCart Database</h3>
<p>
The SmartCart Analytics database stores Amazon
e-commerce product information in a structured
SQLite database.
</p>
<p>
The dashboard uses this database to retrieve
product records and display analytical insights
across different dashboard pages.
</p>
</div>
""", unsafe_allow_html=True)


    conn.close()


except Exception as e:

    st.error(
        f"❌ Database connection failed: {e}"
    )


# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">
🛒 <b>SmartCart Analytics</b>
&nbsp;•&nbsp;
Amazon E-Commerce Product Insights Dashboard
</div>
""", unsafe_allow_html=True)