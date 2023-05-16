"""
     Classe: SensorLuz
     funcao: gerencia os sensores de luz do robo
     Autor: Weslei Ferreira Santos
     Primeira Alteracao: 08/08/2022
     Ultima Alteracao: 27/08/2022
"""

import uos
from machine import Pin
class SensorCor:
"""
     metodo: Construtor
     funcao: inicia os atributos da classe SensorCor
     parametros: recebe parametro que indica em quais portas o sensor esta atribuido
     retorno: -
 """
    def __init__(self,s0,s1,s2,s3,out):
        self.pinoS0=Pin(s0,Pin.OUT)
        self.pinoS1=Pin(s1,Pin.OUT)
        self.pinoS2=Pin(s2,Pin.OUT)
        self.pinoS3=Pin(s3,Pin.OUT)
        self.pinoOut=Pin(out,Pin.IN)

    
    """
     metodo: medePulso
     funcao: mede o tempo na qual a porta indicada ficou ligada
     parametros: recebe parametro que indica em qual porta o sensor esta atribuido
     retorno: retorna o valor do contador
   """
    def medePulso(self,porta,tempo=400):
        cont=0;
        while(porta.value()==1):
            cont=cont+1
            if (tempo == cont):
                break
        return cont
    
     """
     metodo: RetornaCorVermelha
     funcao: mede o tempo na qual a porta indicada ficou ligada
     parametros: -
     retorno: retorna o valor da cor vermelho
     """
    def RetornaCorVermelha(self):
        self.pinoS2.value(0)
        self.pinoS3.value(0)
        vermelho=medePulso(self.pinoOut)
        return vermelho
    
    """
     metodo: RetornaCorAzul
     funcao: mede o tempo na qual a porta indicada ficou ligada
     parametros: -
     retorno: retorna o valor da cor azul
     """
    def RetornaCorAzul(self):
        self.pinoS2.value(0)
        self.pinoS3.value(1)
        azul=medePulso(self.pinoOut)
        return azul
    """
     metodo: RetornaCorBranco
     funcao: mede o tempo na qual a porta indicada ficou ligada
     parametros: -
     retorno: retorna o valor da cor branca
     """
    def RetornaCorBranco(self):
        self.pinoS2.value(1)
        self.pinoS3.value(0)
        branco=medePulso(self.pinoOut)
        return branco
    """
     metodo: RetornaCorVerde
     funcao: mede o tempo na qual a porta indicada ficou ligada
     parametros: -
     retorno: retorna o valor da cor verde
     """    
    def RetornaCorVerde(self):
        self.pinoS2.value(1)
        self.pinoS3.value(1)
        verde=medePulso(self.pinoOut)
        return verde
    
    
        
        
        
    
