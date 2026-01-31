from django.shortcuts import render
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Load saved models from given file paths
rf_model = pickle.load(open(r"C:\Users\User\Music\RAIN_FALL\FRONTEND\random_forest_model.pkl", 'rb'))
xgb_model = pickle.load(open(r"C:\Users\User\Music\RAIN_FALL\FRONTEND\XGBoost_model.pkl", 'rb'))

# Label encoder for categorical inputs
le = LabelEncoder()

# Class names
class_names = ['No Rain Tomorrow', 'Rain Tomorrow']

# Create your views here.
def home(request):
	return render(request, 'index.html')

def input(request):
	return render(request, 'input.html')

def output(request):
    if request.method == "POST":
        # Extract numeric input values
        MinTemp = request.POST.get("MinTemp")
        MaxTemp = request.POST.get("MaxTemp")
        Rainfall = request.POST.get("Rainfall")
        Evaporation = request.POST.get("Evaporation")
        Sunshine = request.POST.get("Sunshine")
        WindGustSpeed = request.POST.get("WindGustSpeed")
        WindSpeed9am = request.POST.get("WindSpeed9am")
        WindSpeed3pm = request.POST.get("WindSpeed3pm")
        Humidity9am = request.POST.get("Humidity9am")
        Humidity3pm = request.POST.get("Humidity3pm")
        Pressure9am = request.POST.get("Pressure9am")
        Pressure3pm = request.POST.get("Pressure3pm")
        Cloud9am = request.POST.get("Cloud9am")
        Cloud3pm = request.POST.get("Cloud3pm")
        Temp9am = request.POST.get("Temp9am")
        Temp3pm = request.POST.get("Temp3pm")

        # Extract categorical input values
        WindGustDir = request.POST.get("WindGustDir")
        WindDir9am = request.POST.get("WindDir9am")
        WindDir3pm = request.POST.get("WindDir3pm")

        # Encode categorical inputs using LabelEncoder
        WindGustDir = le.fit_transform([WindGustDir])[0]
        WindDir9am = le.fit_transform([WindDir9am])[0]
        WindDir3pm = le.fit_transform([WindDir3pm])[0]

        # Combine all input features into a list
        lst = [float(MinTemp), float(MaxTemp), float(Rainfall), float(Evaporation), float(Sunshine),
               float(WindGustDir), float(WindGustSpeed), float(WindDir9am), float(WindDir3pm),
               float(WindSpeed9am), float(WindSpeed3pm), float(Humidity9am), float(Humidity3pm),
               float(Pressure9am), float(Pressure3pm), float(Cloud9am), float(Cloud3pm),
               float(Temp9am), float(Temp3pm)]

        input_data = np.array([lst])

        # Get algorithm choice from form
        algo = request.POST.get('algo')

        # Predict using selected model
        if algo == 'rf':
            out = rf_model.predict(input_data)[0]
        elif algo == 'xgb':
            out = xgb_model.predict(input_data)[0]
        else:
            out = None

        # Determine the prediction result
        if out == 1:
            class_name = "Rain Tomorrow"
        else:
            class_name = "No Rain Tomorrow"

        print(class_name)  # For debugging (optional)

        return render(request, 'output.html', {'out': class_name})
    else:
        return render(request, 'input.html')
