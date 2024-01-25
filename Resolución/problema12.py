nombre_archivo = input("Ingrese el nombre del archivo: ")

if '.' in nombre_archivo:
    sufijo = nombre_archivo.split('.')[-1].lower()
else:
    sufijo = None

tipos_mimes = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

tipo_mime = tipos_mimes.get(sufijo, 'application/octet-stream')

print("Tipo de archivo MIME:", tipo_mime)
