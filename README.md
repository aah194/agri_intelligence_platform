# 🌱 Agri Intelligence Platform

An AI-powered agricultural intelligence platform that uses Sentinel-2 satellite imagery to monitor vegetation health, detect crop stress, generate NDVI maps, forecast crop yield, and produce downloadable reports.

## 🚀 Features

### 🌿 NDVI Analysis

* Calculates Normalized Difference Vegetation Index (NDVI)
* Generates NDVI heatmaps
* Saves NDVI visualizations automatically

### 📊 Vegetation Health Monitoring

* Healthy vegetation detection
* Moderate stress identification
* Stressed vegetation detection

### 🤖 AI Yield Forecasting

* Predicts expected crop yield
* Machine learning based forecasting
* Health-based yield estimation

### 🛰️ Satellite Image Upload

* Upload Sentinel-2 Red Band (B04)
* Upload Sentinel-2 NIR Band (B08)
* Perform real NDVI analysis

### 📈 NDVI Trend Analysis

* Visualizes vegetation trends over time
* Helps monitor crop health progression

### 📄 PDF Report Generation

* Generates agricultural reports
* Downloadable PDF output

---

## 🛠️ Tech Stack

* Python
* Streamlit
* NumPy
* Rasterio
* Matplotlib
* Scikit-Learn
* ReportLab

---

## 📂 Project Structure

agri_intelligence_platform/

├── dashboard/

│ ├── pages/

│ ├── forecasting.py

│ └── app.py

├── preprocessing/

│ ├── ndvi.py

│ └── sentinel_loader.py

├── models/

│ ├── stress_detection/

│ └── forecasting/

├── utils/

│ └── pdf_report.py

├── datasets/

├── outputs/

└── saved_models/

---

## ⚙️ Installation

```bash
git clone https://github.com/aah194/agri_intelligence_platform.git

cd agri_intelligence_platform

pip install -r requirements.txt
```

## ▶️ Run Application

```bash
streamlit run dashboard/app.py
```

## 📊 Example Output

Healthy: 73.08%

Moderate: 25.51%

Stressed: 1.41%

Predicted Yield: 5.9 tons/hectare

## 🎯 Future Improvements

* Real historical yield datasets
* Multi-season crop monitoring
* Weather integration
* Disease prediction models
* Online deployment
* GIS dashboard integration

## 👨‍💻 Author

Sumit Bombale

MCA Student (AI & Data Science)

Machine Learning & Remote Sensing Enthusiast
