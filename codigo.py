print('Encuesta de empleo')

nombre = input('Digite su nombre: ')
edad = input('Digite su edad: ')
id = input('Digite su identificacion: ')
requisito_minimo = 18

print(f'nombre: {nombre}, edad: {edad}, identificacion: {identificacion}')

if edad == requisito_minimo:
  print('Cumple con el requisito de edad')

elif edad < requisito_minimo:
  print('No cumple con el requisito de edad')

else:
  print('Datos no validos')
