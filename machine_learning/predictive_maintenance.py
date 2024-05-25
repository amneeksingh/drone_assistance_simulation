# predictive_maintenance.py
import joblib
import numpy as np
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_model(filename):
    try:
        model = joblib.load(filename)
        logging.info("Model loaded successfully.")
        return model
    except FileNotFoundError:
        logging.error("Model file not found.")
        return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

def predict_maintenance(model, new_data):
    if model is None:
        logging.error("Model is not loaded.")
        return "Error: Model not loaded"
    try:
        # Ensure the new_data is in the correct format (numpy array)
        if not isinstance(new_data, np.ndarray):
            raise ValueError("Input data must be a numpy array.")
        prediction = model.predict([new_data])
        return "Maintenance Required" if prediction[0] == 1 else "No Maintenance Required"
    except Exception as e:
        logging.error(f"An error occurred during prediction: {e}")
        return "Prediction error"

if __name__ == "__main__":
    model = load_model('predictive_maintenance_model.joblib')
    new_data = np.array([0.7, 0.6, 0.1, 0.3, 0.9])  # Example new data input (normalized features)
    result = predict_maintenance(model, new_data)
    print(result)
