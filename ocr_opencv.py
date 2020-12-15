import cv2
import pytesseract
from PIL import Image
import numpy as np

def allowed(txt):
    ch=""
    list1=txt.split('\n')
    for j in list1:
        string=""
        for i in j:
            if ord(i)>=33 and ord(i)<127:
                string+=i
        if string!="":
            ch+=string+'\n'
    return ch

def find_contours(img):
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    x,threshold=cv2.threshold(grayimg,0,255,cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rec = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 
    dil = cv2.dilate(threshold, rec, iterations = 1) 
    contours,heirarchy = cv2.findContours(dil, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    return contours

def img_to_string(img):
    im=np.array(Image.open(img))
    im=cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    image=im.copy()
    contours=find_contours(im)
    string=""
    for i in contours:
        a,b,c,d=cv2.boundingRect(i)
        rectangle=cv2.rectangle(im,(a,b),(a+c,b+d),(0,255,0),2)
        crop_img=image[b:b+d,a:a+c]
        text=pytesseract.image_to_string(crop_img)
        print(text)
        string+=allowed(text)
    return string

