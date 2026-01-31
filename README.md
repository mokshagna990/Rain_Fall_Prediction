# 🌧️ RAIN_FALL - Rainfall Prediction System

A machine learning-powered web application that predicts rainfall using weather data. This project combines advanced ML models (XGBoost and Random Forest) with a user-friendly Django web interface to provide accurate rainfall predictions.

## 📋 Project Overview

RAIN_FALL is a comprehensive rainfall prediction system that analyzes various weather parameters to forecast whether it will rain tomorrow. The system uses historical weather data from multiple Australian locations to train sophisticated machine learning models.

## ✨ Features

- **Dual ML Models**: Implements both XGBoost and Random Forest algorithms for robust predictions
- **Interactive Web Interface**: User-friendly Django-based frontend for easy data input and visualization
- **Comprehensive Weather Analysis**: Analyzes 20+ weather parameters including:
  - Temperature (Min/Max, 9am/3pm)
  - Humidity levels
  - Wind speed and direction
  - Atmospheric pressure
  - Cloud coverage
  - Evaporation and sunshine hours
- **Real-time Predictions**: Instant rainfall forecasting based on current weather conditions
- **Data Visualization**: Visual representation of weather patterns and prediction results

## 🏗️ Project Structure

```
RAIN_FALL/
├── BACKEND/
│   └── Rain_Fall.ipynb          # ML model development and training
├── DATASET/
│   └── Weather Training Data.csv # Historical weather data (99,516 records)
├── FRONTEND/
│   ├── manage.py                 # Django management script
│   ├── db.sqlite3                # SQLite database
│   ├── XGBoost_model.pkl         # Trained XGBoost model
│   ├── random_forest_model.pkl   # Trained Random Forest model
│   ├── self/                     # Django project settings
│   ├── webapp/                   # Main Django application
│   ├── templates/                # HTML templates
│   ├── static/                   # Static files (CSS, JS, images)
│   └── assests/                  # Additional assets
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   cd "d:/MOKI Floder/nube matrix/PROJECTS/RAIN_FALL"
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to the frontend directory**
   ```bash
   cd FRONTEND
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## 📊 Dataset Information

The project uses a comprehensive weather dataset with:
- **99,516 records** from various Australian locations
- **23 features** including meteorological measurements
- **Target variable**: RainTomorrow (binary classification)

### Key Features:
- Location, Date
- MinTemp, MaxTemp
- Rainfall, Evaporation, Sunshine
- WindGustDir, WindGustSpeed
- WindDir9am, WindDir3pm
- WindSpeed9am, WindSpeed3pm
- Humidity9am, Humidity3pm
- Pressure9am, Pressure3pm
- Cloud9am, Cloud3pm
- Temp9am, Temp3pm
- RainToday, RainTomorrow

## 🤖 Machine Learning Models

### XGBoost Classifier
- Gradient boosting algorithm
- Optimized for classification tasks
- High accuracy with efficient training

### Random Forest Classifier
- Ensemble learning method
- Robust against overfitting
- Handles non-linear relationships well

Both models are pre-trained and stored as pickle files for quick predictions.

## 🛠️ Technologies Used

### Backend & ML
- **Python 3.x** - Core programming language
- **Django 3.0.8** - Web framework
- **scikit-learn** - Machine learning library
- **XGBoost** - Gradient boosting framework
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **matplotlib & seaborn** - Data visualization

### Frontend
- **HTML/CSS** - User interface
- **JavaScript** - Interactive elements
- **Django Templates** - Dynamic content rendering

### Database
- **SQLite** - Lightweight database for development

## 📈 Model Performance

The models have been trained on extensive historical weather data and evaluated using:
- Confusion Matrix
- ROC Curve Analysis
- Accuracy Score
- Precision and Recall metrics

## 🔧 Configuration

### Django Settings
The project uses Django 3.0.8 with the following key configurations:
- **Debug Mode**: Enabled (for development)
- **Database**: SQLite
- **Static Files**: Configured for CSS, JS, and images
- **Templates**: Located in the `templates/` directory

### Security Note
⚠️ **Important**: The current configuration includes a hardcoded `SECRET_KEY` and `DEBUG=True`. Before deploying to production:
1. Generate a new secret key
2. Set `DEBUG=False`
3. Configure `ALLOWED_HOSTS`
4. Use environment variables for sensitive data

## 📝 Usage

1. Launch the web application
2. Enter current weather parameters in the input form
3. Click "Predict" to get rainfall forecast
4. View the prediction result and confidence score

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

This project is available for educational and portfolio purposes.

## 👨‍💻 Author

Created as a machine learning portfolio project demonstrating:
- End-to-end ML pipeline development
- Web application integration
- Data science and software engineering skills

## 🔮 Future Enhancements

- [ ] Add more ML models (Neural Networks, SVM)
- [ ] Implement user authentication
- [ ] Add historical prediction tracking
- [ ] Create API endpoints for external integrations
- [ ] Deploy to cloud platform (Heroku, AWS, Azure)
- [ ] Add real-time weather data integration
- [ ] Implement model retraining pipeline
- [ ] Create mobile-responsive design
- [ ] Add data visualization dashboard

## 📞 Support

For questions or issues, please open an issue in the repository.

---

**Note**: This is a portfolio/educational project. For production use, additional security measures and optimizations are recommended.
