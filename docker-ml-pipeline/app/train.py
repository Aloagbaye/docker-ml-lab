import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

RANDOM_SEED = 42

# Load dataset
X, y = load_iris(return_X_y=True)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=RANDOM_SEED)
clf.fit(X, y)

# Save model/ serialize model with joblib
joblib.dump(clf, "model.pkl")
print("Model saved as model.pkl")
