from classes.gclass import Gclass

class Cliente(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    nkey = 1
    auto_number = 0
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_endereco','_telemovel','_senha']
    # Class header title
    header = 'Cliente'
    # field description for use in, for example, in input form
    des = ['User','Endereço de e-mail','Telemóvel','Password']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, endereco, telemovel, senha):
        super().__init__()
        
        self._code=code
        self._endereco=str(endereco)
        self._telemovel=telemovel
        self._senha=senha
        
        Cliente.obj[code]=self
        Cliente.lst.append(code)
    
    
    
    @property 
    def code(self):
        return self._code
    @code.setter 
    def code(self, nome):
        self._code=nome
    @property 
    def endereco(self):
        return self._endereco
    @endereco.setter 
    def endereco(self, email):
        self._endereco=email
        
    @property 
    def telemovel(self):
        return self._telemovel
    @telemovel.setter 
    def telemovel(self, telemovel):
        self._telemovel=telemovel
    @property 
    def senha(self):
        return self._senha
    @senha.setter 
    def senha(self, senha):
        self._senha=senha
    
    def clear():
        Cliente.obj.clear()
        Cliente.lst.clear()
        
