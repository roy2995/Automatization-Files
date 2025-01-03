import json
import re

def load_json(file_path):
    """
    Cargar el archivo JSON desde la ruta especificada.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_filename(filename):
    """
    Limpia el nombre del archivo reemplazando los caracteres no válidos.
    Los caracteres no válidos se reemplazan por guiones bajos, pero las tildes no se tocan.
    """
    # Reemplazar caracteres no válidos (como barras, asteriscos, etc.) por guion bajo
    filename = re.sub(r'[\\/*?:"<>|]', '_', filename)
    # Reemplazar los espacios por guiones bajos
    filename = filename.replace(' ', '_')
    return filename

def separar_pasos(pasos):
    """
    Separa los pasos enumerados en una lista, manejando correctamente
    los casos donde hay saltos de línea y subenumeraciones dentro de un paso.
    """
    # Expresión regular para encontrar el inicio de cada paso (número seguido de punto)
    pattern = r"(?<=\d\.)\s*(?=\D)"
    
    # Dividir los pasos usando la expresión regular
    pasos_separados = re.split(pattern, pasos.strip())
    
    # Limpiar cada paso y eliminar saltos de línea y números de pasos adicionales
    pasos_limpios = []
    for paso in pasos_separados:
        if paso.strip():  # Ignorar cadenas vacías
            # Eliminar números de pasos adicionales y saltos de línea no deseados
            paso_limpio = re.sub(r"\n\d+\.", "\n", paso.strip())
            pasos_limpios.append(paso_limpio)
    
    return pasos_limpios