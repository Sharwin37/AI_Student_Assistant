# clustering.py

import pandas as pd
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# -------------------------------
# 📁 Load Dataset (Safe Path)
# -------------------------------
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, 'data', 'student_data.csv')

data = pd.read_csv(file_path)

print("✅ Dataset Loaded Successfully!\n")

# -------------------------------
# 📊 Select Features for Clustering
# -------------------------------
X = data[['attendance', 'study_hours', 'final_marks']]

# -------------------------------
# 🔵 Apply K-Means Clustering
# -------------------------------
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
data['cluster'] = kmeans.fit_predict(X)

print("📊 Clustering Result:\n")
print(data[['name', 'attendance', 'study_hours', 'final_marks', 'cluster']])

# -------------------------------
# 📌 Cluster Interpretation
# -------------------------------
print("\nCluster Meaning (approx):")
print("0 → High Performers")
print("1 → Average Students")
print("2 → At-Risk Students")

# -------------------------------
# 📈 Visualization (Scatter Plot)
# -------------------------------
plt.figure()

plt.scatter(
    data['study_hours'],
    data['final_marks'],
    c=data['cluster']
)

plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Student Clusters (K-Means)")

plt.show()

# -------------------------------
# 📌 Function for Integration
# -------------------------------
def get_clusters():
    return data[['name', 'cluster']]