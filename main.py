import os
from docxtpl import DocxTemplate
from src.utils import load_json, clean_filename

def main():
    # Cargar los datos desde el JSON
    data = load_json("config/data.json")

    # Iterar sobre las claves del JSON para agregar dinámicamente las secciones file_*
    for key, value in data.items():
        if key.startswith('file_'):
            # Crear un contexto específico para este file_*
            context = {
                'name': data['const']['name'],
                'title': value['title'],
                'paso_prueba': value['paso_prueba']
            }

            # Cargar la plantilla de Word
            file = DocxTemplate("TestFile.docx")

            # Rellenar la plantilla con los datos del contexto
            file.render(context)

            # Limpiar el nombre del archivo
            clean_title = clean_filename(value['title'])
            output_filename = f"{clean_title}.docx"

            # Guardar el archivo con el nombre correspondiente
            file.save(output_filename)

            print(f"Archivo guardado como: {output_filename}")

if __name__ == "__main__":
    main()
