# -*- coding: utf-8 -*-
from salsaDao import salsaDao
from tkinter import *
from tkinter import ttk
import os

salsadao = salsaDao()

window = Tk()
import tkinter as tk

window.title("Salsita")

# gives weight to the cells in the grid
rows = 0
while rows < 50:
    window.rowconfigure(rows, weight=1)
    window.columnconfigure(rows, weight=1)
    rows += 1
    

 
# Defines and places the notebook widget
nb = ttk.Notebook(window)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='Registrar')
 

try:
    def salir():
        basero.desconectar()
        return os._exit(0)
except SystemExit as er :
    print(er)
    
def buscaShit():
    
    cajaasegurado.delete(0,'end')
    cajaasegurado.insert(0,salsadao.devolverPalabra(cajapoliza.get()))
    
   
   
    
    


        
    
tk.Label(page1,text = "Ingrese letra",borderwidth = 20).grid(row =10,column =10)
cajapoliza = tk.Entry(page1)
cajapoliza.grid(row = 10 , column = 11)
botonaceptarregi =tk.Button(page1,text = "Busca esa shit", borderwidth = 3,command = buscaShit).grid(row = 14,column =11)

tk.Label(page1,text = "Su shit:",borderwidth = 20).grid(row = 17 , column = 10)
cajaasegurado = tk.Entry(page1)
cajaasegurado.grid(row = 17 , column = 11)





window.mainloop()




