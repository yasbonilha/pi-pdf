from pdf2image import convert_from_path
import numpy as np
import pandas as pd
import pytesseract
import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
from PIL import Image
import cv2
import os.path
import random


pytesseract.pytesseract.tesseract_cmd = r"C:\Users\bonil\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

imagens = []

#realiza a ocr na imagem passada como parâmetro e retorna o texto extraído no formato de uma string.
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text


#implementação
#passar o pdf como imagem
def pdf_to_img(pdf_file):
    doc = fitz.open(pdf_file)  # open document
    for i, page in enumerate(doc):
        pix = page.get_pixmap()  # render page to an image
        pix.save(f"page_{i}.png")
        imagem = f"page_{i}.png"
        imagens.append(imagem)
        return imagem
        


type = int(input("1 - escanear\n 2- tirar foto: "))

#escanear
#lista para armazenar o texto de todas as páginas
if type == 1 :
    extracao = []
    pdf_file = "Info sobre o pi.pdf"
    image = pdf_to_img(pdf_file)
    preprocessed_image = Image.open(image)
    text = extract_text_from_image(preprocessed_image)
    extracao.append(text)
    print(extracao)
elif type == 2:
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_name = ""

    control = True
    while control:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            control = False
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            control = False

        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(random.randint(4, 1000))
            while os.path.isfile(img_name):
                img_name = "opencv_frame_{}.png".format(random.randint(5, 1000))
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            control = False

    cam.release()
    cv2.destroyAllWindows()
    preprocessed_image = Image.open(img_name)
    text = extract_text_from_image(preprocessed_image)
    print(text)


