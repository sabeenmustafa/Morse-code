from flask import Flask, render_template, Response,request
import os
from werkzeug.utils import secure_filename
#from test import Camera
#from test import Detectmorse
#import testflask
from testflask import *
from testcopy import *
import time
from lip import *

app = Flask(__name__)
#morse = Detectmorse()

@app.route('/',methods=['GET'])
@app.route('/index.html')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/contact.html')
def something():
    return render_template('contact.html')

@app.route('/about.html')
def something1():
    return render_template('about.html')

@app.route('/eye.html')
def eye():
    return render_template('eye.html')

@app.route('/eye1.html')
def eye1():
    return render_template('eye1.html')

@app.route('/morse.html')
def morse():
    return render_template('morse.html')

@app.route('/morse1.html')
def morse1():
    test()
    return render_template('morse1.html')

@app.route('/morse2.html')
def morse2():
    return render_template('morse2.html')
	
@app.route('/lip.html')
def lip():
	return render_template('lip.html')
	
@app.route('/lip1.html')
def lip1():
	mouth()
	return render_template('lip1.html')

#UPLOAD_FOLDER="D:/Palak/minor/EyeMorseCode"
#ALLOWED_EXTENSIONS={'mp4','mov','mkv','avi','wmv'}
#app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

#def allowedFile(filename):
    #return '.' in filename and \
           #filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader',methods=['GET'])
def upload_file():
    file=request.args.get('file')
    test1(file)
    return file

if __name__ == '__main__':
    app.run(debug=True)
