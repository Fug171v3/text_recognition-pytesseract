import os
from flask import Flask, render_template, request

from pytess import *
from ocr_opencv import *


UPLOAD = '/static/uploads/'

EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

def allowed_1(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method =='POST':
        if 'file' not in request.files:
            return render_template('upload.html',msg='No file selected')
        file=request.files['file']
        print(file.filename)
        if file.filename=='':
            return render_template('upload.html',msg='No file selected')
        if file and allowed_1(file.filename):
            text=img_to_text(file)
            return render_template('upload.html',msg='Successfully processed',exstring=text)
    elif request.method =='GET':
        return render_template('upload.html')

@app.route('/upload_CV',methods=['GET','POST'])
def upload1():
    if request.method =='POST':
        if 'file' not in request.files:
            return render_template('upload1.html',msg='No file selected')
        file=request.files['file']
        if file.filename=='':
            return render_template('upload1.html',msg='No file selected')
        if file and allowed(file.filename):
            text=img_to_string(file)
            return render_template('upload1.html',msg='Successfully processed',exstring=text)
    elif request.method =='GET':
        return render_template('upload1.html')

if __name__=='__main__':
    app.run()
