import pandas as pd
import pickle
import joblib


from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, classification_report, confusion_matrix

from sklearn.dummy import DummyClassifier

from xgboost import XGBClassifier, XGBRegressor

import shap
import lime
from lime import lime_tabular

# Import the clean random sample of 10k data
df = pd.read_csv('/home/rahil_shaikh/datasci_9_data_prep/model_dev1/data/raw/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv')
len(df)

# Define the features and the target variable
X = df.drop('YEAR', axis=1)  # Features (all columns except 'arrest')
y = df['YEAR']               # Target variable (arrest)

# Initialize the StandardScaler
scaler = StandardScaler()
scaler.fit(X) # Fit the scaler to the features

# Fit the scaler to the features and transform
X_scaled = scaler.transform(X)

# Split the scaled data into training, validation, and testing sets (70%, 15%, 15%)
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Check the size of each set
(X_train.shape, X_val.shape, X_test.shape)
