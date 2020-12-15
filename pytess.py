import pytesseract
from PIL import Image

def ocr(im):
    config = ('-l eng --oem 1 --psm 3')
    str1 = pytesseract.image_to_string(im, config=config)
    list1 = str1.split('\n')
    return list1

def img_to_text(img):
    im = Image.open(img)
    list1=ocr(im)
    a=""
    print(list1)
    for i in list1:
        a+=i+'\n'
    return a
           
