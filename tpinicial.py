from tkinter import *
from tkinter import ttk
import sqlite3


main = Tk()
main.title("System UTNBA")
main.configure(bg='#F0F7DA')
titulo = Label(main, text="System UTNBA", width=80, foreground='#F0F7DA', bg='#1F192F', font='Arial 15 bold').grid(pady=10, row=0, columnspan=5)
fuentetit = 'Arial 11'
fuentecue = 'Arial 10'

# # CONEXION BASE DE DATOS
# def crear_base():
#     global db
#     db = sqlite3.connect("baseTPinicial.db")


# def crear_tabla():
#     global cursor
#     cursor = db.cursor()
#     sql = "CREATE TABLE IF NOT EXISTS personas(id PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50) NOT NULL, apellido VARCHAR(50) NOT NULL, documento INT NOT NULL, correo VARCHAR(50) NOT NULL, filiacion VARCHAR(50)"
#     cursor.execute(sql)
#     db.commit()


# def regpersona(nombre, apellido, dni, correo, filiacion):
#     sql = "INSERT INTO personas (nombre, apellido, documento, correo) VALUES (%s, %s, %s, %s)"
#     datos = ("Mauro", "Di Filippo", 44544627, "maurodifi16@gmail.com" )
#     cursor.execute(sql, datos)
#     db.commit()


# def conspersona():
#     var_documento = 44544627
#     sql = "SELECT * FROM producto WHERE documento = " + var_documento
#     cursor.execute(sql, datos)
#     resultado = cursor.fetchall()
#     for x in resultado:
#         print(x)


# def modpersona():
#     sql = "UPDATE producto SET titulo = %s WHERE id = %s"
#     datos = ("producto1Modificado", 2)
#     micursor.execute(sql, datos)
#     mibase.commit()


# def eliminarpersona():
#     print("hola")


# VARIABLES
var_nombre = StringVar()
var_apellido = StringVar()
var_dni = StringVar()
var_correo = StringVar()
var_filiacion = StringVar()
# ---------- ALTA DE REGISTRO ---------------------------
registrasetitulo = Label(main, text="Registrarse", bg='#ced4db', font=fuentetit).grid(pady=10,row=1, column=0, columnspan=2)
nombre = Label(main, text="Nombre", bg='#F0F7DA', font=fuentecue).grid(column=0, row=2)
nombreEntry = Entry(main, textvariable=var_nombre).grid(column=1, row=2)

apellido = Label(main, text="Apellido", bg='#F0F7DA', font=fuentecue).grid(column=0, row=3)
apellidoEntry = Entry(main,textvariable=var_apellido).grid(column=1, row=3)

dni = Label(main, text="Dni", bg='#F0F7DA', font=fuentecue).grid(column=0, row=4)
dnientry = Entry(main,textvariable=var_apellido).grid(column=1, row=4)

correo = Label(main, text="Correo", bg='#F0F7DA', font=fuentecue).grid(column=0, row=5)
correoentry = Entry(main,textvariable=var_apellido).grid(column=1, row=5)

filiacion = Label(main, text="Filiacion",bg='#F0F7DA', font=fuentecue).grid(column=0, row=6)
filiacionentry = Entry(main,textvariable=var_apellido).grid(column=1, row=6)

boton_reg = Button(main, text="Registrar", bg='#65B8A6').grid(pady=10, row=7, column=0, columnspan=2)

# ------------ CONSULTA Y EDITAR -------------------

consultatitulo = Label(main, text="Consulta", bg='#ced4db', font=fuentetit).grid(pady=10, row=1, column=3, columnspan=2)
nombrec = Label(main, text="Nombre", bg='#F0F7DA', font=fuentecue).grid(column=3, row=2)
nombrecEntry = Entry(main, textvariable=var_nombre).grid(column=4, row=2)

apellidoc = Label(main, text="Apellido", bg='#F0F7DA', font=fuentecue).grid(column=3, row=3)
apellidocEntry = Entry(main,textvariable=var_apellido).grid(column=4, row=3)

dnic = Label(main, text="Dni", bg='#F0F7DA', font=fuentecue).grid(column=3, row=4)
dnicentry = Entry(main,textvariable=var_apellido).grid(column=4, row=4)

correoc = Label(main, text="Correo", bg='#F0F7DA', font=fuentecue).grid(column=3, row=5)
correocentry = Entry(main,textvariable=var_apellido).grid(column=4, row=5)

filiacionc = Label(main, text="Filiacion", bg='#F0F7DA', font=fuentecue).grid(column=3, row=6)
filiacioncentry = Entry(main,textvariable=var_apellido).grid(column=4, row=6)

# INPUT MODIFICACION/CONSULTA

dniconsulta = Label(main, text="Ingrese Documento", bg='#F0F7DA', font=fuentecue).grid(pady=10, column=0, row=8)
dniconsultaentry = Entry(main,textvariable=var_apellido).grid(column=1, row=8)

boton_mod = Button(main, text="Consultar", bg='#2d6073').grid(padx=10, row=8, column=2)
boton_con = Button(main, text="Modificar", bg='#65B8A6').grid(padx=10, row=8, column=3)
boton_eli = Button(main, text="Eliminar", bg='#ced4db').grid(padx=10, row=8, column=4)

# MUESTRA DE BASE

tree = ttk.Treeview(main)
tree["columns"] = ("col1", "col2", "col3", "col4")
tree.column("#0", minwidth=40, anchor="n")  # no tiene encabezado porque ya existe
tree.column("col1", minwidth=80, anchor="n")
tree.column("col2", minwidth=80, anchor="n")
tree.column("col3", minwidth=60, anchor="n")
tree.column("col4", minwidth=60, anchor="n")

# Encabezado de las columnas del Treeview
tree.heading("#0", text="ID", anchor="n")
tree.heading("col1", text="Nombre", anchor="n")
tree.heading("col2", text="Apellido", anchor="n")
tree.heading("col3", text="Dni", anchor="n")
tree.heading("col4", text="Correo", anchor="n")

tree.grid(row=9, columnspan=5, pady=5)







main.mainloop()