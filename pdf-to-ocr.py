from pdf2image import convert_from_path
import numpy as np
import pandas as pd
import pytesseract
import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons


#corrige a orientação das imagens - tem como parametro a imagem e retorna distorcida
# def deskew(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     gray = cv2.bitwise_not(gray)
#     coords = np.column_stack(np.where(gray > 0))
#     angle = cv2.minAreaRect(coords)[-1]
    
#     if angle < -45:
#         angle = -(90 + angle)
#     else:
#         angle = -angle

#     (h, w) = image.shape[:2]
#     center = (w // 2, h // 2)
#     M = cv2.getRotationMatrix2D(center, angle, 1.0)
#     rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

#     return rotated


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
        image = pix.save(f"page_{i}.png")
        return image


#lista para armazenar o texto de todas as páginas
extracao = []
pdf_file = r"Documento1.pdf"
image = pdf_to_img(pdf_file)
preprocessed_image = image
text = extract_text_from_image(preprocessed_image)
extracao.append(text)
print(extracao)

