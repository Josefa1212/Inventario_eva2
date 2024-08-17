#Conexión a la Base de Datos                    #inventario.db. donde va

import sqlite3
import csv
def conectar_bd(nombre_bd):
 return sqlite3.connect(nombre_bd)

#Crear tablas

def crear_tablas(con):
 cursor = con.cursor()
 cursor.execute('''
 CREATE TABLE IF NOT EXISTS clientes (
 id INTEGER PRIMARY KEY,
 nombre TEXT NOT NULL,
 email TEXT NOT NULL
 )
 ''')
 cursor.execute('''
 CREATE TABLE IF NOT EXISTS ventas (
 id INTEGER PRIMARY KEY,
 cliente_id INTEGER,
 fecha TEXT NOT NULL,
 total REAL NOT NULL,
 FOREIGN KEY(cliente_id) REFERENCES clientes(id)
 )
 ''')
 con.commit()

 #Gestión de inventario

def insertar_producto(con, nombre, stock, precio):
  cursor = con.cursor()
  cursor.execute((nombre, stock, precio))
  con.commit()

def registrar_movimiento(con, producto_id, tipo, cantidad,
fecha):
  cursor = con.cursor()
  cursor.execute((producto_id, tipo, cantidad,
fecha))
  con.commit()


def consultar_movimientos(con, producto_id):
 cursor = con.cursor()
 cursor.execute((producto_id))
 con.commit()


def exportar_movimientos_a_csv(datos, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
         escritor_csv = csv.writer(archivo_csv)
         escritor_csv.writerow(['Nombre Cliente', 'Fecha', 'Total'])
         escritor_csv.writerows(datos)



# Ejecución del ejemplo
con = conectar_bd('empresa.db')
crear_tablas(con)
insertar_producto(con, 'escoba','2', 5000)
insertar_producto(con, 'Cepillo','20', 2000)
registrar_movimiento(con, 'escoba','aseo', 1, )
registrar_movimiento(con,'Cepillo','Belleza', 2, )
ventas = consultar_movimientos(con)
exportar_movimientos_a_csv(ventas, 'reporte_ventas.csv')
con.close()
