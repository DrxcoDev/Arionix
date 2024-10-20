# evaluation.py
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def evaluar_modelo(modelo, X_test, y_test):
    # Hacer predicciones
    predicciones = modelo.predict(X_test)

    # Evaluar precisión
    precision = accuracy_score(y_test, predicciones)
    print(f'Precisión: {precision:.2f}')

    # Matriz de confusión
    confusion = confusion_matrix(y_test, predicciones)
    print('Matriz de Confusión:')
    print(confusion)

    # Informe de clasificación
    informe = classification_report(y_test, predicciones)
    print('Informe de Clasificación:')
    print(informe)
