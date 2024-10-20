import cv2
from object_recognition import get_object_name, calculate_distance, measure_object_size
import time

# Inicia la captura de video
cap = cv2.VideoCapture(0)  # 0 es la cámara por defecto

def Login():
    user = input("Name: ")
    password = input("Password: ")
    number_user_code = input("Number code: ")
    secret_token = input("Secret Token: ")
    captcha = input("Write the next text GGHYYKM344: ")
    confirm_token = input("Confirm the secret token: ")

    if user == "Admin":
        if password == "Admin##@c0dePass":
            if number_user_code == "A#c@n*s":
                if secret_token == "A00CODEIDSECRET20438":
                    if captcha == "GGHYYKM344":
                        if confirm_token == secret_token:
                            print("Succes")
                            return True
    else:
        print("Error name")
        return False
    
Login()

prev_time = time.time()
prev_position = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Para el reconocimiento de objetos, podrías usar un detector adicional
    # Aquí simplificamos usando el nombre del objeto
    object_name = get_object_name(frame)
    
    # Supongamos que detectamos el objeto y tenemos sus coordenadas (x, y, w, h)
    # Esto debería venir de un detector de objetos; aquí es solo un ejemplo.
    # Supón que detectamos un objeto en la posición (100, 100) con un tamaño de (50, 50)
    box_coordinates = (100, 100, 50, 50)  # Ejemplo de coordenadas (x, y, w, h)
    
    size_in_image = measure_object_size(frame, box_coordinates)  # Tamaño en píxeles
    distance = calculate_distance(size_in_image)  # Distancia en metros

    # Calcular la velocidad si hay una posición anterior
    current_time = time.time()
    if prev_position is not None:
        # Calcular la distancia recorrida (asumimos un simple movimiento horizontal)
        distance_moved = box_coordinates[0] - prev_position
        time_elapsed = current_time - prev_time
        if time_elapsed > 0:
            speed = distance_moved / time_elapsed  # Velocidad en píxeles por segundo
        else:
            speed = 0
    else:
        speed = 0

    # Actualizar la posición anterior y el tiempo
    prev_position = box_coordinates[0]
    prev_time = current_time

    # Mostrar resultados en la imagen
    cv2.putText(frame, f'Object: {object_name}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Distance: {distance:.2f} m', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Speed: {speed:.2f} px/s', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    # Mostrar la imagen con los resultados
    cv2.imshow('Object Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
