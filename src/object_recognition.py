import tensorflow as tf
import numpy as np
import cv2

# Cargar el modelo preentrenado MobileNetV2
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Longitud focal de la cámara (ajusta este valor según tu cámara)
FOCAL_LENGTH = 700  # en píxeles
KNOWN_WIDTH = 0.2   # Tamaño real del objeto (en metros, ejemplo: 20 cm)

# Función para preprocesar la imagen
def preprocess_image(image):
    image = cv2.resize(image, (224, 224))  # Cambiar tamaño a 224x224
    image = np.expand_dims(image, axis=0)  # Añadir dimensión extra
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    return image

# Función para obtener el nombre del objeto
def get_object_name(image):
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
    return decoded_predictions[0][0][1]  # Nombre del objeto

# Función para calcular la distancia al objeto
def calculate_distance(size_in_image):
    if size_in_image == 0:
        return float('inf')  # Evitar división por cero
    distance = (KNOWN_WIDTH * FOCAL_LENGTH) / size_in_image
    return distance

# Función para medir el tamaño del objeto en la imagen (asumiendo un rectángulo)
def measure_object_size(frame, box_coordinates):
    x, y, w, h = box_coordinates
    return w  # Considerar el ancho del objeto en la imagen
