
import random
import os
import sys
import time
import shutil
import math


# Clase para la generación de números primos
class PrimeGenerator:
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def generate_primes(limit):
        primes = []
        for num in range(2, limit):
            if PrimeGenerator.is_prime(num):
                primes.append(num)
        return primes


# Clase para el sistema de reservas
class Reservation:
    def __init__(self, name, date, time, guests):
        self.name = name
        self.date = date
        self.time = time
        self.guests = guests


class ReservationSystem:
    def __init__(self):
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def show_reservations(self):
        for res in self.reservations:
            print(f"{res.name} - {res.date} at {res.time} for {res.guests} guests")


# Clase para la simulación del juego de adivinanza
class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)

    def check_guess(self, guess):
        if guess < self.number:
            return "Too low!"
        elif guess > self.number:
            return "Too high!"
        else:
            return "Congratulations!"


# Clase para la generación de reportes
class SalesReport:
    @staticmethod
    def generate_sales_data(months):
        sales_data = {}
        for month in months:
            sales_data[month] = random.randint(1000, 5000)
        return sales_data

    @staticmethod
    def print_report(sales_data):
        for month, sales in sales_data.items():
            print(f"Sales for {month}: ${sales}")


# Clase para la automatización de tareas
class EmailSender:
    @staticmethod
    def send_email(recipient, subject, body):
        print(f"Sending email to {recipient} with subject '{subject}'")
        # Aquí podrías integrar una librería como smtplib para enviar correos reales


class FileCreate:
    @staticmethod
    def file_creator(namefile, route):
        open(f"{route}/{namefile}", "w")
        if open(f"{route}/{namefile}"):
            print(f"Succes, file", namefile, "created in", route)
        else:
            print("Error didn't create")
    
    @staticmethod
    def directory_creator(route):
        os.makedirs(route, exist_ok=True)
        print("Succefully directory created")

    @staticmethod
    def file_read(file): # File with directory
        with open(file, "r") as file:
            print(file.read())

    @staticmethod
    def file_write(file, data):
        with open(file, "w") as file:
            file.write(data)
            print(f"Succes, data wrote in {file}")

    @staticmethod
    def directory_remove(route):
        if os.path.exists(route):
            shutil.rmtree(route)
            print("File delete")
        else:
            print("File  not found")

    @staticmethod
    def copy_file(file):
        shutil.copy(file)
        print("Copy succes")

    
    @staticmethod
    def paste_file(file):
        shutil.move(file)
        print("File moved succes")

    
class CompileFile:

    def compiler(self, language, route_file):

        self.language = language

        if language == "python":
            os.system(f"python {route_file}")
        elif language == "java":
            os.system(f"javac {route_file}")
        elif language == "c++":
            os.system(f"g++ {route_file}")
        elif language == "js" or language == "javascript":
            os.system(f"node {route_file}")
        else:
            print("Language unssuported")
    
class Factorial:
    
    def factorial(self, n):
        self.n = n

        if n == 0 or n == 1:
            return 1
        else:
            return n * n - 1



# Programa principal
if __name__ == "__main__":
    print("Multifuction")

    # # Pegar un archivo
    # file_source = "src/archivo.txt"
    # FileCreate.paste_file(file_source)

    # # Copiar un archivo
    # file_source = "src/archivo.txt"
    # FileCreate.copy_file(file_source)

    # # Eliminar un archivo
    # file = "src/archivo.txt"
    # FileCreate.file_remove(file)

    # # Escribir en un archivo
    # file = "src/archivo.txt"
    # data = "Esto es un texto de prueba"
    # FileCreate.file_write(file, data)


    # # Leer archivo
    # file = "src/archivo.txt"
    # FileCreate.file_read(file)
    
    # # Crear directorio
    # ruta = "src"
    # FileCreate.directory_creator(ruta)

    # # Crear archivos
    # ruta = "src/ruta"
    # archivo = "Archivo.txt"
    # FileCreate.file_creator(archivo, ruta)

    # # Generar números primos
    # primes = PrimeGenerator.generate_primes(1000)
    # print("Primes up to 1000:", primes)

    # # Sistema de reservas
    # reservation_system = ReservationSystem()
    # reservation_system.add_reservation(Reservation("John Doe", "2024-10-21", "18:00", 4))
    # reservation_system.add_reservation(Reservation("Jane Smith", "2024-10-22", "19:00", 2))
    # print("\nReservations:")
    # reservation_system.show_reservations()

    # # Juego de adivinanza
    # game = GuessingGame()
    # print("\nGuess the number (1-100):")
    # guess = None
    # while guess != game.number:
    #     guess = int(input("Your guess: "))
    #     print(game.check_guess(guess))

    # # Generación de reportes
    # months = ["January", "February", "March", "April"]
    # sales_data = SalesReport.generate_sales_data(months)
    # print("\nSales Report:")
    # SalesReport.print_report(sales_data)

    # # Envío de correo electrónico
    # EmailSender.send_email("example@example.com", "Test Subject", "This is a test email body.")


#4086