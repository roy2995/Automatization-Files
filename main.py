import os
import re
from Funciones_Ex import Funexcel
from docxtpl import DocxTemplate
from src.utils import load_json, clean_filename, separar_pasos

def main():
    # Cargar los datos desde el JSON
    #data = load_json("config/data.json")
    
    #Especificar la ruta de la carpeta donde se guardarán los archivos
    output_folder = "C:\\Users\\JuanNav\\OneDrive - Money Free Flex\\Documentos\\Money Free Flex\\Pruebas\\entregable 6\\android"

    # Crear la carpeta si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    fe = Funexcel()
    #Ruta donde se encuentra el excel
    ruta = "C:\\Users\\JuanNav\\OneDrive - Money Free Flex\\Documentos\\Money Free Flex\\Pruebas\\entregable 6\\entregable6_v2.xlsx"
    fila_min = 12
    sheetName = "MP"
    fila_max = fe.get_row_count(ruta, sheetName)
    col_id = 3
    col_plat = 4
    col_modulo = 5
    col_caso = 7
    col_pasos = 9
    
    

    # Iterar sobre las claves del JSON para agregar dinámicamente las secciones file_*
    
    for fcaso in range(12, 36):
        id = fe.read_data(ruta, sheetName, fcaso, col_id)
        plat = fe.read_data(ruta, sheetName, fcaso, col_plat)
        modulo = fe.read_data(ruta, sheetName, fcaso, col_modulo)
        nombre_caso = fe.read_data2(ruta, sheetName, fcaso, col_caso)
        pasos = fe.read_data(ruta, sheetName, fcaso, col_pasos)
        
        if(id < 10):
            id_t = "00" + str(id)
        elif(id <100):
            id_t = "0" + str(id)
        else:
            id_t = str(id)
        
        # Crear un contexto específico para este file_*
        title = modulo + " - " + nombre_caso
        lista_pasos = separar_pasos(pasos)
        
        context = {
                'name': "por confirmar",
                'title': title,
                'caso': nombre_caso,
                'paso_prueba': pasos
            }
        
        # Cargar la plantilla de Word
        file = DocxTemplate("TestFile.docx")
        
        # Rellenar la plantilla con los datos del contexto
        file.render(context)
        
        # Limpiar el nombre del archivo
        clean_title = clean_filename(f"FormatoDeEvidencia_CP_{id_t}_{plat.lower()}")
        output_filename = os.path.join(output_folder,f"{clean_title}.docx")
        
        # Guardar el archivo con el nombre correspondiente
        file.save(output_filename)

        print(f"Archivo guardado como: {output_filename}")
        #print(lista_pasos)

if __name__ == "__main__":
    main()