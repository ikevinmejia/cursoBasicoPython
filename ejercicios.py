#Ejercicios funciones
"""
def titulo_subrayado (titulo, caracter = "*"):
    print(titulo)
    print(caracter*len(titulo))

titulo_subrayado("Sistema de Admin")
titulo_subrayado("Ventas", "-") """

""" def function(valor, iva = 21):
    return valor + valor * iva/100
print(function(30000, 10))
print(function(30000)) """

""" def carga_lista():
    li = []
    for i in range (5):
        valor = int(input("Ingrese valor: "))
        li.append(valor)
    return li
def imprimir_mayor10(li):
    print("Elementos de la lista mayores a 10")
    for i in range (len(li)):
        if li [i]>10:
            print(li[i])

lista=carga_lista()
imprimir_mayor10(lista) """


""" nombre = str(input("¿Cuál es tu nombre?: "))

def function():
    print("¡Hola " + nombre + "!")

function() """

#Bucles

""" word = str(input("Escribe una palabra: "))

for i in range(0, 10):
    print(word) """

""" birthday = int(input("¿Cuál es tu edad?: "))
ed = 0

for i in range(birthday):
    ed += 1
    print("Haz cumplido:", ed) """

""" number = int(input("Escribe un número: "))
for i in range(1,number, 2):
    print(i, end=", ") """

""" number = int(input("Escribe un número: "))
for i in range(number, -1, -1):
    print(i, end=", ") """

""" invest = float(input("¿Cuánto desea invertir?: "))
interest = float(input("¿A qué tasa de interes?: "))
years =  int(input("¿A cuántos años?: "))
count=0
for i in range(years):
    count += 1
    invest *= 1 + interest/100
    print("Su dinero acomulado anualmente es: " + str(round(invest,2))) """


""" number = int(input("Pon un número: "))

for i in range(number):
    for j in range(i + 1):
        print("*", end="")
    print("")

for i in range(number):
    print("*" * (i + 1)) """

""" for i in range (1, 11):
    for j in range (1, 11):
        print(i*j, end="\t")
    print("") """



#Ejercicios condicionales

""" cateto_a = float(input("Introduce el valor del cateto a: "))
cateto_b = float(input("Introduce el valor del cateto b: "))
import math
h = round(math.sqrt((cateto_a**2)+(cateto_b**2)), 2)

print(round(math.sqrt((cateto_a**2)+(cateto_b**2)), 2)) """

""" edad = int(input("¿Cuál es tu edad?: "))

if edad < 4:
    print("Puedes entrar gratis.")
elif edad >= 4 and edad <= 18:
    print("La entrada tiene un costo de 5€.")
else:
    print("La entrada tiene un costo de 10€") """

""" puntuacion = float(input("En la escala de puntuacón de la empresa: 0.0, 0.4 y 0.6 o más ¿Cuál es su puntuación?: "))
nivel = "Su nivel es "
text = "y el dinero a recibir es de: "
dinero = 2400 * puntuacion

if puntuacion == 0.0:
    print(nivel + "inaceptable " + text + str(dinero) + "€")
elif puntuacion == 0.4:
    print(nivel + "aceptable" + text + str(dinero) + "€")
elif puntuacion >= 0.6:
    print(nivel + "meritorio" + text + str(dinero) + "€")
else:
    print("Por favor verifica el valor solicitado") """

""" menu = "Nuestro menu es: "
ingredientes = "con mozzarella y tomate"
pizza = "La orden ha sido recibida, su pizza es de: "
error = "Elija una orden correcta, por favor"

text = str(input("Bienvenido a la pizzería Bella Napoli, ¿Desea ver la carta de pizzas vegetarianas?: "))

if text == "si":
    menu_vegi = str(input(menu + "pimiento y  tofu ¿Cuál desea?: "))
    if menu_vegi == "pimiento":
        print(pizza + "pimiento " + ingredientes)
    elif menu_vegi != "pimiento":
        print(pizza + "tofu " + ingredientes)
    else:
        print(error)
elif text == "no":
    no_vegi = str(input(menu + "Peperoni, Jamón y Salmón ¿Cuál desea?: "))
    if no_vegi == "peperoni":
        print(pizza + "peperoni " + ingredientes)
    elif no_vegi == "jamon":
        print(pizza + "jamón " + ingredientes)
    elif no_vegi == "salmon":
        print(pizza + "salmón " + ingredientes)
    else:
        print(error)
else:
    print(error) """

""" edad = int(input("¿Cuál es su edad?: "))
ingreso = float (input("¿Cuántos son sus ingresos mensuales?: "))

if edad > 16 and ingreso >= 1000:
    print("Este año debe tributar.")
elif edad < 16 or ingreso < 1000:
    print("Su edad o ingresos no lo hacen un ciudadano tributario")
else:
    print("Señor usuario, usted no debe tributar este año") """

""" num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un número: "))
resultado = num1 % num2
if resultado == 0:
    print("Ha ocurrido un error")
else:
    print("El resultado de la división es: " + str(resultado)) """

""" password = str(input("Introduce tu contraseña: "))
key = "kevin"
if password == key:
    print("Tu contraseña es correcta")
else:
    print("Contraseña equivocada") """

""" edad =int(input("Escribe tu edad: "))
if edad > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad") """

""" numero = int(input("Escribe un número: "))
if numero > 5:
    print("Es mayor a 5")
elif numero == 5:
    print("Es igual a 5")
else:
    print("Es menor a 5") """

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