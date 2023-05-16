# LARA
Aqui estão as classes desenvolvidas para o projeto LARA. O objetivo dessas classes é fornecer um bom nivel de abstração para que iniciantes em programação em computadores não se sintam intimidados com 
sitanxes que pareçam extremamente complexas. Essas classes foram desenvolvidas para serem usadas em microcontroladores com ESP32 e com o framework micropython
---

# Instalando MicroPython no ESP32

## Pré-requisitos:

1. Python 3.4 ou superior instalado no seu sistema.
2. Um módulo ESP32.

## Instruções de Instalação:

### 1. Instale a ferramenta esptool.py

Esta ferramenta é usada para interagir com o bootloader do ESP32. Você pode instalá-la usando pip, o gerenciador de pacotes do Python. No terminal, execute:

```shell
pip install esptool
```

### 2. Baixe o firmware MicroPython

Baixe o firmware do MicroPython para ESP32. Você pode encontrar o firmware mais recente na [página de download do MicroPython](https://micropython.org/download/ESP32/). Escolha o apropriado para o seu módulo ESP32.

### 3. Conecte o ESP32 ao seu computador

Use um cabo USB para conectar o ESP32 ao seu computador.

### 4. Apague o flash no ESP32

Primeiro, você deve descobrir qual porta serial seu ESP32 está usando. Em sistemas Linux e macOS, você pode usar o comando `ls /dev/tty.*` para listar as portas disponíveis. No Windows, você pode verificar no Gerenciador de Dispositivos.

Após identificar a porta, execute o seguinte comando para apagar o flash:

```shell
esptool.py --port /dev/tty.SERIAL_PORT erase_flash
```

Substitua `SERIAL_PORT` pela porta que você identificou.

### 5. Instale o firmware MicroPython

Após apagar o flash, você pode instalar o firmware MicroPython. Use o seguinte comando:

```shell
esptool.py --chip esp32 --port /dev/tty.SERIAL_PORT write_flash -z 0x1000 micropython.bin
```

Substitua `SERIAL_PORT` pela porta que você identificou e `micropython.bin` pelo caminho do arquivo de firmware que você baixou.

Agora você deve ter o MicroPython instalado no seu ESP32!

---

Por favor, substitua `SERIAL_PORT` e `micropython.bin` pelos valores corretos para o seu sistema e firmware.
