import streamlit as st
from PIL import Image
import io
import numpy as np
import tensorflow as tf
from utils import clean_image, get_prediction, make_results

# Load the Model and Save to Cache
@st.cache(allow_output_mutation=True)
def load_model(path):
    # Xception Model
    xception_model = tf.keras.models.Sequential([
        tf.keras.applications.xception.Xception(include_top=False, weights='imagenet', input_shape=(512, 512, 3)),
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(4, activation='softmax')
    ])

    # DenseNet Model
    densenet_model = tf.keras.models.Sequential([
        tf.keras.applications.densenet.DenseNet121(include_top=False, weights='imagenet', input_shape=(512, 512, 3)),
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(4, activation='softmax')
    ])

    # Ensemble the Models
    inputs = tf.keras.Input(shape=(512, 512, 3))
    xception_output = xception_model(inputs)
    densenet_output = densenet_model(inputs)
    outputs = tf.keras.layers.average([densenet_output, xception_output])

    model = tf.keras.Model(inputs=inputs, outputs=outputs)

    # Load the Weights of Model
    model.load_weights(path)
    
    return model

# Hiding the Default Streamlit Menu
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True
)

# Load Model
model = load_model('model.h5')

# --- Application Header ---
st.title('🌿 Plant/Leaf Disease Detection 🌿')
st.write("Upload a picture of a leaf, and check for potential diseases affecting your plant!")

# Use columns to center and structure layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Upload Image Section
    st.subheader("Upload Your Leaf Image")
    uploaded_file = st.file_uploader("Choose an image file (JPG or PNG)", type=["jpg", "png"])

    # If a file is uploaded
    if uploaded_file is not None:
        # Display progress and spinner
        with st.spinner("Processing your image..."):
            # Read the uploaded image
            image = Image.open(io.BytesIO(uploaded_file.read()))
            st.image(image, caption='Uploaded Leaf', use_column_width=True)
            
            # Button to start prediction
            if st.button("Analyze Image"):
                # Display progress
                progress_text = st.empty()
                my_bar = st.progress(0)
                
                # Cleaning the image
                image = clean_image(image)
                my_bar.progress(30)
                progress_text.text("Image Cleaned...")
                
                # Making the predictions
                predictions, predictions_arr = get_prediction(model, image)
                my_bar.progress(60)
                progress_text.text("Generating Predictions...")
                
                # Making the results
                result = make_results(predictions, predictions_arr)
                my_bar.progress(100)
                progress_text.text("Analysis Complete")
                
                # Clear the progress display
                my_bar.empty()
                progress_text.empty()

                # --- Display Results ---
                st.markdown(f"### 🔍 Results: The plant {result['status']} with {result['prediction']} accuracy.")
                st.markdown(f"#### 💡 Tips: {result['tips']}")

        # Divider for better spacing
        st.markdown("---")
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

