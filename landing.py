import streamlit as st


# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="SmartCart Analytics",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =====================================================
# SESSION STATE
# =====================================================

if "explored" not in st.session_state:
    st.session_state.explored = False


# =====================================================
# CSS
# =====================================================

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #eef5ff,
            #ffffff,
            #fff4e6
        );
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .block-container {
        padding-top: 45px;
        max-width: 1150px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =====================================================
# LANDING PAGE
# =====================================================

def landing_page():

    st.markdown("# 🛒 SmartCart Analytics")

    st.markdown(
        "## Amazon E-Commerce Product Insights Dashboard"
    )

    st.write(
        "Explore product performance, pricing, ratings, "
        "sales trends and business recommendations."
    )

    st.divider()


    # =================================================
    # WELCOME
    # =================================================

    st.markdown("### 🚀 Explore Dashboard")

    st.write(
        "Would you like to explore the SmartCart Analytics "
        "dashboard?"
    )

    st.divider()


    # =================================================
    # YES / NO BUTTONS
    # =================================================

    col1, col2 = st.columns(2)


    # ---------------- YES ----------------

    with col1:

        if st.button(
            "✅ Yes, Explore Dashboard",
            use_container_width=True
        ):

            st.session_state.explored = True

            # Re-run the app and open dashboard navigation
            st.rerun()


    # ---------------- NO ----------------

    with col2:

        if st.button(
            "❌ No, Stay on Home",
            use_container_width=True
        ):

            st.session_state.explored = False

            st.info(
                "No problem! You can explore the dashboard "
                "whenever you are ready."
            )


    # =================================================
    # FEATURE CARDS
    # =================================================

    st.divider()

    st.markdown("### 📊 Dashboard Features")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.info(
            "📦 **Product Analysis**\n\n"
            "Explore product performance and categories."
        )


    with col2:

        st.success(
            "💰 **Price Analysis**\n\n"
            "Analyze product prices and pricing patterns."
        )


    with col3:

        st.warning(
            "📈 **Sales Insights**\n\n"
            "Discover important sales trends."
        )


    col4, col5, col6 = st.columns(3)


    with col4:

        st.info(
            "⭐ **Rating Analysis**\n\n"
            "Understand ratings and customer reviews."
        )


    with col5:

        st.success(
            "💡 **Business Recommendations**\n\n"
            "Get useful business insights."
        )


    with col6:

        st.warning(
            "🗄️ **SQLite Database**\n\n"
            "Explore data stored in the database."
        )


    # =================================================
    # FOOTER
    # =================================================

    st.write("")

    st.caption(
        "🛒 SmartCart Analytics • "
        "Amazon E-Commerce Product Insights Dashboard"
    )


# =====================================================
# DASHBOARD PAGES
# =====================================================

all_pages = [

    st.Page(
        "pages/1_home.py",
        title="Home",
        icon="🏠"
    ),

    st.Page(
        "pages/2_Dataset_Overview.py",
        title="Dataset Overview",
        icon="📋"
    ),

    st.Page(
        "pages/3_Price_Analysis.py",
        title="Price Analysis",
        icon="💰"
    ),

    st.Page(
        "pages/4_Product_Analysis.py",
        title="Product Analysis",
        icon="📦"
    ),

    st.Page(
        "pages/5_Rating_Analysis.py",
        title="Rating Analysis",
        icon="⭐"
    ),
    st.Page(
            "pages/6_Sales_Insights.py",
            title="Sales Insights",
            icon="📈"
        ),

    st.Page(
        "pages/7_EDA_analysis.py",
        title="EDA Analysis",
        icon="📊"
    ),

    st.Page(
        "pages/8_Business_Recommendations.py",
        title="Business Recommendations",
        icon="💡"
    ),

    st.Page(
        "pages/9_database.py",
        title="SQLite Database",
        icon="🗄️"
    )
]


# =====================================================
# NAVIGATION
# =====================================================

if st.session_state.explored:

    # =============================================
    # AFTER YES
    # =============================================

    pg = st.navigation(
        all_pages,
        position="sidebar",
        expanded=True
    )

else:

    # =============================================
    # BEFORE YES
    # =============================================

    pg = st.navigation(
        [
            st.Page(
                landing_page,
                title="Welcome",
                icon="🛒"
            )
        ],
        position="hidden"
    )

# =====================================================
# RUN CURRENT PAGE
# =====================================================

pg.run()