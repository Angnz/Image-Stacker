import cv2
import numpy as np
import glob

# Carpeta donde están tus fotos (JPG)
ruta = "fotos/*.jpg"

# Cargamos la primera imagen como base y aseguramos orden cronologico
imagenes = glob.glob(ruta)
imagenes.sort()  

if not imagenes:
    raise Exception("No se encontraron fotos en la carpeta.")

base = cv2.imread(imagenes[0])
resultado = base.copy()

# Recorremos el resto de fotos y aplicamos "lighten blend"
for archivo in imagenes[1:]:
    img = cv2.imread(archivo)
    resultado = np.maximum(resultado, img)

#save the crap
cv2.imwrite("startrails.jpg", resultado)
print("Imagen circumpolar guardada como startrails.jpg")
