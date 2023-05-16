import os
import _thread
from time import sleep
import webrepl
import network
import SDCard
from machine import Pin, SoftSPI

#spisd = SoftSPI(-1,miso=Pin(13),mosi=Pin(12),sck=Pin(14))
#sd = SDCard(spisd,Pin(27))

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

def MontarSD():
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
    print("Configuracao de rede ", ('192.168.1.62', '255.255.255.0', '192.168.1.1', '192.168.1.1'))
    

    
    
def consumidor():
    while True:
        arquivos = os.listdir()
        arquiexe="-9"
        for arqui in arquivos:
            if arqui !="Motor.py" and arqui !="BME280.py"and arqui !="classes"  and arqui !="boot.py" and arqui !="Infra.py" and arqui !="Ultra.py" and arqui !="SensorLuz.py" and arqui !="webrepl_cfg.py.py" and arqui !="SDCard.py":
                arquiexe = arqui
            

        if(arquiexe != "-9"):
            print("executando: ", arquiexe)
            exec(open(arquiexe).read())
            os.remove(arquiexe)
        else:
            print("Nenhum arquivo foi enviado")
        sleep(4)
        

#processo produtor
produtor()

#processo consumidor
_thread.start_new_thread(consumidor,())
print("Fim de tudo")
