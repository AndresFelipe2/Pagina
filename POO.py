class vehiculo:
  def __init__(self, ruedas, asientos, espejos):
      self.ruedas = ruedas 
      self.asientos = asientos
      self.espejos = espejos

class carro(vehiculo):
  def __init__(self, ruedas, asientos, espejos, marca, modelo, motor):
      super().__init__(ruedas, asientos, espejos)
      self.marca = marca
      self.modelo = modelo
      self.motor = motor

carro1 = carro(4, 4, 2, 'Honda', 'Type R', 'v10')
print(carro1.marca)
  
