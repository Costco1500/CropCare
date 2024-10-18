import streamlit as st
import pandas as pd
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Crop Health Tracker", layout="centered")

# --- FUNCTION TO LOAD AND SAVE DATA ---
DATA_FILE = "crop_journal.csv"

def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Crop Type", "Notes", "Health Status"])

def save_data(data):
    data.to_csv(DATA_FILE, index=False)

# --- LOAD EXISTING DATA ---
data = load_data()

# --- SIDEBAR FORM FOR DATA ENTRY ---
st.sidebar.header("Add New Entry")
with st.sidebar.form(key='entry_form'):
    date = st.date_input("Date", datetime.today())
    crop_type = st.text_input("Crop Type (e.g., Tomato, Wheat)")
    health_status = st.selectbox("Health Status", ["Healthy", "Needs Attention", "Diseased"])
    notes = st.text_area("Notes (e.g., watering schedule, disease symptoms, etc.)")

    submit_button = st.form_submit_button(label="Add Entry")

# --- ADDING NEW ENTRY TO DATAFRAME ---
if submit_button:
    # Create a new row for the journal
    new_row = pd.DataFrame({
        "Date": [date],
        "Crop Type": [crop_type],
        "Notes": [notes],
        "Health Status": [health_status]
    })

    # Use pd.concat to add the new row to the existing data
    data = pd.concat([data, new_row], ignore_index=True)

    # Save updated data
    save_data(data)
    st.sidebar.success("New entry added successfully!")

# --- MAIN PAGE DISPLAY ---
st.title("🌿 Crop Health Tracker/Journal")
st.write("Keep track of your crops' health by adding daily entries and observations.")

# --- DISPLAY TABLE OF ENTRIES ---
st.subheader("Your Crop Journal Entries")
if not data.empty:
    st.dataframe(data)
else:
    st.write("No entries yet! Use the form on the left to add new entries.")

# --- FILTER SECTION ---
st.subheader("Filter Journal Entries")
with st.expander("Filter by Crop Type or Health Status"):
    # Crop Type filter
    crop_types = data["Crop Type"].unique()
    selected_crop = st.selectbox("Select Crop Type", ["All"] + list(crop_types))

    # Health Status filter
    health_statuses = data["Health Status"].unique()
    selected_health_status = st.selectbox("Select Health Status", ["All"] + list(health_statuses))

    # Filtering the data based on user selection
    filtered_data = data
    if selected_crop != "All":
        filtered_data = filtered_data[filtered_data["Crop Type"] == selected_crop]
    if selected_health_status != "All":
        filtered_data = filtered_data[filtered_data["Health Status"] == selected_health_status]

    st.dataframe(filtered_data)

# --- DELETE OR EXPORT SECTION ---
st.subheader("Manage Entries")
with st.expander("Delete All Entries or Export Data"):
    delete_button = st.button("Delete All Entries")
    export_button = st.button("Export Data as CSV")

    # Delete all entries
    if delete_button:
        data = data[0:0]
        save_data(data)
        st.success("All entries deleted successfully!")

    # Export data as CSV
    if export_button:
        st.download_button(
            label="Download CSV",
            data=data.to_csv(index=False),
            file_name="crop_journal.csv",
            mime="text/csv",
        )

# --- SIDEBAR ---
st.sidebar.header("Navigation")
st.sidebar.write("Use the sidebar to navigate different sections of the app.")
st.sidebar.image("/Users/chi/Plant-Disease-Detection/logo-png.webp", width=100)

# Footer Styling
st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    .footer-text {
        font-size: 0.8em;
        text-align: center;
        color: #333; /* Dark text for contrast on white background */
        margin-top: 50px;
    }
    </style>
    <div class="footer-text">
        Built with ❤️ by passionate students of Florida.
    </div>
    """,
    unsafe_allow_html=True
)
