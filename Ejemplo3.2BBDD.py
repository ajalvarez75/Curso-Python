import sqlite3

miConexion=sqlite3.connect("Gestion de productos 2.3")

miCursor=miConexion.cursor()

#para que los codigos se generen autoamticamente AUTOINCREMENT
#UNIQUE para que no se repita la informacion
miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos=[
#Al tener dos productos con el mismo nombre saltaria error debido a que hemos usado el comando unique anteriormente
	("pelota", 20, "jugueteria"),
	("pantalon", 15, "confeccion"),
	("destornillador", 25, "ferreteria"),
	("jarron", 45, "ceramica"),
	("pantalon", 35, "confeccion")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

#en caso de querer agregar un elemento adicional, recodar elimnar los registros anteriores
#cuando hay comillas dobles las internas deben ser simples se sacan con alt + 39 
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 15, 'jugueteria')")


miConexion.commit()

miConexion.close()