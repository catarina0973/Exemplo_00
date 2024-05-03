# Class Product
# Import the generic class
from classes.gclass import Gclass

class Veiculo(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_placa','_modelo','_ano','_valorDiario','_disponivel']
    # Class header title
    header = 'Veículos'
    # field description for use in, for example, in input form
    des = ['Placa','Modelo','Ano','Valor Diário','Disponível']
    # Constructor: Called when an object is instantiated
    def __init__(self, placa, modelo, ano, valorDiario, disponivel):
        super().__init__()
        self._placa = placa
        self._modelo = modelo
        self._ano = int(ano)
        self._valorDiario = float(valorDiario)
        self._disponivel=bool(disponivel)
        # Add the new object to the Product list
        Veiculo.obj[placa] = self
        Veiculo.lst.append(placa)
    # Object properties
    # placa property getter method
    @property
    def placa(self):
        return self._placa
    # modelo property getter method
    @property
    def modelo(self):
        return self._modelo
    # ano property getter method
    @property
    def ano(self):
        return self._ano
    # valorDiario property getter method
    @property
    def valorDiario(self):
        return self._valorDiario
    # disponivel property getter method
    @property
    def disponivel(self):
        return self._disponivel
    # valorDiario property setter method
    @valorDiario.setter
    def valorDiario(self, valorDiario):
        self._valorDiario = valorDiario
    # disponivel property setter method
    @disponivel.setter
    def disponivel(self, disponivel):
        self._disponivel=disponivel


