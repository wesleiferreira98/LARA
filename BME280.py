from machine import I2C
import time

# Endereco padrao BME280.
BME280_I2CADDR = 0x76

# Modos de operacao
BME280_OSAMPLE_1 = 1
BME280_OSAMPLE_2 = 2
BME280_OSAMPLE_4 = 3
BME280_OSAMPLE_8 = 4
BME280_OSAMPLE_16 = 5

# Registros BME280

BME280_REGISTER_DIG_T1 = 0x88  # Aparando registros de parametros
BME280_REGISTER_DIG_T2 = 0x8A
BME280_REGISTER_DIG_T3 = 0x8C

BME280_REGISTER_DIG_P1 = 0x8E
BME280_REGISTER_DIG_P2 = 0x90
BME280_REGISTER_DIG_P3 = 0x92
BME280_REGISTER_DIG_P4 = 0x94
BME280_REGISTER_DIG_P5 = 0x96
BME280_REGISTER_DIG_P6 = 0x98
BME280_REGISTER_DIG_P7 = 0x9A
BME280_REGISTER_DIG_P8 = 0x9C
BME280_REGISTER_DIG_P9 = 0x9E

BME280_REGISTER_DIG_H1 = 0xA1
BME280_REGISTER_DIG_H2 = 0xE1
BME280_REGISTER_DIG_H3 = 0xE3
BME280_REGISTER_DIG_H4 = 0xE4
BME280_REGISTER_DIG_H5 = 0xE5
BME280_REGISTER_DIG_H6 = 0xE6
BME280_REGISTER_DIG_H7 = 0xE7

BME280_REGISTER_CHIPID = 0xD0
BME280_REGISTER_VERSION = 0xD1
BME280_REGISTER_SOFTRESET = 0xE0

BME280_REGISTER_CONTROL_HUM = 0xF2
BME280_REGISTER_CONTROL = 0xF4
BME280_REGISTER_CONFIG = 0xF5
BME280_REGISTER_PRESSURE_DATA = 0xF7
BME280_REGISTER_TEMP_DATA = 0xFA
BME280_REGISTER_HUMIDITY_DATA = 0xFD


class Device:
  """Classe para comunicacao com um dispositivo I2C.

   Permite ler e escrever valores de matriz de 8 bits, 16 bits e bytes para
   registradores no dispositivo."""

  def __init__(self, address, i2c):
    """Crie uma instancia do dispositivo I2C no endereco especificado usando
     o objeto de interface I2C especificado."""
    self._address = address
    self._i2c = i2c

  def escrevaRaw8(self, value):
    """Escreva um valor de 8 bits no barramento (sem registrador)."""
    value = value & 0xFF
    self._i2c.writeto(self._address, value)

  def escreva8(self, register, value):
    """Escreva um valor de 8 bits no registrador especificado"""
    b=bytearray(1)
    b[0]=value & 0xFF
    self._i2c.writeto_mem(self._address, register, b)

  def escreva16(self, register, value):
    """Escreva um valor de 16 bits no registrador especificado"""
    value = value & 0xFFFF
    b=bytearray(2)
    b[0]= value & 0xFF
    b[1]= (value>>8) & 0xFF
    self.i2c.writeto_mem(self._address, register, value)

  def lerRaw8(self):
    """Le um valor de 8 bits no barramento (sem registrador)."""
    return int.from_bytes(self._i2c.readfrom(self._address, 1),'little') & 0xFF

  def lerU8(self, register):
    """Le um byte nao assinado do registrador especificado."""
    return int.from_bytes(
        self._i2c.readfrom_mem(self._address, register, 1),'little') & 0xFF

  def lerS8(self, register):
    """Le um byte assinado do registrador especificado."""
    result = self.lerU8(register)
    if result > 127:
      result -= 256
    return result

  def lerU16(self, register, little_endian=True):
    """Leia um valor de 16 bits sem sinal do registrador especificado, com o
     endianness especificado (padrão little endian, ou byte menos significativo
     primeiro)."""
    result = int.from_bytes(
        self._i2c.readfrom_mem(self._address, register, 2),'little') & 0xFFFF
    if not little_endian:
      result = ((result << 8) & 0xFF00) + (result >> 8)
    return result

  def lerS16(self, register, little_endian=True):
    """Leia um valor de 16 bits com sinal do registrador especificado, com o
     endianness especificado (padrão little endian, ou byte menos significativo
     primeiro)."""
    result = self.lerU16(register, little_endian)
    if result > 32767:
      result -= 65536
    return result

  def lerU16LE(self, register):
    """Leia um valor de 16 bits sem sinal do registrador especificado, em pouco
     ordem de bytes endian."""
    return self.lerU16(register, little_endian=True)

  def lerU16BE(self, register):
    """Leia um valor de 16 bits sem sinal do registrador especificado, em grande
     ordem de bytes endian."""
    return self.lerU16(register, little_endian=False)

  def lerS16LE(self, register):
    """Leia um valor de 16 bits com sinal do registrador especificado, em pouco
     ordem de bytes endian."""
    return self.lerS16(register, little_endian=True)

  def lerS16BE(self, register):
    """Leia um valor de 16 bits assinado do registrador especificado, em grande
     ordem de bytes endian."""
    return self.lerS16(register, little_endian=False)


class BME280:
  def __init__(self, mode=BME280_OSAMPLE_1, address=BME280_I2CADDR, i2c=None,
               **kwargs):
    # Verifique se o modo e valido.
    if mode not in [BME280_OSAMPLE_1, BME280_OSAMPLE_2, BME280_OSAMPLE_4,
                    BME280_OSAMPLE_8, BME280_OSAMPLE_16]:
        raise ValueError(
            'Valor de modo inesperado {0}. Defina o modo para um dos '
            'BME280_ULTRALOWPOWER, BME280_STANDARD, BME280_HIGHRES, or '
            'BME280_ULTRAHIGHRES'.format(mode))
    self._mode = mode
    # Crie um dispositivo I2C.
    if i2c is None:
      raise ValueError('Um objeto I2C e necessário')
    self._device = Device(address, i2c)
    # Carregar valores de calibracao.
    self._calibracao_de_carga() # _calibracao_de_carga
    self._device.escreva8(BME280_REGISTER_CONTROL, 0x3F)
    self.t_fine = 0

  def _calibracao_de_carga(self):

    self.dig_T1 = self._device.lerU16LE(BME280_REGISTER_DIG_T1)
    self.dig_T2 = self._device.lerS16LE(BME280_REGISTER_DIG_T2)
    self.dig_T3 = self._device.lerS16LE(BME280_REGISTER_DIG_T3)

    self.dig_P1 = self._device.lerU16LE(BME280_REGISTER_DIG_P1)
    self.dig_P2 = self._device.lerS16LE(BME280_REGISTER_DIG_P2)
    self.dig_P3 = self._device.lerS16LE(BME280_REGISTER_DIG_P3)
    self.dig_P4 = self._device.lerS16LE(BME280_REGISTER_DIG_P4)
    self.dig_P5 = self._device.lerS16LE(BME280_REGISTER_DIG_P5)
    self.dig_P6 = self._device.lerS16LE(BME280_REGISTER_DIG_P6)
    self.dig_P7 = self._device.lerS16LE(BME280_REGISTER_DIG_P7)
    self.dig_P8 = self._device.lerS16LE(BME280_REGISTER_DIG_P8)
    self.dig_P9 = self._device.lerS16LE(BME280_REGISTER_DIG_P9)

    self.dig_H1 = self._device.lerU8(BME280_REGISTER_DIG_H1)
    self.dig_H2 = self._device.lerS16LE(BME280_REGISTER_DIG_H2)
    self.dig_H3 = self._device.lerU8(BME280_REGISTER_DIG_H3)
    self.dig_H6 = self._device.lerS8(BME280_REGISTER_DIG_H7)

    h4 = self._device.lerS8(BME280_REGISTER_DIG_H4)
    h4 = (h4 << 24) >> 20
    self.dig_H4 = h4 | (self._device.lerU8(BME280_REGISTER_DIG_H5) & 0x0F)

    h5 = self._device.lerS8(BME280_REGISTER_DIG_H6)
    h5 = (h5 << 24) >> 20
    self.dig_H5 = h5 | (
        self._device.lerU8(BME280_REGISTER_DIG_H5) >> 4 & 0x0F)

  def leia_temperatura_bruta(self): #leia_temperatura_bruta
    """Le a temperatura bruta (não compensada) do sensor."""
    meas = self._mode
    self._device.escreva8(BME280_REGISTER_CONTROL_HUM, meas)
    meas = self._mode << 5 | self._mode << 2 | 1
    self._device.escreva8(BME280_REGISTER_CONTROL, meas)
    sleep_time = 1250 + 2300 * (1 << self._mode)

    sleep_time = sleep_time + 2300 * (1 << self._mode) + 575
    sleep_time = sleep_time + 2300 * (1 << self._mode) + 575
    time.sleep_us(sleep_time)  # Aguarde o tempo necessario
    msb = self._device.lerU8(BME280_REGISTER_TEMP_DATA)
    lsb = self._device.lerU8(BME280_REGISTER_TEMP_DATA + 1)
    xlsb = self._device.lerU8(BME280_REGISTER_TEMP_DATA + 2)
    raw = ((msb << 16) | (lsb << 8) | xlsb) >> 4
    return raw

  def leia_pressao_bruta(self): #leia_pressao_bruta
    """Le o nível de pressão bruto (não compensado) do sensor."""
    """Assume que a temperatura ja foi lida """
    """ou seja, que atraso suficiente foi fornecido"""
    msb = self._device.lerU8(BME280_REGISTER_PRESSURE_DATA)
    lsb = self._device.lerU8(BME280_REGISTER_PRESSURE_DATA + 1)
    xlsb = self._device.lerU8(BME280_REGISTER_PRESSURE_DATA + 2)
    raw = ((msb << 16) | (lsb << 8) | xlsb) >> 4
    return raw

  def leia_humidade_bruta(self):
    """Assume que a temperatura ja foi lida """
    """ou seja, que atraso suficiente foi fornecido"""
    msb = self._device.lerU8(BME280_REGISTER_HUMIDITY_DATA)
    lsb = self._device.lerU8(BME280_REGISTER_HUMIDITY_DATA + 1)
    raw = (msb << 8) | lsb
    return raw

  def leia_temperatura(self):
    """Obtenha a temperatura compensada em 0,01 de grau Celsius."""
    adc = self.leia_temperatura_bruta()
    var1 = ((adc >> 3) - (self.dig_T1 << 1)) * (self.dig_T2 >> 11)
    var2 = ((
        (((adc >> 4) - self.dig_T1) * ((adc >> 4) - self.dig_T1)) >> 12) *
        self.dig_T3) >> 14
    self.t_fine = var1 + var2
    return (self.t_fine * 5 + 128) >> 8

  def leia_pressao(self):
    """Obtem a pressão compensada em Pascals."""
    adc = self.leia_pressao_bruta()
    var1 = self.t_fine - 128000
    var2 = var1 * var1 * self.dig_P6
    var2 = var2 + ((var1 * self.dig_P5) << 17)
    var2 = var2 + (self.dig_P4 << 35)
    var1 = (((var1 * var1 * self.dig_P3) >> 8) +
            ((var1 * self.dig_P2) >> 12))
    var1 = (((1 << 47) + var1) * self.dig_P1) >> 33
    if var1 == 0:
      return 0
    p = 1048576 - adc
    p = (((p << 31) - var2) * 3125) // var1
    var1 = (self.dig_P9 * (p >> 13) * (p >> 13)) >> 25
    var2 = (self.dig_P8 * p) >> 19
    return ((p + var1 + var2) >> 8) + (self.dig_P7 << 4)

  def leia_humidade(self):
    adc = self.leia_humidade_bruta()
    # print 'Umidade bruta = {0:d}'.format (adc)
    h = self.t_fine - 76800
    h = (((((adc << 14) - (self.dig_H4 << 20) - (self.dig_H5 * h)) +
         16384) >> 15) * (((((((h * self.dig_H6) >> 10) * (((h *
                          self.dig_H3) >> 11) + 32768)) >> 10) + 2097152) *
                          self.dig_H2 + 8192) >> 14))
    h = h - (((((h >> 15) * (h >> 15)) >> 7) * self.dig_H1) >> 4)
    h = 0 if h < 0 else h
    h = 419430400 if h > 419430400 else h
    return h >> 12

  @property
  def temperatura(self):
    "Return the temperature in degrees."
    t = self.leia_temperatura()
    ti = t // 100
    td = t - ti * 100
    return "{}.{:02d}C".format(ti, td)

  @property
  def pressao(self):
    "Return the temperature in hPa."
    p = self.leia_pressao() // 256
    pi = p // 100
    pd = p - pi * 100
    return "{}.{:02d}hPa".format(pi, pd)

  @property
  def humidade(self):
    "Return the humidity in percent."
    h = self.leia_humidade()
    hi = h // 1024
    hd = h * 100 // 1024 - hi * 100
    return "{}.{:02d}%".format(hi, hd)
