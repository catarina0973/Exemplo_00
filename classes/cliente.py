# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:36:29 2024

@author: cacfa
"""
from classes.gclass import Gclass

class Cliente(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    att=['_code','_nome','_endereco','_telemovel','_senha']
    def __init__(self, code, nome, endereco, telemovel, senha):
        super().__init__()
        self._code=code
        self._nome=str(nome)
        self._endereco=str(endereco)
        self._telemovel=telemovel
        self._senha=senha
        
        Cliente.obj[code]=self
        Cliente.lst.append(code)
    
    @property 
    def code(self):
        return self._code
    
    @property 
    def nome(self):
        return self._nome
    @nome.setter 
    def nome(self, nome):
        self._nome=nome
    @property 
    def endereco(self):
        return self._endereco
    @endereco.setter 
    def endereco(self, email):
        self._endereco=email
        
    @property 
    def telemovel(self):
        return self._telemovel
    
    @property 
    def senha(self):
        return self._senha
    @senha.setter 
    def senha(self, senha):
        self._senha=senha
    
    def clear():
        Cliente.obj.clear()
        Cliente.lst.clear()
