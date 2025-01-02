# Automatization-Files Project

Este proyecto genera archivos Word basados en una plantilla predefinida y datos dinámicos provenientes de un archivo JSON. Está diseñado para automatizar la creación de documentos con pasos de prueba y otros detalles proporcionados en formato estructurado.

---

## Estructura del Proyecto

```plaintext
/Automatization-Files
│
├── config/
│   └── data.json      # Archivo de datos JSON con los detalles dinámicos
│
├── src/
│   └── utils.py       # Funciones auxiliares como carga de JSON y limpieza de nombres
│
├── template.docx      # Plantilla de Word con marcadores de posición
├── main.py            # Script principal que genera los archivos Word
└── README.md          # Instrucciones y requerimientos del proyecto
```

---

## Requerimientos

1. **Python**: Versión 3.8 o superior.
2. **Bibliotecas necesarias**:
   - `docxtpl`: Para trabajar con plantillas de Word.
   - `re` y `json`: Módulos estándar de Python.

Instala las dependencias ejecutando:

```bash
pip install docxtpl
```

---

## Instrucciones de Uso

1. **Prepara el archivo JSON**:
   - Ubica el archivo `data.json` en la carpeta `config/`.
   - Asegúrate de que el archivo tenga una estructura como esta:

```json
{
    "const": {
        "name": "John Doe"
    },

    "file_1": {
        "title": "Ejemplo de título",
        "paso_prueba": {
            "paso_1": "Primer paso.",
            "paso_2": "Segundo paso."
        }
    }
}
```

2. **Personaliza la plantilla Word**:
   - Usa `template.docx` para definir los marcadores de posición como:
     - `{{ name }}`
     - `{{ title }}`
     - `{% for paso in paso_prueba %} - {{ paso }} {% endfor %}`

3. **Ejecuta el script**:
   - Desde la raíz del proyecto, ejecuta:

```bash
python main.py
```

4. **Archivos generados**:
   - Los archivos Word se generarán en el mismo directorio donde ejecutaste el script, con nombres basados en el campo `title` del JSON.

---

## Ejemplo de Salida

### JSON de Entrada:

```json
{
    "const": {
        "name": "John Doe"
    },

    "file_1": {
        "title": "Prueba de Retiro ATM",
        "paso_prueba": {
            "paso_1": "Seleccionar el botón Tarjeta.",
            "paso_2": "Seleccionar un retiro ATM."
        }
    }
}
```

### Documento Word Generado:

```plaintext
Nombre: John Doe
Título: Prueba de Retiro ATM

Pasos de prueba:
    - Seleccionar el botón Tarjeta.
    - Seleccionar un retiro ATM.
```

---

## Notas Adicionales

- Asegúrate de que los nombres de archivo generados no contengan caracteres no válidos (automáticamente manejado por el script).
- Puedes agregar más archivos JSON con estructura similar para generar múltiples documentos.

---

## Contribuciones

Si deseas contribuir o reportar problemas, por favor crea un issue o un pull request en el repositorio correspondiente.

---

## Autor

Proyecto desarrollado por Roderick Esquivel M.

