# Manual de usuario — Extractor de PDF

Esta aplicación te permite cargar un archivo PDF, ver su contenido de texto en pantalla y descargarlo como archivo `.txt`.

## 1. Iniciar la aplicación

Desde la carpeta del proyecto, ejecuta:

```
uv run main.py
```

Luego abre tu navegador en:

```
http://127.0.0.1:5000
```

## 2. Cargar un PDF

1. En la parte superior de la página verás un campo para seleccionar un archivo y un botón **"Cargar PDF"**.
2. Haz clic en el campo de archivo y elige el PDF que quieras leer.
3. Presiona **"Cargar PDF"**.

Si el archivo es válido, el texto extraído aparecerá debajo del formulario.

## 3. Errores comunes

| Mensaje | Causa | Qué hacer |
|---|---|---|
| "Debes seleccionar un archivo PDF." | No se eligió ningún archivo antes de presionar el botón | Selecciona un archivo antes de cargar |
| "El archivo debe ser un PDF." | El archivo elegido no tiene extensión `.pdf` | Verifica que el archivo sea un PDF válido |
| "No se pudo leer el PDF..." | El archivo está dañado o protegido | Prueba con otro PDF o revisa que no esté corrupto |

## 4. Exportar el texto a TXT

Una vez que el contenido del PDF se muestra en pantalla, aparece un botón **"Exportar a TXT"** debajo del texto.

1. Haz clic en **"Exportar a TXT"**.
2. El navegador descargará un archivo llamado `contenido_pdf.txt` con todo el texto extraído.

## 5. Notas

- Puedes cargar un PDF distinto en cualquier momento repitiendo el paso 2; el texto mostrado se actualizará.
- El texto extraído depende de que el PDF tenga texto seleccionable (no imágenes escaneadas sin OCR).
