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
        
        #     
if __name__== '__main__' :
    window = Tk()
    application = Product(window)
    window.mainloop()