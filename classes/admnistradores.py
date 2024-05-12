# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 08:36:44 2024

@author: cacfa
"""

from classes.gclass import Gclass
import datetime
class Admnistradores(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    att=['_nome','__senha']
    def __init__(self, nome,senha):
        super().__init__()
        
        self._nome=str(nome)
        
        self._senha=senha
        Admnistradores.obj[nome]=self
        Admnistradores.lst.append(nome)
    
    
    @property 
    def nome(self):
        return self._nome
    
    @property 
    def senha(self):
        return self._senha
    @senha.setter 
    def senha(self, senha):
        self._senha=senha
    
    def clear():
        Admnistradores.obj.clear()
        Admnistradores.lst.clear()
        

