# water_quality_ai.py

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import pickle  # ✅ to save model

# Step 1: Create synthetic dataset
np.random.seed(42)
ph_values = np.random.uniform(0, 14, 200)

# Labeling rule
labels = []
for ph in ph_values:
    if 6.5 <= ph <= 8.5:
        labels.append("Good")
    elif 5.5 <= ph < 6.5 or 8.5 < ph <= 9.5:
        labels.append("Average")
    else:
        labels.append("Bad")

data = pd.DataFrame({"pH": ph_values, "Quality": labels})

# Step 2: Encode labels
data["QualityEncoded"] = data["Quality"].map({"Bad": 0, "Average": 1, "Good": 2})

# Step 3: Train-test split
X = data[["pH"]]
y = data["QualityEncoded"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train model
model = LogisticRegression()
print("\n🔁 Training AI Model on Water Quality Data...")
model.fit(X_train, y_train)
print("✅ Training Complete!\n")

# Step 5: Evaluate model
y_pred = model.predict(X_test)
print("📊 Model Evaluation Report:")
print(classification_report(y_test, y_pred))
print(f"Overall Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%\n")

# ✅ Step 6: Save trained model for Flask
with open("water_quality_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("💾 Model saved as 'water_quality_model.pkl'!")

# Optional: interactive test (keep for manual testing)
try:
    user_ph = float(input("Enter water pH value to predict quality: "))
    pred = model.predict([[user_ph]])[0]
    prob = model.predict_proba([[user_ph]])[0]

    quality_map = {0: "Bad", 1: "Average", 2: "Good"}
    predicted_quality = quality_map[pred]

    print(f"\n💧 Predicted Water Quality: {predicted_quality}")
    print(f"Confidence Levels:")
    print(f"  • Bad: {prob[0]*100:.2f}%")
    print(f"  • Average: {prob[1]*100:.2f}%")
    print(f"  • Good: {prob[2]*100:.2f}%")
except:
    print("Skipping manual test mode.")
