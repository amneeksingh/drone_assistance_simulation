# training_model.py
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        logging.info("Data loaded successfully.")
        return data
    except FileNotFoundError:
        logging.error("Data file not found.")
        return None

def preprocess_data(data):
    if data is None:
        logging.error("No data to preprocess.")
        return None, None
    X = data.drop('maintenance_required', axis=1)  # Features
    y = data['maintenance_required']  # Target
    return X, y

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    # Hyperparameter grid
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20],
    }
    grid_search = GridSearchCV(model, param_format = {key: val for key, val in param_grid.items() if val is not None}, cv=3, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    logging.info("Best parameters found: {}".format(grid_search.best_params_))
    return grid_search.best_estimator_

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    logging.info("Accuracy: {}".format(accuracy_score(y_test, predictions)))
    logging.info("Classification Report:\\n{}".format(classification_report(y_test, predictions)))

def save_model(model, filename):
    joblib.dump(model, filename)
    logging.info(f"Model saved as {filename}")

if __name__ == "__main__":
    data = load_data('sensor_data.csv')
    X, y = preprocess_data(data)
    if X is not None and y is not None:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = train_model(X_train, y_train)
        evaluate_model(model, X_test, y_test)
        save_model(model, 'predictive_maintenance_model.joblib')
