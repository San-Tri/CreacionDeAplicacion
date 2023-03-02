from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Products application')
        # Crear un frame dentro de contenedor
        frame = LabelFrame(self.wind, text='Ferreteria El Tornillo Feliz')
        frame.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Entrada para un nombre:
        Label(frame, text='DNI  ').grid(row=1, column=0)
        self.dni = Entry(frame)
        self.dni.grid(row=1, column=1)
        
        # Colocar otro elemento:
        Label(frame, text= 'Apellidos ').grid(row =2, column=0)
        self.apellido = Entry(frame)
        self.apellido.grid(row=2, column=1)
        
        Label(frame, text="Nombres ").grid(row=2, column=2)
        self.nombre = Entry(frame)
        self.nombre.grid(row=2, column=3)
        
        Label(frame, text="Direccion ").grid(row=3, column=0)
        self.direccion = Entry(frame)
        self.direccion.grid(row=3, column=1, columnspan=3, sticky=W + E)
        
        Label(frame, text="Telefono ").grid(row=4, column=0)
        self.telefono = Entry(frame)
        self.telefono.grid(row=4, column=1)
if __name__== '__main__' :
    window = Tk()
    application = Product(window)
    window.mainloop()