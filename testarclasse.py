# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:38:23 2024

@author: cacfa
"""

from datafile import filename

from classes.veiculo import Veiculo

Veiculo.read(filename + 'business.db')

cname = "Veiculo"
cl = eval(cname)

obj = cl('','','','')

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

