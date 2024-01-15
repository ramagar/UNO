class Jugador():
    '''
    Clase que permite generar un Jugador con su nombre y puntaje
    
    Atributos:
    - __jugador (dict): Diccionario que almacena el nombre del jugador y sus puntos
    - __jugadorRondaAnterior (dict): Diccionario que almacena el nombre del jugador y sus puntos en la ronda anterior
    '''
    
    def __init__(self, nombre:str, puntos:int|float=0) -> None:
        '''
        Contructor de la clase Jugador
        
        Parametros:
        - nombre (str): El nombre del jugador
        - puntos (int|float): Los puntos del jugador. Default = 0
        '''
        
        self.__jugador:dict = {nombre:puntos}
        '''Diccionario que almacena el nombre del jugador y sus puntos'''
        self.__jugadorRondaAnterior:dict = {nombre:puntos}
        '''Diccionario que almacena el nombre del jugador y sus puntos en la ronda anterior'''
         
    def setPuntos(self, nombre:str, puntos:int|float=0) -> None:
        '''Metodo que define los puntos del jugador, por defecto es 0'''
        self.__jugador = {nombre:puntos}
    
    def setPuntosRondaAnterior(self, nombre:str, puntos:int|float=0) -> None:
        '''Metodo que define los puntos del jugador la ronda anterior, por defecto es 0'''
        self.__jugadorRondaAnterior = {nombre:puntos}
        
    def getPuntos(self) -> int|float:
        '''Metodo que devuelve los puntos del jugador'''
        return list(self.__jugador.values())[0]
    
    def getPuntosRondaAnterior(self) -> int|float:
        '''Metodo que devuelve los puntos del jugador la ronda anterior'''
        return list(self.__jugadorRondaAnterior.values())[0]
    
    def getNombre(self) -> str:
        '''Metodo que devuelve el nombre del jugador'''
        return list(self.__jugador.keys())[0]