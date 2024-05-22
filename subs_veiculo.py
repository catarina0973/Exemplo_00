# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:51:47 2024

@author: cacfa
"""


from flask import Flask, render_template, request, session
from classes.userlogin import Userlogin

def veiculo():
    return render_template("veiculo.html",ulogin=session.get("user"), usergroup=session.get('usergroup'))
def veiculo1():
    return render_template("veiculo1.html",ulogin=session.get("user"), usergroup=session.get('usergroup'))