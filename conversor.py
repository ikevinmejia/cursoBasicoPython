#COP vs USD
pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")

#USD vs COP

usd = int(input("USD a cambiar: "))
cop = 3800
usd = cop * usd
usd = round(usd, 2)
usd = str(usd)
print("El valor de USD en COP es: $" + usd)
