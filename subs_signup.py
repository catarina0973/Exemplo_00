# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:09:18 2024

@author: cacfa
"""

from flask import render_template, request, session
from classes.userlogin import Userlogin

def signup():
    return render_template("signup.html", user="", usergroup="", password="", ulogin=session.get("user"), resul="")

def chkregister():
    user = request.form["user"]
    usergroup = request.form["usergroup"]
    password = request.form["password"]
    
    # Check if user already exists
    if user in Userlogin.obj:
        resul = "User already exists."
        return render_template("signup.html", user=user, usergroup=usergroup, password=password, ulogin=session.get("user"), resul=resul)
    else:
    # Create and add new user
        new_user = Userlogin(user, usergroup, Userlogin.set_password(password))
        Userlogin.obj[user] = new_user
        Userlogin.insert(user)
        Userlogin.lst.append(user)
        resul = "Registration successful."
        
        # Log in the new user
        session["user"] = user
        session["usergroup"] = usergroup
        
        return render_template("login.html", ulogin=session.get("user"), usergroup=session.get('usergroup'))