# predictive_maintenance.py
import joblib
import numpy as np

def load_model(filename):
    """Load a pre-trained machine learning model from a file."""
    model = joblib.load(filename)
    return model

def predict_maintenance(model, new_data):
    """Predict whether maintenance is required based on new sensor data."""
    prediction = model.predict([new_data])
    return "Maintenance Required" if prediction[0] == 1 else "No Maintenance Required"

if __name__ == "__main__":
    model = load_model('predictive_maintenance_model.joblib')
    # Example new data input (normalized features)
    new_data = np.array([0.7, 0.6, 0.1, 0.3, 0.9])
    result = predict_maintenance(model, new_data)
    print(result)
