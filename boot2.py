import os
import _thread
from time import sleep
import webrepl
import network
import SDCard
from machine import Pin, SoftSPI



ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

def MontarSD():
    spisd = SoftSPI(-1,miso=Pin(13),mosi=Pin(12),sck=Pin(14))
    sd = SDCard(spisd,Pin(27))
    vfs=os.VfsFat(sd)
    os.mount(vfs,'/classes')

def produtor():
    #MontarSD()
    do_connect()
    webrepl.start(password='82946357')
    gc.collect()

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Conectando na rede WI-FI")
        sta_if.active(True)
        sta_if.connect('Vox','CN3_42+20_MGer&@')
        while not sta_if.isconnected():
            pass
    sta_if.ifconfig(('192.168.1.32', '255.255.255.0', '192.168.1.1', '192.168.1.1'))
    print("Configuracao de rede ", ('192.168.1.32', '255.255.255.0', '192.168.1.1', '192.168.1.1'))
    

    
    
def consumidor():
    while True:
        arquivos = os.listdir()
        for nome_do_arquivo in arquivos:
           if nome_do_arquivo.endswith('.py') and nome_do_arquivo != "boot.py" and nome_do_arquivo != "SDCard.py" and nome_do_arquivo !="teste.py":
                try:
                    print("executando: ", nome_do_arquivo)
                    exec(open(nome_do_arquivo).read())
                except Exception as e:
                    print("Erro ao execultar o arquivo: ", e)
                finally:
                    os.remove(nome_do_arquivo)
           else:
              print("Nenhum arquivo foi enviado")
        sleep(5)
        

#processo produtor
produtor()

#processo consumidor
_thread.start_new_thread(consumidor,())
print("Fim de tudo")


