# Generador de examen (a.py)

Descripción
- Script en Python que convierte una lista de preguntas en formato JSON a un archivo Excel (`examen_generado.xlsx`).
- Cada pregunta debe tener campos: `pregunta`, `opciones` (A..D), `respuesta_correcta`, `justificación`, `referencia`.

Requisitos
- Python 3.8+
- Dependencias: pandas, openpyxl
  - Instalar: `pip install pandas openpyxl`

Uso
1. Abrir `a.py`.
2. Reemplazar la variable `json_data` con el JSON de preguntas (ejemplo abajo).
3. Ejecutar desde PowerShell o CMD en Windows:
   - `python a.py`
4. Se generará `examen_generado.xlsx` en la misma carpeta.

Ejemplo de `json_data` (ejemplo completado)
- Copiar este bloque y pegarlo como el valor de la variable `json_data` en `a.py` (con las comillas r""" ... """):

```json
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
    "justificación": "El algoritmo DOS se basa en la sustracción del valor del píxel más oscuro para corregir el efecto aditivo de la atmósfera.",
    "referencia": "TEL Tema 6 Preprocesamiento y Correccion.pdf, p. 12-13"
  },
  {
    "pregunta": "¿Cuál es la principal ventaja de realizar una corrección radiométrica absoluta?",
    "opciones": {
      "A": "Mejora la resolución espacial de la imagen",
      "B": "Permite comparar reflectancias entre imágenes tomadas en distintas fechas",
      "C": "Elimina completamente el ruido de la imagen",
      "D": "Corrige errores geométricos por movimiento de la plataforma"
    },
    "respuesta_correcta": "B",
    "justificación": "La corrección radiométrica absoluta transforma valores digitales a unidades físico-espectrales, permitiendo comparaciones entre escenas.",
    "referencia": "Manual de teledetección, capítulo de correcciones radiométricas"
  }
]
```

Notas
- Mantener la estructura de claves exacta para que el script mapee correctamente las opciones y la respuesta.
- Si añade más opciones (E, F...), actualizar el script para incluirlas en el CSV/Excel.