#Ejercicio 8: Filtrar temperaturas mayores a 50 grados Fahrenheit
# Dada una lista de temperaturas en Fahrenheit, filtra aquellas que son mayores a 50 grados.

fahrenheit = [32.0, 68.0, 98.6, 212.0]
temperaturas_filtradas = [temp for temp in fahrenheit if temp > 50]
print(temperaturas_filtradas)
