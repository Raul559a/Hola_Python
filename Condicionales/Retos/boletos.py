```Escribe un programa que calcule el precio en la entrada de un cine dependiendo de la edad:
      El precio normal de la entrada es de 10 Euros.
      Si el cliente tiene una edad de 60 o más años, solo pagará 2 Euros.
      Si el cliente tiene una edad de 12 o menos años, solo pagará 4 Euros.```
price = int(input('ingrese su edad'))
if price >= 60:
    print('pagar 2 euros')
elif price <= 12:
    print('pagar 4 euros')  
else:
    print('no cumples con los requisitos')
