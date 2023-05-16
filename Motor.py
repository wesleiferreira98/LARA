"""
     Classe: Motor
     funcao: gerencia os motores do Robo
     Autor: Weslei Ferreira Santos
     Primeira Alteracao: 03/03/2022
     Ultima Alteracao: 27/08/2022
"""
import uos
from machine import Pin, PWM
class Motor:
    """
     metodo: Construtor
     funcao: inicia os atributos da classe motor
     parametros: recebe parametros para velocidade minima e maxima e para a porta PWM
     retorno: -
    """
    def __init__(self):
        self.pinoMotor1 = Pin(5, Pin.OUT)#inicia a primeira porta para controlar o motor
        self.pinoMotor2 = Pin(4, Pin.OUT)#inicia a segunda porta para controlar o motor
         self.pinoMotor3 = Pin(6, Pin.OUT)#inicia a primeira porta para controlar o motor
        self.pinoMotor4 = Pin(7, Pin.OUT)#inicia a segunda porta para controlar o motor
        self.habilitaP = PWM(Pin(16),15000) # esta se comportara como uma porta PWM
        self.velMin = 2 # instacia a velociade minima com o valor passado por parametro
        self.velMax = 300 # instacia a velociade maxima com o valor padrao
    
    """"
     metodo: frenteMotor1
     funcao: faz o motor 1 andar para frente
     parametros: self, velocidade (int)
     retorno: -
    """
    def frenteMotor1(self,velocidade):
        self.velocidade=velocidade # instacia a velociadade que foi passada por parametro
        self.habilitaP.duty(self.duracao(self.velocidade)) # recebe o valor que foi retornado pela função duracao
        self.pinoMotor1.value(0)# desliga a porta pinoMotor2
        self.pinoMotor2.value(1)# liga a porta pinoMotor2
        
    
     """"
     metodo: frenteMotor2
     funcao: faz o motor 2 andar para frente
     parametros: self, velocidade (int)
     retorno: -
    """
    def frenteMotor2(self,velocidade):
        self.velocidade=velocidade # instacia a velociadade que foi passada por parametro
        self.habilitaP.duty(self.duracao(self.velocidade)) # recebe o valor que foi retornado pela função duracao
        self.pinoMotor3.value(0)# desliga a porta pinoMotor2
        self.pinoMotor4.value(1)# liga a porta pinoMotor2
        
    """
     metodo: trasMotor1
     @see frente(self,velocidade)
     funcao: faz o motor 1 andar para tras, definindo os pinosMotor 1 e 2 para obter o movimento para tras
     parametros: self, velocidade (int)
     retorno: -
    """
    def trazMotor1(self,velocidade):
        self.velocidade=velocidade# instacia a velociadade que foi passada por parametro
        self.habilitaP.duty(self.duracao(self.velocidade))# recebe o valor que foi retornado pela função duracao
        self.pinoMotor3.value(1)# liga a porta pinoMotor1
        self.pinoMotor4.value(0)# desliga a porta pinoMotor2
        
          
    """
     metodo: trazMotor2
     funcao: faz o motor 2 andar para tras, definindo os pinosMotor 3 e 4 para obter o movimento para tras
     parametros: self, velocidade (int)
     retorno: -
    """
    def trazMotor2(self,velocidade):
        self.velocidade=velocidade# instacia a velociadade que foi passada por parametro
        self.habilitaP.duty(self.duracao(self.velocidade))# recebe o valor que foi retornado pela função duracao
        self.pinoMotor3.value(1)# liga a porta pinoMotor1
        self.pinoMotor4.value(0)# desliga a porta pinoMotor2
        
    
        
    """
     metodo: pararMotores
     funcao: interrompe o movimento, definindo 'habilita' e pinosMotor 1,2,3 e 4 para 0
     parametros: apenas a instancia do Motor
     retorno: -
    """
    def pararMotores(self):
        self.habilitaP.duty(0)# desliga a porta habilita
        self.pinoMotor1.value(0)# desliga a porta pinoMotor1
        self.pinoMotor2.value(0)# desliga a porta pinoMotor2
        self.pinoMotor3.value(0)# liga a porta pinoMotor1
        self.pinoMotor4.value(0)# desliga a porta pinoMotor2
         
    """
     metodo: pararMotor1
     funcao: interrompe o movimento, definindo 'habilita' e pinosMotor 1 e 2 para 0
     parametros: apenas a instancia do Motor
     retorno: -
    """
    def pararMotor1(self):
        self.habilitaP.duty(0)# desliga a porta habilita
        self.pinoMotor1.value(0)# desliga a porta pinoMotor1
        self.pinoMotor2.value(0)# desliga a porta pinoMotor1
         
    """
     metodo: pararMotor2
     funcao: interrompe o movimento, definindo 'habilita' e pinosMotor 3 e 4 para 0
     parametros: apenas a instancia do Motor
     retorno: -
    """
    def pararMotor2(self):
        self.habilitaP.duty(0)# desliga a porta habilita
        self.pinoMotor3.value(0)# liga a porta pinoMotor1
        self.pinoMotor4.value(0)# desliga a porta pinoMotor2
     

    """
     metodo: duracao
     funcao: controlar a velocidade e tempo de funcionamento do motor, calculando a duracao do ciclo com base na velocidade (0-100) do motor
     parametros: self e velocidade(int) determina a velocidade
     return duracaoCiclo (int)
    """
    def duracao(self,velocidade):
        if self.velocidade <= 0 or self.velocidade > 300: #checagem de limites da velocidade (0-100)
            duracaoCiclo = 0
        else:
            duracaoCiclo = int(self.velMin + (self.velMax - self.velMin)*((self.velocidade-1)/(100-1)))
        return duracaoCiclo
        
        
        
        
