#Ejercicio 6: Filtrar palabras con longitud mayor a 4
# Dada una lista de palabras, filtra aquellas que tienen una longitud mayor a 4.

palabras = ["hola", "mundo", "python", "hi"]
palabras_filtradas = [palabra for palabra in palabras if len(palabra) > 4]
print(palabras_filtradas)
