from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Products application')
        # Crear un frame dentro de contenedor
        frame = LabelFrame(self.wind, text='Registre un nuevo producto.')
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        
        # Entrada para un nombre con input:
        Label(frame, text='Nombre: ').grid(row=1, column=0)
        self.nombre = Entry(frame)
        self.nombre.grid(row=1, column=1)
if __name__== '__main__' :
    window = Tk()
    application = Product(window)
    window.mainloop()