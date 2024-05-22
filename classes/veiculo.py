from classes.gclass import Gclass

class Veiculo(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_modelo','_ano','_valordiario', '_disponivel','_recolha']
    # Class header title
    header = 'Veículo'
    # field description for use in, for example, in input form
    des = ['Code','Modelo','Ano','Valor Diário', 'Disponível','Local de Recolha']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, modelo, ano, valordiario, disponivel, recolha):
        super().__init__()
        
        self._code=code
        self._modelo=modelo
        self._ano=ano
        self._valordiario=valordiario
        self._disponivel=disponivel
        self._recolha=recolha
        Veiculo.obj[code]=self
        Veiculo.lst.append(code)
    
    
    
    @property 
    def code(self):
        return self._code
    @code.setter 
    def code(self, nome):
        self._code=nome
    @property 
    def recolha(self):
        return self._recolha
    @recolha.setter 
    def recolha(self,local):
        self._recolha=local
    @property 
    def modelo(self):
        return self._modelo
    @modelo.setter 
    def modelo(self, model):
        self._modelo=model
        
    @property 
    def ano(self):
        return self._ano
    @ano.setter 
    def ano(self, ano):
        self._ano=ano
    @property 
    def valordiario(self):
        return self._valordiario
    @valordiario.setter 
    def valordiario(self, valordiario):
        self._valordiario=valordiario
    @property 
    def disponivel(self):
        return self._disponivel
    @disponivel.setter 
    def disponivel(self, valor):
        self._disponivel= valor
    def clear():
        Veiculo.obj.clear()
        Veiculo.lst.clear()
        
