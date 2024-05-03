# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:04:44 2024

@author: cacfa
"""

import bcrypt
from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst= list()
    pos=0
    sortkey=''
    auto_number =0
    nkey=1
    att=['_user','_usergroup','_senha']
    header= 'Login'
    des=['User', 'User group', 'Senha']
    username=''
    def __init__(self,user, usergroup, senha):
        super().__init__()
        self._user=user
        self._usergroup=usergroup
        self._senha=senha
        
        Userlogin.obj[user]=self 
        Userlogin.lst.append(user)
        

    @property 
    def user(self):
        return self._user 
    
    @property 
    def usergroup(self):
        return self._usergroup 
    
    @usergroup.setter 
    def usergroup(self, usergroup):
        self._usergroup=usergroup
    @property 
    def senha(self,senha):
        return ''
    @senha.setter 
    def senha(self, senha):
        self._senha=senha
    
    @classmethod
    def set_senha (self, senha):
        passencrypted = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        return passencrypted.decode()
    
    @classmethod
    def verificarSenha(self, user, senha) :
        Userlogin.username = ''
        if user in Userlogin.obj:
            obj = Userlogin.obj[user]
            valido = bcrypt.checkpw(senha.encode(), obj._password.encode ())
            if valido:
                Userlogin.username = user
                messagem = "Palavra-passe válida"
            else:
                messagem = 'Palavra-passe inválida'
        else:
            messagem = 'O user que introduziu não existe'
            return messagem
    
        
