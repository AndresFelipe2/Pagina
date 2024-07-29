print('Servicios públicos')

# Solicitar datos al usuario y convertirlos a enteros
agua = int(input('Digite los centímetros cúbicos de agua consumida: '))
energia = int(input('Digite los kilovatios de energía consumidos: '))
gas = int(input('Digite los centímetros cúbicos de gas consumidos: '))

# Precios por unidad
precio_agua = 2300
precio_energia = 1800
precio_gas = 2000

# Calcular el costo total de cada servicio
total_agua = agua * precio_agua
total_energia = energia * precio_energia
total_gas = gas * precio_gas

# Calcular el gasto total mensual
total_mensual = total_agua + total_energia + total_gas

# Mostrar el gasto total mensual
print(f'Gasto mensual en factura: {total_mensual}')

