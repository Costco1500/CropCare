# CropCare

**Plant-disease detection and crop-health tracking in a Streamlit web app.**

CropCare helps growers explore possible leaf diseases from photos, learn about common symptoms, and record crop-health observations. It combines a TensorFlow image-classification ensemble with a simple interface for uploading images and keeping a crop journal.

**Winner — 2024 Congressional App Challenge, Florida's 2nd District**

[Watch the demo and read the award announcement](https://www.congressionalappchallenge.us/24-fl02/) · [View the source code](https://github.com/Costco1500/CropCare)

## Features

- **Leaf-image classification:** Upload a JPG or PNG and generate a prediction across four categories: healthy, multiple diseases, rust, and scab.
- **Prediction scores and care tips:** View the model's selected category, its score, and guidance or links to educational content.
- **Crop Health Tracker:** Record dates, crop types, health status, and notes; filter entries and export them as CSV.
- **Disease education:** Explore causes, symptoms, and prevention information for rust, scab, and multiple diseases.
- **Multipage interface:** Navigate between the home page, disease detector, educational content, and journal.

## How detection works

1. The user uploads a leaf image.
2. The preprocessing code resizes it to **512 × 512**, keeps three color channels, adds a batch dimension, and rescales pixel values by `1/255`.
3. **DenseNet121** and **Xception** backbones each feed a global-average-pooling layer and a four-class softmax classifier.
4. The ensemble averages the two models' outputs.
5. The app displays the highest-scoring category and associated guidance.

The backbones are initialized with ImageNet weights, then the application loads the project's trained weights from `model.h5`.

> The displayed percentage is a model prediction score, not a measured accuracy for that image. Predictions are limited to the four supported classes; the app does not establish reliable detection across all crops or diseases.

## Technology

| Component | Technology |
| --- | --- |
| Interface and navigation | Streamlit |
| Model architecture and inference | TensorFlow / Keras |
| Image handling | Pillow, NumPy |
| Journal storage and filtering | pandas, CSV |
| Training workflow | Jupyter / Google Colab notebook |

## Repository guide

| File | Purpose |
| --- | --- |
| `streamlit_app.py` | Multipage entry point and navigation |
| `app.py` | Model construction, weight loading, image upload, and prediction UI |
| `utils.py` | Image preprocessing, inference, and result formatting |
| `crop_journal.py` | Crop-health entries, filtering, deletion, and CSV export |
| `crop_journal.csv` | Local journal data |
| `cause_effect.py` | Disease education page |
| `about_me.py` | Home page and project goals |
| `Plant Disease Detection.ipynb` | Model training and prediction workflow |
| `requirements.txt` | Original dependency list |
| `setup.sh` | Streamlit configuration script |

## Local setup

**The checked-in prototype requires preparation before it can run end to end.** The repository does not currently include `model.h5`, the referenced `crop_dashboard.py`, or the local image assets used by several pages.

### 1. Clone and create an environment

```bash
git clone https://github.com/Costco1500/CropCare.git
cd CropCare
python -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Or in Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Resolve dependency compatibility

The original `requirements.txt` pins Streamlit to `0.57.3`, while the multipage entry point uses newer `st.Page` and `st.navigation` APIs. It also includes older TensorFlow dependencies and a Windows-specific package.

Use a Python/TensorFlow combination supported by your platform and reconcile the dependency versions before installing. A maintained environment needs Streamlit, TensorFlow, NumPy, pandas, and Pillow. The current repository does not provide a verified, compatible lockfile; installing the original requirements unchanged may fail.

### 3. Supply model weights and assets

- Obtain compatible trained ensemble weights and place them at `model.h5` in the repository root. No weight-download URL is included in this repository.
- Replace or remove developer-specific absolute paths to `logo-png.webp` and `background.jpeg` in the page files.
- Restore `crop_dashboard.py`, or remove its page declaration and navigation entry from `streamlit_app.py`.
- If retraining, update the notebook's Google Drive dataset paths and provide the training data. The dataset is not bundled.

### 4. Launch

After resolving the prerequisites above, run from the repository root:

```bash
streamlit run streamlit_app.py
```

To launch only the disease-detection page after supplying its dependencies, weights, and image assets:

```bash
streamlit run app.py
```

## Current limitations

- The Crop Analytics page is referenced in navigation but is not included in the repository.
- The journal uses a local CSV file shared by the running app; it does not provide separate accounts or a multi-user database.
- Image preprocessing assumes an image with color channels. Grayscale input needs additional handling.
- No independently reproduced evaluation metrics are reported here.

## Team and recognition

Built by **Wesley Kuntz, Alex Wang, Mikhail Abraimov, and Raami Abichou**.

CropCare won the **2024 Congressional App Challenge in Florida's 2nd District**. See the [official announcement and demo](https://www.congressionalappchallenge.us/24-fl02/).

## Acknowledgments

The included training notebook contains attribution to **Noor Khokhar / [PyResearch](https://github.com/pyresearch/pyresearch)**. Preserve that attribution when adapting or redistributing the notebook.
