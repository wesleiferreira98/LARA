"""
     Classe: Infra
     funcao: gerencia os sensor de InfraVermelho do robo
     Autor: Weslei Ferreira Santos
     Primeira Alteracao: 03/03/2022
     Ultima Alteracao: 27/08/2022
"""
import uos
from machine import Pin
class Infra:
    """
     metodo: Construtor
     funcao: inicia os atributos da classe Infra
     parametros: recebe parametro que indica em quais portas o sensor esta atribuido
     retorno: -
    """
    def __init__(self):
        self.portaADC = ADC(34)
        self.portaLuzADC.atten(ADC.ATTN_11DB)
    """
     metodo: calculaDistancia
     funcao: cacula a distancia obitida pelo sensor
     parametros: nao recebe parametros
     retorno: retorna a distancia calculada
    """
    def calculaDistancia(self):
        valorVolts = self.portaADC.read() * 0.0048828125 # ler o valor da tensao na porta indicada
        distancia = 4800/(valorVolts*200-20) # calcula a distancia e armazena na variavel distancia
        return distancia # retorna o valor da distacia

        
