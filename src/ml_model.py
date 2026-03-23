# ml_model.py

import pandas as pd
import os

# ML Models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score

# -------------------------------
# 📁 Load Dataset (Safe Path)
# -------------------------------
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, 'data', 'student_data.csv')

data = pd.read_csv(file_path)

print("Dataset Loaded Successfully!\n")
print(data.head())

# -------------------------------
# 📊 Features & Labels
# -------------------------------
X = data[['attendance', 'study_hours', 'internal_marks']]
y_reg = data['final_marks']  # for regression

# -------------------------------
# 🔀 Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y_reg, test_size=0.2, random_state=42
)

# -------------------------------
# 📈 LINEAR REGRESSION (Predict Marks)
# -------------------------------
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

y_pred = reg_model.predict(X_test)

print("\n--- Regression Output ---")
print("Predicted Marks:", y_pred)
print("Actual Marks:", list(y_test))

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# -------------------------------
# 🎯 CLASSIFICATION (Pass/Fail)
# -------------------------------
# Create new column
data['result'] = data['final_marks'].apply(lambda x: 1 if x >= 50 else 0)

y_clf = data['result']

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X, y_clf, test_size=0.2, random_state=42
)

clf_model = DecisionTreeClassifier()
clf_model.fit(X_train_c, y_train_c)

y_pred_c = clf_model.predict(X_test_c)

print("\n--- Classification Output ---")
print("Predicted:", y_pred_c)
print("Actual:", list(y_test_c))

accuracy = accuracy_score(y_test_c, y_pred_c)
print("Accuracy:", accuracy)

# -------------------------------
# 🔮 Prediction Functions (for main.py)
# -------------------------------
def predict_marks(attendance, study_hours, internal_marks):
    return reg_model.predict([[attendance, study_hours, internal_marks]])[0]

def predict_result(attendance, study_hours, internal_marks):
    result = clf_model.predict([[attendance, study_hours, internal_marks]])[0]
    return "Pass" if result == 1 else "Fail"