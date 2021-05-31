import tkinter
from tkinter import StringVar, ttk
import sqlite3
from os import curdir
from tkinter import messagebox
from sqlite3.dbapi2 import Cursor

ventana=tkinter.Tk()
ventana.title("App")

ventana.geometry("700x500")


id=StringVar()
nombre=StringVar()
direccion=StringVar()
telefono=StringVar()

def conexionBD():
    Conexion=sqlite3.connect("base")
    Cursor=Conexion.cursor()

    try:
        Cursor.execute('''
            CREATE TABLE agenda(
            id integer primary key autoincrement,
            nombre varchar(50) not null,
            direccion varchar(50) not null,
            telefono varchar(14) not null)
            ''')
        messagebox.showinfo("Conexion", "BD creada con exito")
    except:

        messagebox.showinfo("Conexion", "exito en la conexion con la BD")





notebook=ttk.Notebook(ventana)
notebook.pack()

pes1=ttk.Frame(notebook,width=700,height=700)
pes2=ttk.Frame(notebook)

notebook.add(pes1,text="Inicio")
notebook.add(pes2,text="ayuda")

ayuda=ttk.Label(pes2,text="ayuda.com")
ayuda.pack()


nombre=ttk.Label(pes1,text="Nombre",font=("Roboto",12))
direccion=ttk.Label(pes1,text="Direccion",font=("Roboto",12))
telefono=ttk.Label(pes1,text="Teléfono",font=("Roboto",12))

Entry1=tkinter.Entry(pes1)
Entry1.config(width=50)
Entry2=tkinter.Entry(pes1)
Entry2.config(width=50)
Entry3=tkinter.Entry(pes1)
Entry3.config(width=20)


nombre.place(x=10,y=20)
direccion.place(x=10,y=50)
telefono.place(x=10,y=80)

Entry1.place(x=100,y=20)
Entry2.place(x=100,y=50)
Entry3.place(x=100,y=80)
    






BotonEnvia=tkinter.Button(pes1,text="Crear",command=conexionBD,bg="green",fg="white")
BotonEnvia.place(x=20,y=150)
BotonEnvia=tkinter.Button(pes1,text="Modificar",command=conexionBD,bg="orange",fg="white")
BotonEnvia.place(x=80,y=150)
BotonEnvia=tkinter.Button(pes1,text="Eliminar",command=conexionBD,bg="red",fg="white")
BotonEnvia.place(x=150,y=150)

tree=ttk.Treeview(pes1,height=10,columns=("#0","#1","#2"))
tree.place(x=30,y=260)
tree.column("#0",width=50)
tree.heading("#0",text="ID",anchor=tkinter.CENTER)
tree.heading("#1",text="Nombre",anchor=tkinter.CENTER)
tree.heading("#2",text="Dirección",anchor=tkinter.CENTER)
tree.heading("#3",text="Teléfono")
 
#tree.insert('',0,text="1",values=("hola","hola","hola"))


ventana.mainloop()






#hola