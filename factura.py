print('Servicios publicos')
agua = input('Digite los centimetros cubicos de agua consumida: ')
energia = input('Digite los kilovatios de energia consumidos: ')
gas = input('Digite los centimetro cubicos de gas consumidos: ')

precio_agua = 2300
precio_energia = 1800
precio_gas = 2000

total_agua = agua * precio_agua
total_energia = energia * precio_energia
total_gas = gas * precio_gas

total_mensual = total_agua + total_energia + total_gas
print(f'gasto mensual en factura: {total_mensual}')
