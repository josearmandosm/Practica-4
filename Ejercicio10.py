#Ejercicio 10: Filtrar palabras que contienen la letra 'a'
# Dada una lista de palabras, filtra aquellas que contienen la letra 'a'.

palabras = ["hola", "mundo", "python", "vida"]
palabras_filtradas = [palabra for palabra in palabras if 'a' in palabra]
print(palabras_filtradas)
