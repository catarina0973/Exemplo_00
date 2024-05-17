# Class OrderProduct
from classes.cliente import Cliente
from classes.veiculo import Veiculo
import datetime
# Import the generic class
from classes.gclass import Gclass

class Aluguer(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    nkey = 2
    # class attributes, identifier attribute must be the first one on the list
    att = ['_aluguer','_placa','_dias','_preco','_datainicio','_datafinal']
    # Class header title
    header = 'Aluguer'
    # field description for use in, for example, in input form
    des = ['Código de aluguer','Placa','Número de dias','Preço', 'Data de início','Data final']
    # Constructor: Called when an object is instantiated
    def __init__(self, aluguer, cliente, placa, dias, preco_veiculo, datainicio, datafinal):
        super().__init__()
        # Object attributes
        # Check the order and product referential integrity
        if cliente in Cliente.lst:
            if placa in Veiculo.lst:
                self._aluguer = aluguer
                self._placa = placa
                self._dias = int(dias)
                self._preco_veiculo = float(preco_veiculo)
                self._datainicio = datetime.date.fromisoformat(datainicio)
                self._datafinal = datetime.date.fromisoformat(datafinal)
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
    def preco_veiculo(self):
        return self._preco_veiculo
    # price property setter method
    @preco_veiculo.setter
    def preco_veiculo(self, preco):
        self._preco_veiculo = float(preco)
    # first date getter method
    @property
    def datainicio(self):
        return self._datainicio
    # last date getter method
    @property
    def datafinal(self):
        return self._datafinal
    # first date property setter method
    @datainicio.setter
    def datainicio(self, datai):
        self._datainicio = datetime.date.fromisoformat(datai)
    # last date property setter method
    @datafinal.setter
    def datainicio(self, dataf):
        self._datafinal = datetime.date.fromisoformat(dataf)
    def preco_aluguer(self):
        p=self._preco_veiculo*self._dias
        return p
