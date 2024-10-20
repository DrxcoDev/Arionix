# main.py
from data_preprocessing import cargar_datos, preprocesar_datos
from model import entrenar_modelo
from evaluation import evaluar_modelo

def main():
    # Cargar los datos
    data = cargar_datos('tus_datos.csv')

    # Preprocesar los datos
    X_train, X_test, y_train, y_test = preprocesar_datos(data, 'target')

    # Entrenar el modelo
    modelo = entrenar_modelo(X_train, y_train)

    # Evaluar el modelo
    evaluar_modelo(modelo, X_test, y_test)

if __name__ == "__main__":
    main()
