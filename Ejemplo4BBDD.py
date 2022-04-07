import sqlite3

miConexion=sqlite3.connect("Gestion de productos 2.2")

miCursor=miConexion.cursor()


#Tener cuidado cuando se realiza BBDD ya que los datos son case sensitive(diferencia mayus y minus).
#busca en mi base de datos un articulo en particular
#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confeccion'")
#productos=miCursor.fetchall()
#print(productos)

#para actualizar el precio de un articulo
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

#para eliminar
#miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

miConexion.commit()

miConexion.close()