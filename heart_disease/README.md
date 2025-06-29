
# 💓 Heart Disease Prediction System

## 📌 Project Overview

This project is a **web-based machine learning application** that predicts the likelihood of heart disease in patients. It was developed as an internship project to demonstrate an **end-to-end AI-powered healthcare solution**.

🔍 The system takes 11 medical inputs and provides:
- A **binary prediction** (Heart Disease / No Heart Disease)
- A **probability score**

![System Architecture](system_architecture.png)  
*Diagram showing the workflow*

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

-📊 Classification Report:
- --------------------------
                  precision    recall  f1-score   support

       Normal       0.71      1.00      0.83        10
Heart Disease       1.00      0.80      0.89        20

     accuracy                           0.87        30
    macro avg       0.86      0.90      0.86        30
 weighted avg       0.90      0.87      0.87        30

📉 Confusion Matrix:
[[10  0]
 [ 4 16]]




🔍 Prediction Details:
 age  sex  chest pain type  resting bp s  cholesterol  fasting blood sugar  resting ecg  max heart rate  exercise angina  oldpeak  ST slope  True_Label  Predicted_Label  HeartDisease_Prob(%)
  49    0                3           160          180                    0            0             156                0      1.0         2           1                0                 23.19
  48    0                4           138          214                    0            0             108                1      1.5         2           1                1                 80.35
  37    1                4           140          207                    0            0             130                1      1.5         2           1                1                 92.62
  58    1                2           136          164                    0            1              99                1      2.0         2           1                1                 84.79
  49    1                4           140          234                    0            0             140                1      1.0         2           1                1                 92.13
  38    1                4           110          196                    0            0             166                0      0.0         2           1                1                 69.03
  60    1                4           100          248                    0            0             125                0      1.0         2           1                1                 83.57
  36    1                2           120          267                    0            0             160                0      3.0         2           1                1                 53.28
  44    1                2           150          288                    0            0             150                1      3.0         2           1                1                 78.92
  53    1                3           145          518                    0            0             130                0      0.0         2           1                0                 21.59
  54    1                4           125          224                    0            0             122                0      2.0         2           1                1                 89.52
  41    1                4           130          172                    0            1             130                0      2.0         2           1                1                 86.95
  65    1                4           140          306                    1            0              87                1      1.5         2           1                1                 98.01
  54    0                3           130          294                    0            1             100                1      0.0         2           1                0                 24.52
  43    1                4           120          175                    0            0             120                1      1.0         2           1                1                 92.47
  41    1                4           110          289                    0            0             170                0      0.0         2           1                1                 62.38
  50    1                4           130          233                    0            0             121                1      2.0         2           1                1                 94.79
  47    0                4           120          205                    0            0              98                1      2.0         2           1                1                 82.41
  31    1                4           120          270                    0            0             153                1      1.5         2           1                1                 87.23
  58    1                3           130          213                    0            1             140                0      0.0         2           1                0                 41.87
  37    0                3           130          211                    0            0             142                0      0.0         1           0                0                  1.71
  39    1                2           120          204                    0            0             145                0      0.0         1           0                0                  6.85
  42    0                3           115          211                    0            1             137                0      0.0         1           0                0                  1.55

---