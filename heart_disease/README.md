
# 💓 Heart Disease Prediction System

## 📌 Project Overview

This project is a **web-based machine learning application** that predicts the likelihood of heart disease in patients. It was developed as an internship project to demonstrate an **end-to-end AI-powered healthcare solution**.

🔍 The system takes 11 medical inputs and provides:
- A **binary prediction** (Heart Disease / No Heart Disease)
- A **probability score**


---

## 🧰 Tech Stack

### 🧠 Machine Learning
- Python 3.8+
- scikit-learn
- pandas
- numpy
- joblib (for model serialization)

### 🖥️ Backend
- Flask (Python web framework)
- Gunicorn (for production deployment)

### 🎨 Frontend
- HTML5
- CSS3 (responsive)
- Jinja2 templating

### ☁️ Infrastructure
- Git & GitHub (version control)
- Heroku (cloud deployment)

---

## 🧪 Implementation Details

### 🔍 Machine Learning Model

- **Algorithm**: Random Forest Classifier  
- **Dataset**: Cleveland Heart Disease Dataset  
- **Size**: 303 records, 14 features  
- **Key Features**:
  - Age
  - Sex
  - Chest pain type
  - Resting blood pressure
  - Serum cholesterol
  - Fasting blood sugar
  - Resting ECG
  - Maximum heart rate
  - Exercise-induced angina
  - ST depression
  - ST slope

#### ✅ Performance Metrics
| Metric     | Score   |
|------------|---------|
| Accuracy   | 87.5%   |
| Precision  | 88.2%   |
| Recall     | 86.7%   |
| F1-Score   | 87.4%   |

---

### 🌐 Web Application

#### Backend
- Flask REST API (`/predict`)
- Input validation & model loading
- Probability calculation based on predicted class

#### Frontend
- Responsive HTML/CSS form
- Accessible dropdown inputs
- Jinja2 templated result display
- Optional probability bars/animations

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

```bash
# Clone the repository
git clone https://github.com/username/heart-disease-predictor.git
cd heart-disease-predictor

# Create a virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate         # Windows

# Install required packages
pip install -r requirements.txt

# Run the application
python app.py
```

---

## 🚀 Usage

1. Open browser: `http://localhost:5000`
2. Fill in the patient's details
3. Click **Predict Heart Disease Risk**
4. View results:
   - ✅ Prediction (e.g. Heart Disease Detected)
   - 📊 Probability (e.g. 87.53%)

---

## 📁 Project Structure

```
.
├── app.py                      # Flask backend
├── heart_disease_model.pkl     # Trained ML model
├── dataset.csv                 # Cleaned dataset
├── heart_disease_prediction.ipynb  # Jupyter notebook
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # Main HTML page
├── static/
│   └── style.css               # Custom CSS styles
└── README.md                   # Project documentation
```

---

## 🔮 Future Improvements

- [ ] Add user authentication
- [ ] Save & track patient prediction history
- [ ] Integrate charts or bar graphs (visual results)
- [ ] Add SHAP explainability for each prediction

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full terms.

---

### ✅ Heart Disease Prediction Check (30 real samples)
        - Accuracy: 86.67%
