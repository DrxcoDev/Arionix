from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

def generar_informe(nombre_archivo, datos):
    # Crear un documento PDF
    documento = SimpleDocTemplate(nombre_archivo, pagesize=letter)
    estilos = getSampleStyleSheet()
    elementos = []

    # Título
    titulo = Paragraph("Informe de Datos", estilos['Title'])
    elementos.append(titulo)

    # Crear tabla
    tabla = Table(datos)
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elementos.append(tabla)

    # Construir el PDF
    documento.build(elementos)

# Ejemplo de datos
datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Alice", 30, "Madrid"],
    ["Bob", 25, "Barcelona"],
    ["Charlie", 35, "Valencia"],
]

def init():
    name = input("Add the name for report: ")
    generar_informe(f"../../{name}.pdf", datos)

init()



