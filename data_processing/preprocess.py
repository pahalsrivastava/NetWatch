import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

def load_and_preprocess_data():
    data = pd.read_csv('path/to/UNSW-NB15.csv')
    data = data.dropna()

    scaler = StandardScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data.select_dtypes(include=['float64', 'int64'])), columns=data.select_dtypes(include=['float64', 'int64']).columns)

    label_encoder = LabelEncoder()
    data_encoded = data.apply(lambda col: label_encoder.fit_transform(col) if col.dtype == 'object' else col)

    X = data_encoded.drop('label', axis=1)
    y = data_encoded['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_preprocess_data()
