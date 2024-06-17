from sklearn.ensemble import IsolationForest #uses IsolationForest for cybersecurity help
from sklearn.metrics import classification_report, roc_auc_score
import joblib
from data_processing.preprocess import load_and_preprocess_data

X_train, X_test, y_train, y_test = load_and_preprocess_data()

model = IsolationForest(contamination=0.1)
model.fit(X_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print("AUC-ROC Score:", roc_auc_score(y_test, y_pred))

joblib.dump(model, 'ml_model/isolation_forest_model.pkl')
