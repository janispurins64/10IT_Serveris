# Musu Flask serveris
from flask import Flask
from flask import request
from flask import render_template
import requests


app = Flask(__name__)
#-------------------- Šeit mūsu daļa
@app.route('/',methods=['GET','POST'])
def root():
    return render_template("tests.html")

@app.route('/dati',methods=['GET'])
def dati():
    return render_template("katevisauc.html")

@app.route('/uzruna',methods=['GET'])
def uzruna():
    vards = request.args.get("vards")
    uzvards = request.args.get("uzvards")
    print(f"Vārds= {vards}  uzvārds= {uzvards}")
    return  render_template("sveiciens.html",vards=vards,uzvards=uzvards)


#----------------------------------------
if __name__ == '__main__':
  app.run(debug=True,port=5000) # ,host='0.0.0.0' 
