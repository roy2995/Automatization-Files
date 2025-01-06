import re
from openpyxl import load_workbook

def clean_filename(filename):
    """
    Limpia el nombre del archivo reemplazando caracteres no válidos.
    """
    filename = re.sub(r'[\\/*?:"<>|]', '_', filename)
    filename = filename.replace(' ', '_')
    return filename

def load_excel_with_formulas(file_path, sheet_name, cell_ranges):
    """
    Carga datos de un archivo Excel, obteniendo el valor calculado de celdas con fórmulas.
    """
    try:
        workbook = load_workbook(file_path, data_only=True)  # Leer el archivo Excel con valores calculados
        sheet = workbook[sheet_name]
        # Extraer los valores de las celdas especificadas
        return {key: sheet[cell].value for key, cell in cell_ranges.items()}
    except PermissionError as e:
        print(f"Error de permisos al leer el archivo Excel: {e}")
    except FileNotFoundError as e:
        print(f"Archivo Excel no encontrado: {e}")
    except Exception as e:
        print(f"Error general al leer el archivo Excel: {e}")
    return None

def split_steps(steps_text):
    """
    Divide un texto de pasos en una lista de pasos individuales.
    """
    steps = re.split(r'\d+\.', steps_text)  # Divide en base a números seguidos de puntos
    return [step.strip() for step in steps if step.strip()]
