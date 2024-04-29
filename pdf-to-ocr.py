from pdf2image import convert_from_path
import numpy as np
import pandas as pd
import pytesseract
import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
from PIL import Image

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
        



#lista para armazenar o texto de todas as páginas
extracao = []
pdf_file = "Documento1.pdf"
image = pdf_to_img(pdf_file)
preprocessed_image = Image.open(image)
# text = extract_text_from_image(preprocessed_image)
# extracao.append(text)
# print(extracao)

