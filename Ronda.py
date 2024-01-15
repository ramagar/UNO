from random import randint

class Ronda():
    '''
    Clase que permite generar una Ronda con el numero de ronda actual
    
    Atributos:
    - __numeroRonda (int): Numero de la ronda acutal
    - __rondaEspecial (bool): Booleano que cuando es ronda especial se le asigna True, de lo contrario False
    '''
    
    def __init__(self, numeroRonda:int=1) -> None:
        '''
        Constructor de la clase Ronda
        
        Parametros:
        - numeroRonda (int): numero de la ronda. Default = 1
        '''
        
        self.__numeroRonda:int = numeroRonda
        '''Numero de la ronda acutal'''
        self.__rondaEspecial:bool = bool()
        '''Booleano que cuando es ronda especial se le asigna True, de lo contrario False'''
        
    def setNumeroRonda(self, numeroRonda:int=1) -> None:
        '''Metodo que define el numero de la ronda'''
        self.__numeroRonda = numeroRonda
        
    def getNumeroRonda(self) -> int:
        '''Metodo que devuelve el numero de la ronda'''
        return self.__numeroRonda
    
    def setRondaEspecial(self) -> None:
        '''Metodo que define True si es ronda especial (25%) y False si es ronda normal (75%)'''
        if randint(1, 4) == 1:
            self.__rondaEspecial = True
        else:
            self.__rondaEspecial = False
        
    def getRondaEspecial(self) -> bool:
        '''Metodo que devuelve True si es ronda especial, de lo contrario devuelve False'''
        return self.__rondaEspecial