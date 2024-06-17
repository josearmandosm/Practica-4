#Ejercicio 4: Filtrar palabras que empiezan con 'p'
# Dada una lista de palabras, filtra aquellas que comienzan con la letra 'p'.


palabras = ["hola", "mundo", "python", "programacion"]
palabras_filtradas = [palabra for palabra in palabras if palabra.startswith('p')]

print(palabras_filtradas)
