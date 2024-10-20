# model.py
from sklearn.linear_model import LogisticRegression

def entrenar_modelo(X_train, y_train):
    # Inicializar el modelo
    modelo = LogisticRegression()
    
    # Entrenar el modelo
    modelo.fit(X_train, y_train)
    return modelo
