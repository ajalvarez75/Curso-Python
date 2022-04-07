#para generar archivo binario
import pickle

lista_nombres=["pedro", "ana", "maria", "isabel"]

fichero_binario=open("lista_nombres", "wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

#para convertir-leer archivos binarios
import pickle

fichero=open("lista_nombres", "rb")

lista=pickle.load(fichero)

print(lista)

