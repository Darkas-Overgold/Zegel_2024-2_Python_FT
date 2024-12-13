import random
import pandas as pd
import openpyxl
# Generar datos similares
num_elements = 1500
nodos = [chr(i) for i in range(65, 91)]  # Letras de A a Z

data_similar = pd.DataFrame({
    'Nodo 1': [random.choice(nodos) for _ in range(num_elements)],
    'Nodo 2': [random.choice(nodos) for _ in range(num_elements)],
    'Distancia (km)': [random.randint(1, 20) for _ in range(num_elements)],
    'Grosor (cm)': [random.randint(5, 15) for _ in range(num_elements)],
    'Costo (USD)': [random.randint(100, 1000) for _ in range(num_elements)]
})

# Guardar en un archivo Excel (XLSX) compatible con VSCode
output_path = 'C:/Users/Alumno/Desktop/Python/Excel/Generated_Datos.xlsx'
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    data_similar.to_excel(writer, index=False)

print(f"Archivo generado en: {output_path}")