import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()


#Despues de ser ejecuta esta linea debe desabilitarse de lo contraria el programa crearia una nueva tabla.
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#siguiente linea comentada para no afectar ejercicio siguiente. ver curso de youtube.
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

variosProductos=[

	("Camiseta", 10, "Deportes"),
	("Jarron", 90, "Ceramica"),
	("Camion", 20, "Jugueteria")

]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)

#para extraer los productos de la base de datos
miursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:

	print("Nombre articulo: ", producto[0], "Seccion: ", producto[2])


miConexion.commit()

miConexion.close()

