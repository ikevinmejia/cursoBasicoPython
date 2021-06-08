#COP vs USD
menu = """
Bienvenido al conversor de monedas. 💰

1 - Pesos colombianos.
2 - Pesos argentinos.
3 - Pesos mexicanos.

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    pesos = float(input("¿Cuántos pesos argentinos tienes?: "))
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 3:
    pesos = float(input("¿Cuántos pesos mexicanos tienes?: "))
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else:
    print("Escoge una opción correcta, por favor.")
    
#USD vs COP

""" usd = int(input("USD a cambiar: "))
cop = 3800
usd = cop * usd
usd = round(usd, 2)
usd = str(usd)
print("El valor de USD en COP es: $" + usd) """

#Ejercicios simples: 
""" n = int(input("Escribe un número entero positivo: "))
suma = (n*(n + 1))/(2)
print("La suma de los primeros enteros de 1 hasta " + str(n) + " es: " + str(suma)) """

#Ejercicio de Indice de masa corporal
""" kg = float(input("¿Cuál es tu peso?: "))
m = float(input("¿Cuál es tu estatura?: "))
imc = (kg) / (m) **2
print("Tu indice de masa corporal es: " + str(round(imc, 2))) """

#Ejercicio panaderia
""" Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total. """
""" pan = 3.49
pan_pasado = pan * 0.6
cant_pan = float(input("¿Cúantos panes va a llevar?: "))
cant_pan = round(cant_pan, 2)
print("El valor del pan es: € " + str(pan) + ". El descuento por unidad son € " + str(pan_pasado) + " y el valor total a pagar con el descuento aplicado son: € " + str((cant_pan * pan ) * 0.6) ) """