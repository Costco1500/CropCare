import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Plant Disease Detection", layout="centered")

# --- STYLING THE PAGE ---
st.markdown(
    """
    <style>
    /* Set the background color to white */
    .stApp {
        background-color: white;
        color: black; /* Change text color to black for contrast */
    }
    /* Styling the main title */
    .title h1 {
        font-size: 3em;
        text-align: center;
        color: #333; /* Darker color for better contrast on white background */
        margin-bottom: 20px;
    }
    /* Subtitle Styling */
    .subheader {
        font-size: 1.5em;
        margin-top: 20px;
        margin-bottom: 10px;
        color: #008000; /* Green color for subtitles */
    }
    /* Paragraphs */
    p {
        font-size: 1.1em;
        line-height: 1.6;
        color: #333; /* Darker text for better readability */
    }
    /* List items */
    ul {
        margin-left: 20px;
        margin-top: 10px;
        list-style-type: "✔️";
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- HERO SECTION ---
st.markdown('<div class="title">', unsafe_allow_html=True)
st.image("/Users/chi/Plant-Disease-Detection/logo-png.webp", width=250)
st.title("🌿 CropCare 🌿")
st.write("Something about crops here")
st.markdown('</div>', unsafe_allow_html=True)

# --- EXPERIENCE & QUALIFICATIONS ---
st.markdown('<div class="subheader">Future Goals</div>', unsafe_allow_html=True)
st.write(
    """
    - **🌾 Increased Crop Yields and Food Security**: Early detection of plant diseases allows farmers to take swift action, preventing the spread of diseases and minimizing crop losses.
    - **🚜 Reduced Use of Pesticides**: With accurate disease detection, farmers can target specific plants or areas that are affected, rather than applying pesticides broadly.
    - **💰 Cost Savings for Farmers**: Detecting plant diseases early helps farmers avoid the high costs associated with treating widespread outbreaks or replacing lost crops.
    - **🥗 Improved Public Health and Nutrition**: Healthy plants produce more nutritious food. By preventing plant diseases, the community benefits from a higher quality of fruits, vegetables, and grains.
    """
)

# --- ABOUT US ---
st.markdown('<div class="subheader">About Us</div>', unsafe_allow_html=True)
st.write(
    """
    🌱 We are a group of high schoolers passionate about improving agriculture using the future of technology for a better and sustainable future!
    """
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
