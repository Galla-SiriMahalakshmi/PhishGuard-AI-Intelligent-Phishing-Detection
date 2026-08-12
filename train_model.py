import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# ==========================================
# 1. CREATE TRAINING DATASET
# ==========================================

np.random.seed(42)

n = 3000

data = pd.DataFrame({
    "url_length": np.random.randint(15, 180, n),
    "num_dots": np.random.randint(0, 8, n),
    "num_hyphens": np.random.randint(0, 8, n),
    "num_special_chars": np.random.randint(0, 18, n),
    "has_ip": np.random.randint(0, 2, n),
    "has_https": np.random.randint(0, 2, n),
    "domain_length": np.random.randint(5, 50, n),
    "num_subdomains": np.random.randint(0, 5, n),
    "has_at_symbol": np.random.randint(0, 2, n),
    "redirect_count": np.random.randint(0, 5, n)
})


# ==========================================
# 2. CREATE TARGET LABEL
# ==========================================

data["phishing"] = (
    (data["has_ip"] == 1) |
    (data["has_at_symbol"] == 1) |
    (data["num_special_chars"] > 10) |
    (data["num_subdomains"] > 2) |
    (data["redirect_count"] > 2)
).astype(int)


# ==========================================
# 3. FEATURES AND TARGET
# ==========================================

X = data.drop("phishing", axis=1)
y = data["phishing"]


# ==========================================
# 4. TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==========================================
# 5. RANDOM FOREST MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=150,
    random_state=42
)


# ==========================================
# 6. TRAIN MODEL
# ==========================================

model.fit(X_train, y_train)


# ==========================================
# 7. TEST MODEL
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("PHISHING WEBSITE DETECTION MODEL")
print("=" * 50)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ==========================================
# 8. SAVE MODEL
# ==========================================

joblib.dump(model, "phishing_model.pkl")

print("\nModel saved successfully!")
print("File created: phishing_model.pkl")