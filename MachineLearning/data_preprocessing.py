# data_preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split

def cargar_datos(archivo_csv):
    # Cargar datos desde un archivo CSV
    data = pd.read_csv(archivo_csv)
    return data

def preprocesar_datos(data, target_col):
    # Manejar valores faltantes
    data.fillna(data.mean(), inplace=True)

    # Convertir variables categóricas en variables dummy
    data = pd.get_dummies(data, drop_first=True)

    # Separar características y variable objetivo
    X = data.drop(target_col, axis=1)  # Características
    y = data[target_col]                # Variable objetivo

    # Dividir los datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
