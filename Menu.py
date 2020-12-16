import os
import sqlite3

def modificar():
    codigo = int (input("ingrese codigo del producto: "))
    nombre = input("ingrese nuevo nombre del producto: ")
    precio = int (input("ingrese nuevo precio del producto: "))
    
    #Si la base de datos existe se conecta, de lo contrario se CREA la base de datos por defecto
    conexion=sqlite3.connect("ventas.db")
    
    #Para eliminar elementos de la Tablas en la BD Academico.db
    cursor=conexion.cursor()
    consulta = (f"""UPDATE PRODUCTO
                    SET 
                    NOMBRE ='{nombre}'
                    PRECIO = {precio}
                    WHERE
                    CODIGO = {codigo}""")
    
    cursor.execute(consulta)
    conexion.commit()
    
    #Cerrar conexion
    conexion.close()
    print("Producto modificado...\n")
    
def eliminar():
    codigo = int (input("ingrese codigo del producto: "))
    
    #Si la base de datos existe se conecta, de lo contrario se CREA la base de datos por defecto
    conexion=sqlite3.connect("ventas.db")
    
    #Para eliminar elementos de la Tablas en la BD Academico.db
    cursor=conexion.cursor()
    consulta = (f"""DELETE FROM 
                      PRODUCTO
                      WHERE
                      CODIGO = {codigo}""")
    
    cursor.execute(consulta)
    conexion.commit()
    
    #Cerrar conexion
    conexion.close()
    print("Producto eliminado...\n")
    
def agregar():
    conexion=sqlite3.connect("ventas.db")

    #Para crear Tablas en la BD Academico.db
    cursor=conexion.cursor()
    prod = input("ingrese nombre de producto: ")
    codigo = input("ingrese código de producto: ")
    precio = input("ingrese precio de producto: ")
    cursor.execute(f"""INSERT INTO PRODUCTO VALUES(
                        '{prod}',
                        '{codigo}',
                        {precio}
                        )""")
    
    conexion.commit()
    
    #Cerrar conexion
    conexion.close()
    print("Contenido agregado...\n")    
    
def listar():
    
    conexion=sqlite3.connect("ventas.db")
    
    #Para crear Tablas en la BD Academico.db
    cursor=conexion.cursor()
    
    print("NOMBRE\t"+"PRECIO\t"+"CODIGO")
    cursor.execute("""select NOMBRE,PRECIO,CODIGO
                   from PRODUCTO
                   order by IDPRODUCTO""")
    
    #Todo el resultado del select esta en personas
    #en java lo conocemos como resultset
    
    productos=cursor.fetchall()
    
    for producto in productos:
        print(producto[0],producto[1],producto[2])
    
    #Cerrar conexion
    conexion.close()


def error():
    print ("")
    input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        
def menu():
	
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print ("Selecciona una opción")
    print ("\t1-Listar")
    print ("\t2-Agregar")
    print ("\t3-Eliminar")
    print ("\t4-Modificar")
    print ("\t5-salir")
 
 
while True:
    # Mostramos el menu
    menu() 
    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ") 
    if opcionMenu=="1":
        listar()
        
    elif opcionMenu=="2":
        agregar()
        listar()
        
    elif opcionMenu=="3":
        eliminar()
        listar()
        
    elif opcionMenu=="4":
        listar()
        listar()
    	
    elif opcionMenu=="5":
    	break
    
    else:
        error()