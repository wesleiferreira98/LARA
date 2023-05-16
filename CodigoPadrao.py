"""
esses imports sao obrigatorios em todos os codigos que serão submetidos ao ESP
Em outras palavras essa e a estrutura basica dos codigos que sao ennviados ao ESP

"""
import sys
sys.path.insert(1,'/classes')
import Pacotes
led = Pin(2, Pin.OUT)

def rotina(execucaoMin):
    execucaoSec = execucaoMin * 60 # converte o tempo de minutos para segudos
    while execucaoSec: # executa o programa conforme o tempo definido pelo usuario
        # Aqui e onde deve ser inserida toda a rotina do robo
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(0.5)
        execucaoSec -= 1 #nao apague essa linha
        
    print('programa finalizado.') # aparace quando o programa é finalizado


rotina(2)# chama a rotina passando o tempo de execucao dentro dos parenteses
   

    
