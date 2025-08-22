import json
import csv
import io
import pandas as pd

# JSON data from the previous response (contains 50 questions)
# Using a raw string literal r"""...""" to avoid issues with backslashes
# within the string itself. JSON requires backslashes to be escaped as \\.
# Python raw strings treat backslashes literally, so we need \\ for JSON's \.
# For LaTeX's \sqrt, JSON needs \\sqrt, so the raw string needs \\sqrt.
json_data = r"""
[
  {
    "pregunta": "¿Qué tipo de error radiométrico se corrige habitualmente utilizando el algoritmo DOS (Dark Object Subtraction)?",
    "opciones": {
      "A": "Errores producidos por fallo en los detectores del sensor (bandeado)",
      "B": "Errores producidos por la dispersión y absorción atmosférica",
      "C": "Errores geométricos debidos a la rotación de la Tierra",
      "D": "Errores de moteado (speckle) en imágenes SAR"
    },
    "respuesta_correcta": "B",
    "justificación": "El algoritmo DOS se basa en la sustracción del valor del píxel más oscuro (asumiendo reflectancia cero) para corregir el efecto aditivo de la dispersión atmosférica en el histograma de la imagen. Los otros errores se corrigen con métodos diferentes (corrección de histogramas parciales para bandeado, filtros espaciales para moteado, modelos matemáticos o GCP para errores geométricos).",
    "referencia": "TEL Tema 6 Preprocesamiento y Correccion.pdf, p. 12-13, 19, 16, 64, 66"
  }
]
"""

# Load JSON data
try:
    questions = json.loads(json_data)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    # Handle error appropriately, maybe print the problematic section
    # For now, we'll exit if JSON is invalid
    exit()

# Define the CSV header
header = ["Question Text", "Question Type", "Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Correct Answer", "Time in seconds", "Image Link", "Answer explanation"]

# Create an in-memory text stream for CSV
output = io.StringIO()
writer = csv.writer(output, quoting=csv.QUOTE_ALL)

# Write the header
writer.writerow(header)

# Map for correct answer letters to option numbers
correct_answer_map = {
    "A": "1",
    "B": "2",
    "C": "3",
    "D": "4"
}

data = []

for q in questions:
    row = {
        "Question Text": q.get("pregunta", ""),
        "Question Type": "Multiple Choice",
        "Option 1": q.get("opciones", {}).get("A", ""),
        "Option 2": q.get("opciones", {}).get("B", ""),
        "Option 3": q.get("opciones", {}).get("C", ""),
        "Option 4": q.get("opciones", {}).get("D", ""),
        "Option 5": "",  # En blanco
        "Correct Answer": correct_answer_map.get(q.get("respuesta_correcta", ""), ""),
        "Time in seconds": 60,
        "Image Link": "",
        "Answer explanation": q.get("justificación", "")
    }
    data.append(row)

# Crear un DataFrame
df = pd.DataFrame(data)

# Escribirlo a un archivo Excel
df.to_excel('examen_generado.xlsx', index=False)