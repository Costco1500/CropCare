import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Causes and Effects of Plant Diseases", layout="centered")

# --- PAGE TITLE ---
st.title("🌿 Causes and Effects of Leaf/Plant Diseases 🌿")

# --- RUST DISEASE SECTION ---
st.header("🌱 Rust Disease")
st.subheader("Causes:")
st.write("""
- **Fungal Pathogens**: Caused by a group of fungi known as 'rust fungi' (Puccinia species).
- **Moisture and Humidity**: Thrives in warm, moist conditions; water on leaves facilitates spore germination.
- **Weak Plant Health**: Weak plants or those under stress (drought, poor soil) are more susceptible.
""")

st.subheader("Effects:")
st.write("""
- **Yellow-Orange Spots**: Rust-colored pustules appear on the underside of leaves, stems, and flowers.
- **Reduced Photosynthesis**: Infected leaves often have reduced chlorophyll, which limits the plant's ability to produce food.
- **Defoliation and Yield Loss**: Severe infections can cause premature leaf drop, resulting in yield loss and reduced quality.
""")

# --- SCAB DISEASE SECTION ---
st.header("🍏 Scab Disease")
st.subheader("Causes:")
st.write("""
- **Fungal Infection**: Mainly caused by the fungus *Venturia inaequalis*.
- **Wet and Cool Weather**: Spores require wet and cool conditions to germinate and infect plants.
- **Poor Air Circulation**: Dense foliage or overcrowded planting can create a humid environment favorable for scab development.
""")

st.subheader("Effects:")
st.write("""
- **Lesions on Fruits and Leaves**: Circular, dark, and sunken spots develop on leaves, fruits, and stems.
- **Deformation and Cracking**: Affected fruits may become deformed, crack, and are often not suitable for sale or consumption.
- **Reduced Photosynthesis and Growth**: Infected leaves have reduced photosynthetic capacity, impairing growth and overall plant health.
""")

# --- MULTIPLE DISEASES SECTION ---
st.header("🌾 Multiple Diseases")
st.subheader("Causes:")
st.write("""
- **Combination of Pathogens**: Multiple diseases can be caused by a combination of bacteria, fungi, and viruses.
- **Environmental Stress**: Drought, extreme temperatures, poor soil nutrition can increase the likelihood of multiple diseases.
- **Weak Plant Immunity**: Plants with low immunity due to stress or improper care are more prone to infections.
""")

st.subheader("Effects:")
st.write("""
- **Mixed Symptoms**: Yellowing, wilting, lesions, leaf curl, and stunted growth can all appear simultaneously.
- **Difficulty in Treatment**: Managing multiple diseases can be complex as different pathogens may require different control measures.
- **Severe Yield Reduction**: The combined effect of multiple diseases can severely impact plant health, leading to major yield loss.
""")

# --- SUMMARY SECTION ---
st.header("📋 Summary and Prevention")
st.write("""
- **Proper Care**: Ensure adequate watering, pruning, and nutrient supply to maintain plant health.
- **Disease-Resistant Varieties**: Use disease-resistant seeds or plant varieties whenever possible.
- **Good Hygiene**: Keep tools, equipment, and planting areas clean to prevent the spread of pathogens.
- **Appropriate Fungicide Use**: Use fungicides and pesticides appropriately, and target specific diseases as needed.
""")

# --- SIDEBAR ---
st.sidebar.header("Navigation")
st.sidebar.write("Use the sidebar to navigate different sections of the app.")
st.sidebar.image("/Users/chi/Plant-Disease-Detection/logo-png.webp", width=100)

# --- BACKGROUND IMAGE ---
background_image = "/Users/chi/Plant-Disease-Detection/background.jpeg"
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url({background_image});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: #333;
    }}
    h1, h2, h3 {{
        color: #2E8B57;
    }}
    p, li {{
        font-size: 1.1em;
        line-height: 1.6;
    }}
    </style>
    """, unsafe_allow_html=True
)

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
