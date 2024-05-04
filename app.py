from flask import Flask, render_template, request, session
from datafile import filename

import os

from classes.cliente import Cliente
from classes.admnistradores import Admnistradores
from classes.veiculo import Veiculo
from classes.recolha import Recolha
from classes.aluguer import Aluguer
from classes.userlogin import Userlogin

app = Flask(__name__)

Cliente.read(filename + 'business.db')
Admnistradores.read(filename + 'business.db')
Veiculo.read(filename + 'business.db')
Userlogin.read(filename + 'business.db')
Aluguer.read(filename + 'business.db')
Recolha.read(filename + 'business.db')
prev_option = ""
submenu = ""
app.secret_key = 'BAD_SECRET_KEY'

upload_folder = os.path.join('static', 'ProductFotos')
app.config['UPLOAD'] = upload_folder


import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub



@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()
@app.route("/signup")
def signup():
    return lsub.signup()
@app.route("/submenu", methods=["post","get"])
def getsubm():
    global submenu
    submenu = request.args.get("subm")
    return render_template("index.html", ulogin=session.get("user"),submenu=submenu)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
    submenu = request.args.get("subm")
    return gfsub.gform(cname,submenu)

@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    submenu = request.args.get("subm")
    return gfTsub.gformT(cname,submenu)


@app.route("/uc", methods=["post","get"])
def uc():
    return render_template("uc.html", ulogin=session.get("user"),submenu=submenu)



    
if __name__ == '__main__':
    app.run(debug=True,port=6001)
    #app.run()
