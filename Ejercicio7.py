#Ejercicio 7: Convertir una lista de temperaturas de Celsius a Fahrenheit
# Dada una lista de temperaturas en Celsius, conviértelas a Fahrenheit.

celsius = [0, 20, 37, 100]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)