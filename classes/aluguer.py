"""

"""""
# Class OrderProduct
from classes.cliente import Cliente
from classes.veiculo import Veiculo
# Import the generic class
from classes.gclass import Gclass

class Aluguer(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    nkey = 2
    # class attributes, identifier attribute must be the first one on the list
    att = ['_aluguer','_placa','_dias','_preco']
    # Class header title
    header = 'Aluguer'
    # field description for use in, for example, in input form
    des = ['Código de aluguer','Placa','Número de dias','Preço']
    # Constructor: Called when an object is instantiated
    def __init__(self, aluguer, cliente, placa, dias, preco):
        super().__init__()
        # Object attributes
        # Check the order and product referential integrity
        if cliente in Cliente.lst:
            if placa in Veiculo.lst:
                self._aluguer = aluguer
                self._placa = placa
                self._dias = int(dias)
                self._preco = float(preco)
                # Add the new object to the OrderProduct list
                Aluguer.obj[placa] = self
                Aluguer.lst.append(placa)
            else:
                print('Aluguer ', placa, ' inexistente.')
        else:
            print('Aluguer', placa, ' inexistente.')
    # Object properties
    # order property getter method
    @property
    def aluguer(self):
        return self._aluguer
    # product property getter method
    @property
    def placa(self):
        return self._placa
    # quantity property getter method
    @property
    def dias(self):
        return self._dias
    # quantity property setter method
    @dias.setter
    def dias(self, dias):
        self._dias = int(dias)
    # price property getter method
    @property
    def preco(self):
        return self._preco
    # price property setter method
    @preco.setter
    def preco(self, preco):
        self._preco = float(preco)
        