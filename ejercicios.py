#Ejercicios funciones
nombre = str(input("¿Cuál es tu nombre?: "))

def function():
    print("¡Hola " + nombre + "!")

function()

#Ejercicios condicionales

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