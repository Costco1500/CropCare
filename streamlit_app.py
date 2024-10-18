import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    "about_me.py",
    title="Home Page",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "app.py",
    title="Disease Detection",
    icon="🔎",
)
cause_effect_page = st.Page(
    "cause_effect.py",
    title="Causes & Effects",
    icon=":material/info:",
)
crop_journal_page = st.Page(
    "crop_journal.py",
    title="Crop Health Tracker",
    icon="📝",  # Use a valid single character emoji
)
crop_dashboard_page = st.Page(
    "crop_dashboard.py",
    title="Crop Analytics",
    icon ="📊",
)



# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Tools": [project_1_page, cause_effect_page, crop_journal_page, crop_dashboard_page,],
    }
)

# --- RUN NAVIGATION ---
pg.run()
