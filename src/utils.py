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
