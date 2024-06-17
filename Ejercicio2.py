#Ejercicio 2: Filtrar números mayores a 10
# Dada una lista de números, filtra los números que son mayores a 10.

numeros = [5, 10, 15, 20, 25]
numeros_filtrados = [x for x in numeros if x > 10]
print(numeros_filtrados)