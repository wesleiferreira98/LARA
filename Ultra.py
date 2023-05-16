"""
     Classe: Ultra
     funcao: gerencia os sensor de Ultra Sonico  do robo
     Autor: Weslei Ferreira Santos
     Primeira Alteracao: 03/03/2022
     Ultima Alteracao: 27/08/2022
"""
import uos
from machine import Pin
class Ultra:
    """
     metodo: Construtor
     funcao: inicia os atributos da classe Ultra
     parametros: recebe parametro que indica em quais portas o sensor esta atribuido
     retorno: -
    """
    def __init__(self,tr,echo):
        self.trigger = machine.Pin(tr)
        self.echo = machine.Pin(echo)
        self.VelocidadeSom = 340
    """
     metodo: iniciaSensor
     funcao: inicia o sensor UltraSonico
     parametros: nao recebe parametros
     retorno: nao retorna valores
    """
    def iniciaSensor(self):
        self.trigger.Pin(1)
        self.echo.Pin(1)
    """
     metodo: calculaDistancia
     funcao: cacula a distancia obitida pelo sensor
     parametros: nao recebe parametros
     retorno: retorna a distancia calculada
    """
    def calculaDistaciaUltra(self):
        self.iniciaSensor(self)
        distancia = (100*self.VelocidadeSom)/2
        return distancia

