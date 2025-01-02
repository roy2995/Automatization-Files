import os
from docxtpl import DocxTemplate
from src.utils import load_json, clean_filename

def main():
    # Cargar los datos desde el JSON
    data = load_json("config/data.json")

    # Crear la carpeta "Files" si no existe
    output_dir = "Files"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterar sobre las claves del JSON para agregar dinámicamente las secciones file_*
    for key, value in data.items():
        if key.startswith('file_'):
            # Crear un contexto específico para este file_*
            context = {
                'name': data['const']['name'],
                'title': value['title'],
                # Convertir el diccionario de pasos en una lista para usar en la plantilla
                'paso_prueba': [step for step in value['paso_prueba'].values()]
            }

            # Cargar la plantilla de Word
            file = DocxTemplate("TestFile.docx")

            # Rellenar la plantilla con los datos del contexto
            file.render(context)

            # Limpiar el nombre del archivo
            clean_title = clean_filename(f"FormatoDeEvidencia_CP_{value['id']}_{value['platform']}")
            output_filename = os.path.join(output_dir, f"{clean_title}.docx")

            # Guardar el archivo con el nombre correspondiente
            file.save(output_filename)

            print(f"Archivo guardado como: {output_filename}")

if __name__ == "__main__":
    main()
