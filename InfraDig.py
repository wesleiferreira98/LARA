"""
     Classe: InfraDig
     funcao: gerencia os sensor de InfraVermelho digital do robo
     Autor: Weslei Ferreira Santos
     Primeira Alteracao: 03/03/2022
     Ultima Alteracao: 27/08/2022
"""
import uos
from machine import Pin
class InfraDig:
    """
     metodo: Construtor
     funcao: inicia os atributos da classe InfraDig
     parametros: recebe parametro que indica em quais portas o sensor esta atribuido
     retorno: -
    """
    def __init__(self):
        self.portaInfra = Pin(19,Pin.IN)
    """
     metodo: haObjeto
     funcao: verifica se ha algum objeto a menos de 30 cm
     parametros: nao recebe parametros
     retorno: retorna verdadeiro caso haja objeto ou retorna falso caso contrario
    """
    def haObjeto(self):
        
        if (self.portaInfra.value() == 1):
            distancia=False
        else:
           distancia=True 
        return distancia # retorna o valor da distacia

        
