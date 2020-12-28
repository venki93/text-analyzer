# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template("mainUI.html")

def file_load(loc):
    with open(loc,"r") as file:
        return file.read().lower().split()
        
def wordCount(content):
    words=(list(set(content)))
    print(words)
    vals={}
    #outs=[]
    for word in words:
        val = str(content.count(word))
        #outs.append(word +" - "+ val)
        vals[word]=val    
    #return vals,outs
    return vals
	
@app.route('/result', methods = ['GET', 'POST'])
def load_file():
   if request.method == 'POST':
      f = request.files['file']
      if str(f.filename).endswith(".txt"):
          f.save(secure_filename(f.filename))
          val = file_load(f.filename)
          #vals,out=wordCount(val)
          out=wordCount(val)
          return render_template("success.html", name = f.filename, values = str(out))  
      else:
          return render_template("failure.html", name = f.filename)
		
if __name__ == '__main__':
   app.run()
   