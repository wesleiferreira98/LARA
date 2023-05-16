"""
     Classe: SensorLuz
     funcao: gerencia os sensores de luz do robo
     Autor: Weslei Ferreira Santos
     Primeira Alteracao: 03/03/2022
     Ultima Alteracao: 27/08/2022
"""
from machine import ADC, Pin

class SensorLuz:
    """
         metodo: Construtor
         funcao: inicia os atributos da classe SensorLuz
         parametros: recebe parametro que indica em qual porta o sensor esta atribuido
         retorno: -
    """
    def __init__(self):
        self.portaLuz1= Pin(32,Pin.IN)
        self.portaLuz2=Pin(25,Pin.IN)
        self.portaLuz3=Pin(15,Pin.IN)
        
        self.portaLuzADC1 = ADC(self.portaLuz1)
        self.portaLuzADC1.atten(ADC.ATTN_11DB)
        self.portaLuzADC1.width(ADC.WIDTH_12BIT)
        
        self.portaLuzADC2 = ADC(self.portaLuz2)
        self.portaLuzADC2.atten(ADC.ATTN_11DB)
        self.portaLuzADC2.width(ADC.WIDTH_12BIT)
        
        self.portaLuzADC3 = ADC(self.portaLuz3)
        self.portaLuzADC3.atten(ADC.ATTN_11DB)
        self.portaLuzADC3.width(ADC.WIDTH_12BIT)
    """
     metodo: RetornaValorLuz
     funcao: retorna o valor lido pelo sensor 1
     parametros: -
     retorno: retorna o valor da intensidade de luz
    """
    def RetornaValorLuzSensor1(self):
        leitura = self.portaLuzADC1.read()
        leitura = leitura * 3.3 / 4095
        return int(leitura * 1023 // 3.3)
    
    """
     metodo: RetornaValorLuzSensor2
     funcao: retorna o valor lido pelo sensor 2
     parametros: -
     retorno: retorna o valor da intensidade de luz
    """
    def RetornaValorLuzSensor2(self):
        leitura = self.portaLuzADC2.read()
        leitura = leitura * 3.3 / 4095
        return int(leitura * 1023 // 3.3)
        
    """
     metodo: RetornaValorLuzSensor3
     funcao: retorna o valor lido pelo sensor 3
     parametros: -
     retorno: retorna o valor da intensidade de luz
    """
    def RetornaValorLuzSensor3(self):
        leitura = self.portaLuzADC3.read()
        leitura = leitura * 3.3 / 4095
        return int(leitura * 1023 // 3.3)
        
    """
     metodo: ligarSensor1
     funcao: habilita o sensor 1
     parametros: -
     retorno: -
    """
    
    def ligarSensor1(self):
        self.portaLuz1.value(1)
        
    """
     metodo: desligarSensor1
     funcao: desabilita o sensor 1
     parametros: -
     retorno: -
    """
    def desligarSensor1(self):
        self.portaLuz1.value(0)
        
    """
     metodo: ligarSensor2
     funcao: habilita o sensor 2
     parametros: -
     retorno: -
    """
    
    def ligarSensor2(self):
        self.portaLuz2.value(1)
        
    """
     metodo: desligarSensor2
     funcao: desabilita o sensor 2
     parametros: -
     retorno: -
    """
    def desligarSensor2(self):
        self.portaLuz2.value(0)
    
    """
     metodo: ligarSensor3
     funcao: habilita o sensor 3
     parametros: -
     retorno: -
    """
    
    def ligarSensor3(self):
        self.portaLuz3.value(1)
        
    """
     metodo: desligarSensor3
     funcao: desabilita o sensor 3
     parametros: -
     retorno: -
    """
    def desligarSensor3(self):
        self.portaLuz3.value(0)
    
        
