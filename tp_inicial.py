from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import sqlite3
import re

mi_id = 0
main = Tk()
main.title("System UTNBA")
main.configure(bg='#F0F7DA')
titulo = Label(main, text="System UTNBA", width=80, foreground='#F0F7DA', bg='#1F192F', font='Arial 15 bold').grid(pady=10, row=0, columnspan=6)
fuentetit = 'Arial 11'
fuentecue = 'Arial 10'
patrondni = "^[0-9]+(?i:[ _-][0-9]+)*$"

db = sqlite3.connect("baseTPinicial.db")
cursor = db.cursor()
sql = "CREATE TABLE IF NOT EXISTS personas(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50) NOT NULL, apellido VARCHAR(50) NOT NULL, documento INT NOT NULL, correo VARCHAR(50) NOT NULL, filiacion VARCHAR(50))"
cursor.execute(sql)
db.commit()

def regpersona():
    patron = "^[A-Za-z]+(?i:[ _-][A-Za-z]+)*$"
    resultadodni = busquedadni(var_dni.get())
    if (re.match(patron, var_nombre.get()) and re.match(patrondni, var_dni.get()) and re.match(patron, var_apellido.get())):
        if (resultadodni ==[]):
            sql = "INSERT INTO personas (nombre, apellido, documento, correo, filiacion) VALUES (?,?,?,?,?)"
            datos = (var_nombre.get(),var_apellido.get(),var_dni.get(),var_correo.get(),combo.get())
            cursor.execute(sql, datos)
            db.commit()
            mostrardb()
            var_nombre.set('')
            var_apellido.set('')
            var_dni.set('')
            var_correo.set('')
            combo.set('')
        else:
            showwarning("Error", "El dni ingresado ya existe en la base, ingrese otro")
    else:
        showerror("Error", "No es posible guardar")
   
def busquedadni(var):
    sql = "SELECT * FROM personas WHERE documento = " + var
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado

def conspersona():
    if (re.match(patrondni, var_dnic.get())):
        resultado = busquedadni(var_dnic.get())
        if resultado !=[] :
            showinfo("El resultado es:", resultado)
        else:
            showerror("Error", "No existe en la base de datos")
    else:
        showwarning("Error", "Por favor ingrese un valor valido")


def modpersona():
    global botonmod
    if (re.match(patrondni, var_dnic.get())):
        resultado = busquedadni(var_dnic.get())
        if resultado !=[]:
            sql = "SELECT * FROM personas WHERE documento = " + var_dnic.get()
            cursor.execute(sql)
            persona = cursor.fetchone()
            var_nombre.set(persona[1])
            var_apellido.set(persona[2])
            var_dni.set(persona[3])
            var_correo.set(persona[4])
            combo.set(persona[5])
            botonmod = Button(main, text="Aceptar", bg='#65B8A6', command=modificarendb)
            botonmod.grid(row=7, column=1, columnspan=2)
        else:
            showerror("Error", "No existe en la base de datos")
    else:
        showwarning("Error", "Por favor ingrese un valor numerico")

def modificarendb():
    if askyesno("Modificar persona", "¿Esta seguro que desea modificar esta persona?"):
        sql = "UPDATE personas SET nombre=?, apellido=?, documento=?, correo=?, filiacion=? WHERE documento = " + var_dnic.get()
        datos = (var_nombre.get(),var_apellido.get(),var_dni.get(),var_correo.get(),combo.get())
        cursor.execute(sql, datos)
        db.commit()
        mostrardb()
        var_nombre.set('')
        var_apellido.set('')
        var_dni.set('')
        var_correo.set('')
        combo.set('')
    else:
        showinfo("Salir", "Esta a punto de salir")
    botonmod.destroy()
    var_nombre.set('')
    var_apellido.set('')
    var_dni.set('')
    var_correo.set('')
    combo.set('')
    


def eliminarpersona():
    if (re.match(patrondni, var_dnic.get())):
        resultado = busquedadni(var_dnic.get())
        if resultado !=[]:
            if askyesno("Eliminar persona", "Esta seguro que desea eliminar esta persona"):
                sql = "DELETE FROM personas WHERE documento = " + var_dnic.get()
                cursor.execute(sql)
                db.commit()
                mostrardb()
                showinfo("Eliminar", "Usuario eliminado")
            else:
                showinfo("Salir", "Esta a punto de salir")
        else:
            showerror("Error", "No existe en la base de datos")
    else:
        showwarning("Error", "Por favor ingrese un valor numerico")


# VARIABLES
var_nombre = StringVar()
var_apellido = StringVar()
var_dni = StringVar()
var_correo = StringVar()
var_dnic = StringVar()
# ---------- ALTA DE REGISTRO ---------------------------
registrasetitulo = Label(main, text="Registrarse", bg='#ced4db', font=fuentetit).grid(pady=10,row=1, column=1, columnspan=2)
nombre = Label(main, text="Nombre", bg='#F0F7DA', font=fuentecue).grid(column=1, row=2)
nombreentry = Entry(main, textvariable=var_nombre).grid(column=2, row=2)

apellido = Label(main, text="Apellido", bg='#F0F7DA', font=fuentecue).grid(column=1, row=3)
apellidoentry = Entry(main,textvariable=var_apellido).grid(column=2, row=3)

dni = Label(main, text="Dni", bg='#F0F7DA', font=fuentecue).grid(column=1, row=4)
dnientry = Entry(main,textvariable=var_dni).grid(column=2, row=4)

correo = Label(main, text="Correo", bg='#F0F7DA', font=fuentecue).grid(column=1, row=5)
correoentry = Entry(main,textvariable=var_correo).grid(column=2, row=5)

filiacion = Label(main, text="Filiacion",bg='#F0F7DA', font=fuentecue).grid(column=1, row=6, pady=3)
#filiacionentry = Entry(main,textvariable=var_filiacion).grid(column=1, row=6)

boton_reg = Button(main, text="Registrar", bg='#65B8A6', command=regpersona).grid(pady=10, row=7, column=1, columnspan=2)

combo = ttk.Combobox(
    state="readonly",
    values=["Docente", "No Docente", "Alumno", "Monotributista"]
)
combo.grid(column=2,row=6)

# INPUT MODIFICACION/CONSULTA
consultatitulo = Label(main, text="Consulta", bg='#ced4db', font=fuentetit).grid(pady=10, row=1, column=3, columnspan=2)
dniconsulta = Label(main, text="Ingrese Documento", bg='#F0F7DA', font=fuentecue).grid(column=3, row=2)
dniconsultaentry = Entry(main, textvariable=var_dnic).grid(column=4, row=2 )

boton_con = Button(main, text="Consultar", bg='#2d6073', command=conspersona).grid(column=3, row=4, columnspan=2)
boton_mod = Button(main, text="Modificar", bg='#65B8A6', command=modpersona).grid(row=3, column=3)
boton_eli = Button(main, text="Eliminar", bg='#ced4db', command=eliminarpersona).grid(row=3, column=4)
# MUESTRA DE BASE

tree = ttk.Treeview(main, show="headings")
tree["columns"] = ("1", "2", "3", "4", "5", "6")
tree.column("1", minwidth=40, anchor="n")  # no tiene encabezado porque ya existe
tree.column("2", minwidth=80, anchor="n")
tree.column("3", minwidth=80, anchor="n")
tree.column("4", minwidth=60, anchor="n")
tree.column("5", minwidth=60, anchor="n")
tree.column("6", minwidth=60, anchor="n")

# Encabezado de las columnas del Treeview
tree.heading("1", text="ID", anchor="n")
tree.heading("2", text="Nombre", anchor="n")
tree.heading("3", text="Apellido", anchor="n")
tree.heading("4", text="Dni", anchor="n")
tree.heading("5", text="Correo", anchor="n")
tree.heading("6", text="Filiacion", anchor="n")

def mostrardb():
    sql = "SELECT * FROM personas"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    registros= tree.get_children()
    for x in registros:
        tree.delete(x)
    for i in resultado:
        tree.insert("", 'end', values=i)

tree.grid(row=9, columnspan=6, pady=5)
mostrardb()

main.mainloop()
