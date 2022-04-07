import re

cadena="vamos a aprender expresiones regulares"

textoBuscar="vamos"

#forma 1 para buscar palabras
'''if re.search(textoBuscar, cadena) is not None:

	print("he encontrado el texto")

else:

	print("no he encontrado el texto")'''

#forma 2 para encontrar en que parte de la cadena de texto se encuentra
textoEncontrado=re.search(textoBuscar, cadena)

print(textoEncontrado.start())

print(textoEncontrado.end())

print(textoEncontrado.span())


#otro ejercicio, para saber cuantas veces esta el texto a buscar
cadena2="vamos a aprender expresiones regulares python. python es un lenguaje e sintaxis sencilla"

textoBuscar="python"

print(re.findall(textoBuscar, cadena2))

print(len(re.findall(textoBuscar, cadena2)))

