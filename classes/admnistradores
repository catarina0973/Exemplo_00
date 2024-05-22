from classes.gclass import Gclass

class Admnistradores(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    nkey = 1
    auto_number = 0
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_senha']
    # Class header title
    header = 'Admnistrador'
    
    # field description for use in, for example, in input form
    des = ['User','Password']
    # Constructor: Called when an object is instantiated
    def __init__(self, code,senha):
        super().__init__()
        # Object attributes
        self._code = code
        
        self._senha = senha
        
        Admnistradores.obj[code] = self
        Admnistradores.lst.append(code)

    # Object properties
    # getter methodes
  
    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, name):
        self._code = name
    @property 
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, senha):
        self._senha = senha
        
    def clear():
        Admnistradores.obj.clear()
        Admnistradores.lst.clear()
