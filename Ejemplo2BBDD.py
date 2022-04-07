import sqlite3

miConexion=sqlite3.connect("Gestion de productos")

miCursor=miConexion.cursor()

miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos=[

	("AR.01", "pelota", 20, "jugueteria"),
	("AR.02", "pantalon", 15, "confeccion"),
	("AR.03", "destornillador", 25, "ferreteria"),
	("AR.04", "jarron", 45, "ceramica"),

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

#en caso de querer agregar un elemento adicional, recodar elimnar los registros anteriores
#cuando hay comillas dobles las internas deben ser simples se sacan con alt + 39 
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 15, 'jugueteria')")


miConexion.commit()

miConexion.close()