import streamlit as st
import cv2
import numpy as np
import tempfile
import os

st.title("⭐ Generador de Circumpolares")

fotos = st.file_uploader("Sube tus fotos (JPG/PNG)", type=["jpg", "png"], accept_multiple_files=True)

if fotos:
    temp_dir = tempfile.mkdtemp()
    paths = []
    for f in fotos:
        path = os.path.join(temp_dir, f.name)
        with open(path, "wb") as out:
            out.write(f.read())
        paths.append(path)

    paths.sort()
    base = cv2.imread(paths[0])
    resultado = base.copy()

    for archivo in paths[1:]:
        img = cv2.imread(archivo)
        resultado = np.maximum(resultado, img)

    salida = os.path.join(temp_dir, "startrails.jpg")
    cv2.imwrite(salida, resultado)

    st.image(salida, caption="Circumpolar generada", use_column_width=True)
    st.download_button("Descargar imagen", data=open(salida, "rb"), file_name="startrails.jpg")
