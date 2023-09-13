from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import sqlite3


mi_id = 0
main = Tk()
main.title("System UTNBA")
main.configure(bg='#F0F7DA')
titulo = Label(main, text="System UTNBA", width=80, foreground='#F0F7DA', bg='#1F192F', font='Arial 15 bold').grid(pady=10, row=0, columnspan=5)
fuentetit = 'Arial 11'
fuentecue = 'Arial 10'


# CONEXION BASE DE DATOS
db = sqlite3.connect("baseTPinicial.db")
cursor = db.cursor()
sql = "CREATE TABLE IF NOT EXISTS personas(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50) NOT NULL, apellido VARCHAR(50) NOT NULL, documento INT NOT NULL, correo VARCHAR(50) NOT NULL, filiacion VARCHAR(50))"
cursor.execute(sql)
db.commit()


def regpersona():
    global mi_id
    mi_id += 1
    sql = "INSERT INTO personas (nombre, apellido, documento, correo, filiacion) VALUES (?,?,?,?,?)"
    datos = (var_nombre.get(),var_apellido.get(),var_dni.get(),var_correo.get(),var_filiacion.get())
    cursor.execute(sql, datos)
    db.commit()
    tree.insert("", "end", text=str(mi_id),values=(var_nombre.get(), var_apellido.get(),var_dni.get(),var_correo.get(),var_filiacion.get()))


def conspersona():
    if var_dnic.get() != "":
        sql = "SELECT * FROM personas WHERE documento = " + var_dnic.get()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if resultado !=[] :
            showinfo("El resultado es:", resultado)
        else:
            showerror("Error", "No existe en la base de datos")
    else:
        showwarning("Error", "Por favor ingrese un valor numerico")


def modpersona():
    if var_dnic.get() != "":
        sql = "UPDATE producto SET titulo = %s WHERE id = %s"
        datos = ("producto1Modificado", 2)
        micursor.execute(sql, datos)
        mibase.commit()
    else:
        showwarning("Error", "Por favor ingrese un valor numerico")


def eliminarpersona():
    if var_dnic.get() != "":
        if askyesno("Eliminar persona", "Esta seguro que desea eliminar esta persona"):
            sql = "DELETE FROM personas WHERE documento =" + var_dnic.get()
            cursor.execute(sql)
            showinfo("Eliminar", "Usuario eliminado")
        else:
            showinfo("Salir", "Esta a punto de salir")
    else:
        showwarning("Error", "Por favor ingrese un valor numerico")


# VARIABLES
var_nombre = StringVar()
var_apellido = StringVar()
var_dni = StringVar()
var_correo = StringVar()
var_filiacion = StringVar()
var_dnic = StringVar()
# ---------- ALTA DE REGISTRO ---------------------------
registrasetitulo = Label(main, text="Registrarse", bg='#ced4db', font=fuentetit).grid(pady=10,row=1, column=0, columnspan=2)
nombre = Label(main, text="Nombre", bg='#F0F7DA', font=fuentecue).grid(column=0, row=2)
nombreentry = Entry(main, textvariable=var_nombre).grid(column=1, row=2)

apellido = Label(main, text="Apellido", bg='#F0F7DA', font=fuentecue).grid(column=0, row=3)
apellidoentry = Entry(main,textvariable=var_apellido).grid(column=1, row=3)

dni = Label(main, text="Dni", bg='#F0F7DA', font=fuentecue).grid(column=0, row=4)
dnientry = Entry(main,textvariable=var_dni).grid(column=1, row=4)

correo = Label(main, text="Correo", bg='#F0F7DA', font=fuentecue).grid(column=0, row=5)
correoentry = Entry(main,textvariable=var_correo).grid(column=1, row=5)

filiacion = Label(main, text="Filiacion",bg='#F0F7DA', font=fuentecue).grid(column=0, row=6)
filiacionentry = Entry(main,textvariable=var_filiacion).grid(column=1, row=6)

boton_reg = Button(main, text="Registrar", bg='#65B8A6', command=regpersona).grid(pady=10, row=7, column=0, columnspan=2)

"""
------------ CONSULTA Y EDITAR -------------------

nombrec = Label(main, text="Nombre", bg='#F0F7DA', font=fuentecue).grid(column=3, row=2)
nombrecEntry = Entry(main, textvariable=var_nombre).grid(column=4, row=2)

apellidoc = Label(main, text="Apellido", bg='#F0F7DA', font=fuentecue).grid(column=3, row=3)
apellidocEntry = Entry(main).grid(column=4, row=3)

dnic = Label(main, text="Dni", bg='#F0F7DA', font=fuentecue).grid(column=3, row=4)
dnicentry = Entry(main).grid(column=4, row=4)

correoc = Label(main, text="Correo", bg='#F0F7DA', font=fuentecue).grid(column=3, row=5)
correocentry = Entry(main).grid(column=4, row=5)

filiacionc = Label(main, text="Filiacion", bg='#F0F7DA', font=fuentecue).grid(column=3, row=6)
filiacioncentry = Entry(main).grid(column=4, row=6)
"""
# INPUT MODIFICACION/CONSULTA
consultatitulo = Label(main, text="Consulta", bg='#ced4db', font=fuentetit).grid(pady=10, row=1, column=2, columnspan=3)
dniconsulta = Label(main, text="Ingrese Documento", bg='#F0F7DA', font=fuentecue).grid(pady=10, column=2, row=2)
dniconsultaentry = Entry(main, textvariable=var_dnic).grid(column=4, row=2 )

boton_mod = Button(main, text="Consultar", bg='#2d6073', command=conspersona).grid(column=2, row=3)
boton_con = Button(main, text="Modificar", bg='#65B8A6', command=modpersona).grid(row=3, column=3)
boton_eli = Button(main, text="Eliminar", bg='#ced4db', command=eliminarpersona).grid(row=3, column=4)

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