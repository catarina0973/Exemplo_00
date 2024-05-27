from classes.cliente import Cliente
from datafile import filename
import datetime
# Import the generic class
from classes.gclass import Gclass
from classes.veiculo import Veiculo
from classes.cliente import Cliente
from classes.userlogin import Userlogin

class Aluguer(Gclass):
    obj = dict()
    
    iobj =dict()
    fobj=dict()
    lst = list()
    ilist=list()
    flist=list()
    pos = 0
    sortkey = ''
    nkey = 1
    auto_number = 0
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_user','_dias','_datainicio','_datafinal','_precodiario','_precototal','_recolha']
    # Class header title
    header = 'Aluguer'
    # field description for use in, for example, in input form
    des = ['Modelo','User','Número de dias', 'Data de início (AAAA-MM-DD)','Data final (AAAA-MM-DD)','Preço Diário','Preço Total (preço diário*nº de dias)','Local de Recolha']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, user, dias,  datainicio, datafinal, precodiario, precototal,recolha):
        super().__init__()
        # Object attributes
        # Check the order and product referential integrity
        
        self._code=code #o code é o modelo do veiculo
        self._user = user
        self._dias = int(dias)
        self._precodiario = precodiario
        self._precototal = precototal
        self._datainicio = datetime.date.fromisoformat(datainicio)
        self._datafinal = datetime.date.fromisoformat(datafinal)
        self._recolha=recolha
        Aluguer.ilist.append(datetime.date.fromisoformat(datainicio))
        Aluguer.flist.append(datetime.date.fromisoformat(datafinal))
        Aluguer.obj[code] = self
        Aluguer.lst.append(code)
        
        
        
    @property
    def recolha(self):
        return self._recolha
    @recolha.setter
    def recolha(self,local):
        self._recolha=local
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self,user):
        self._coder=user
    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, user):
        self._user = user
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
    def precodiario(self):
        
        return self._precodiario
    # price property setter method
    @precodiario.setter
    def precodiario(self, preco):
        self._precodiario = float(preco)
    @property
    def precototal(self):
        
        return self._precototal
    # price property setter method
    @precodiario.setter
    def precototal(self, preco):
        self._precototal = float(preco)
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
    def datafinal(self, dataf):
        self._datafinal = datetime.date.fromisoformat(dataf)
    
    
    def chk_validity(self):
        message = 'Aprovado!'
        
        if self._code not in Veiculo.obj.keys():            
            return 'Veículo não encontrado!'
            Aluguer.ilist.remove(self._datainicio)
            Aluguer.flist.remove(self._datafinal)
        elif self._user not in Userlogin.obj.keys():
            Aluguer.ilist.remove(self._datainicio)
            Aluguer.flist.remove(self._datafinal)
            return 'User não encontrado!'
        elif (self._datafinal - self._datainicio).days != int(self._dias):
            return 'As datas não correspondem ao número de dias!'
        
        elif Aluguer.lst.count(self._code)>1 and (Aluguer.flist.count(self._datafinal)>1 or Aluguer.ilist.count(self._datainicio)>1 ):
            message=f'O veículo já está alugado de {self._datainicio} a {self._datafinal}'
            Aluguer.ilist.remove(self._datainicio)
            Aluguer.flist.remove(self._datafinal)
            Aluguer.lst.remove(self._code)
        elif self._recolha != Veiculo.robj.get(self._code):
            Aluguer.ilist.remove(self._datainicio)
            Aluguer.flist.remove(self._datafinal)
            return f'Local de recolha: {Veiculo.robj.get(self._code)}'
        
        self._precototal = float(Veiculo.vobj[self._code]) * int(self._dias)
        self._precodiario = Veiculo.vobj[self._code]
        
        return message
