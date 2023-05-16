# MicroBotPy

MicroBotPy ( Uma combinação de "MicroPython" e "Robô") é uma extensão do projeto LARA. Este framework foi desenvolvido com o objetivo de oferecer um alto nível de abstração para que os iniciantes em programação de computadores não se sintam intimidados por sintaxes que pareçam extremamente complexas.

Especificamente projetado para trabalhar com microcontroladores ESP32 e o framework MicroPython, o MicroBotPy torna mais fácil para os usuários iniciarem e progredirem no mundo da robótica e automação. Ao simplificar a interação com os sensores e fornecer um conjunto abrangente de funcionalidades, este framework permite que os usuários se concentrem na lógica e funcionalidade do seu projeto, em vez de lidarem com os detalhes técnicos dos dispositivos de hardware.

Com MicroBotPy, a programação de robôs e dispositivos automatizados se torna mais acessível, abrindo as portas para mais pessoas explorarem este campo fascinante. Este framework se empenha em tornar a robótica uma atividade divertida e gratificante para todos, independentemente do seu nível de habilidade em programação.

Em resumo, se você está começando sua jornada na programação de microcontroladores e robótica, ou se você é um entusiasta procurando uma maneira mais simplificada de programar seus projetos, o MicroBotPy é uma excelente ferramenta para ajudá-lo a alcançar seus objetivos.
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

Baixe o firmware do MicroPython para ESP32. Você pode encontrar o firmware mais recente na [página de download do MicroPython](https://micropython.org/download/?mcu=esp32). Escolha o apropriado para o seu módulo ESP32.

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



---

# Programando ESP32 com MicroPython Usando Thonny IDE

## Pré-requisitos:

1. MicroPython instalado no ESP32. Se ainda não o fez, consulte as [instruções de instalação do MicroPython no ESP32](link_para_instruções).
2. Thonny IDE instalado no seu computador. Se ainda não o fez, você pode baixá-lo do [site oficial do Thonny](https://thonny.org).

## Instruções:

### 1. Conecte o ESP32 ao seu computador

Use um cabo USB para conectar o ESP32 ao seu computador.

### 2. Abra o Thonny IDE

Inicie o Thonny IDE no seu computador.

### 3. Configure o Thonny para usar o MicroPython no ESP32

No menu do Thonny, vá para `Run > Select Interpreter`. Na janela que aparece, escolha "MicroPython (ESP32)". Em seguida, na lista suspensa `Port`, selecione a porta que o ESP32 está usando.

### 4. Crie ou abra um script Python

Agora você pode escrever os seus codigos.




---


---

# Usando as Classes do Robô

Este documento descreve como usar a classe `Pacotes` em seu robô. `Pacotes` é uma classe de fachada que encapsula o uso de várias outras classes, simplificando a interação do usuário com o sistema.

## Pré-requisitos

Antes de começar, certifique-se de que você importou a classe `Pacotes` em seu código:

```python
import sys
sys.path.insert(1,'/classes')
import Pacotes
```

## Inicialização

Para criar uma instância da classe `Pacotes`, use o seguinte comando:

```python
meus_pacotes = Pacotes.Pacotes()
```

## Usando a Classe Motor através dos Pacotes

A classe `Motor` é usada para controlar os movimentos de dois motores do robô. Ela pode ser acessada através da classe `Pacotes`.

### Inicialização

Para criar uma instância da classe `Motor`, use o seguinte comando:

```python
meu_motor = Pacotes.Motor()
```

### Movendo os Motores

Para mover os motores para frente, use:

```python
meu_motor.frenteMotor1(velocidade)
meu_motor.frenteMotor2(velocidade)
```

Para mover os motores para trás, use:

```python
meu_motor.trazMotor1(velocidade)
meu_motor.trazMotor2(velocidade)
```

Em todos os casos, substitua `velocidade` pela velocidade desejada.

### Parando os Motores

Para parar todos os motores, use:

```python
meu_motor.pararMotores()
```

Para parar um motor específico, use:

```python
meu_motor.pararMotor1()
meu_motor.pararMotor2()
```

## Executando a Rotina do Robô

Para executar a rotina do robô, chame a função `rotina` e passe o tempo de execução desejado (em minutos) como argumento:

```python
Pacotes.rotina(2)  # Executa a rotina por 2 minutos
```

Durante a rotina, o LED no pino 2 piscará. Quando a rotina terminar, "programa finalizado." será impresso na saída.

---

# Usando as Classes de Sensores do Robô

Este documento descreve como usar as classes `Infra`, `InfraDig` e `SensorCor` em seu robô.

## Classe Infra

A classe `Infra` gerencia o sensor de infravermelho do robô.

### Inicialização

Para criar uma instância da classe `Infra`, use o seguinte comando:

```python
meu_infra = Infra()
```

### Calculando a Distância

Para calcular a distância obtida pelo sensor, use:

```python
distancia = meu_infra.calculaDistancia()
```

O método `calculaDistancia()` retorna a distância calculada.

## Classe InfraDig

A classe `InfraDig` gerencia o sensor de infravermelho digital do robô.

### Inicialização

Para criar uma instância da classe `InfraDig`, use o seguinte comando:

```python
meu_infra_dig = InfraDig()
```

### Verificando a Existência de um Objeto

Para verificar se há um objeto a menos de 30 cm, use:

```python
objeto = meu_infra_dig.haObjeto()
```

O método `haObjeto()` retorna `True` se houver um objeto a menos de 30 cm e `False` caso contrário.

## Classe SensorCor

A classe `SensorCor` gerencia os sensores de cor do robô.

### Inicialização

Para criar uma instância da classe `SensorCor`, use o seguinte comando:

```python
meu_sensor_cor = SensorCor(s0, s1, s2, s3, out)
```

Substitua `s0`, `s1`, `s2`, `s3` e `out` pelos números de portas correspondentes.

### Medindo o Pulso

Para medir o tempo em que uma porta ficou ligada, use:

```python
cont = meu_sensor_cor.medePulso(porta, tempo)
```

Substitua `porta` pela porta desejada e `tempo` pelo tempo desejado. O método `medePulso()` retorna o valor do contador.

### Retornando a Cor

Para retornar a cor vermelha, use:

```python
vermelho = meu_sensor_cor.RetornaCorVermelha()
```

Para retornar a cor azul, use:

```python
azul = meu_sensor_cor.RetornaCorAzul()
```

Para retornar a cor branca, use:

```python
branco = meu_sensor_cor.RetornaCorBranco()
```

Para retornar a cor verde, use:

```python
verde = meu_sensor_cor.RetornaCorVerde()
```

Cada um dos métodos acima retorna o valor correspondente à cor.

---


# Usando a Classe Pacote

A classe `Pacote` serve como um agregador ou "fachada" para as outras classes, como `Infra`, `InfraDig` e `SensorCor`. Ela facilita o uso dessas classes, permitindo que você crie uma única instância de `Pacote` que inicializa todas as outras classes automaticamente.

## Inicialização

Para criar uma instância da classe `Pacote`, você pode usar o seguinte comando:

```python
meu_pacote = Pacote()
```

Este comando cria uma nova instância da classe `Pacote` e, internamente, também inicializa instâncias das classes `Infra`, `InfraDig` e `SensorCor`.

Depois de criar uma instância de `Pacote`, você pode acessar as instâncias das outras classes através dessa instância de `Pacote`. Aqui está como você pode fazer isso:

```python
distancia = meu_pacote.infra.calculaDistancia()
objeto = meu_pacote.infra_dig.haObjeto()
vermelho = meu_pacote.sensor_cor.RetornaCorVermelha()
```


Observe que `infra`, `infra_dig` e `sensor_cor` são os atributos da classe `Pacote` que contêm as instâncias das classes `Infra`, `InfraDig` e `SensorCor`, respectivamente. 


## SensorLuz

A classe SensorLuz gerencia os sensores de luz do robô. Os métodos incluem:

- `RetornaValorLuzSensor1()`: Retorna a intensidade da luz lida pelo sensor 1.
- `RetornaValorLuzSensor2()`: Retorna a intensidade da luz lida pelo sensor 2.
- `RetornaValorLuzSensor3()`: Retorna a intensidade da luz lida pelo sensor 3.
- `ligarSensor1()`: Habilita o sensor 1.
- `desligarSensor1()`: Desabilita o sensor 1.
- `ligarSensor2()`: Habilita o sensor 2.
- `desligarSensor2()`: Desabilita o sensor 2.
- `ligarSensor3()`: Habilita o sensor 3.
- `desligarSensor3()`: Desabilita o sensor 3.

Exemplo de uso:

```python
from Pacotes import SensorLuz

luz = SensorLuz()
luz.ligarSensor1()
print(luz.RetornaValorLuzSensor1())
luz.desligarSensor1()
```

## Ultra

A classe Ultra gerencia o sensor ultrassônico do robô. Os métodos incluem:

- `iniciaSensor()`: Inicia o sensor ultrassônico.
- `calculaDistaciaUltra()`: Calcula a distância obtida pelo sensor.

Exemplo de uso:

```python
from Pacotes import Ultra

ultra = Ultra(tr=trigger_pin, echo=echo_pin)
ultra.iniciaSensor()
print(ultra.calculaDistaciaUltra())
```

Essas classes podem ser importadas e usadas diretamente, ou através da classe Pacotes. O uso da classe Pacotes é recomendado para simplificar e agrupar as operações do robô. A classe Pacotes permite a fácil inicialização e gerenciamento de todos os sensores e funções relacionadas, fornecendo um ponto de acesso unificado.





