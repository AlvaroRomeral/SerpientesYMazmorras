from tkinter import *
from tkinter.ttk import Combobox


def pantallaMenu():
    pantalla = Tk()
    pantalla.title("Serpientes y Mazmorras")
    pantalla.configure(width=500, height=500)
    pantalla.resizable(False, False)
    Label(pantalla, text="Bienvenido a Serpientes y Mazmorras").place(x=10, y=400)
    imgFondo = PhotoImage(file="Images/Fondo3.png")
    canvas = Canvas(pantalla, width=500, height=400, background="black")
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=imgFondo, anchor="nw")
    Button(pantalla, text="Empezar a Jugar").place(x=10, y=445)
    Button(pantalla, text="Cargar Partida").place(x=210, y=445)
    Button(pantalla, text="Salir").place(x=400, y=445)
    return pantalla


def pantallaJuego():
    panatella = Tk()
    panatella.title("Serpientes y Mazmorras")
    panatella.configure(width=500, height=500)
    panatella.resizable(False, False)
    Label(panatella, text="Sala 1").place(x=10, y=400)
    canvas = Canvas(panatella, width=500, height=400, background="black")
    imgFondo = PhotoImage(master=canvas, file="Images/Fondo1.png")
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=imgFondo, anchor="nw")
    combo = Combobox(panatella)
    combo['values'] = (1, 2, 3, 4, 5, "Text")
    combo.current(1)  # set the selected item
    Button(panatella, text="Continuar Izquierda").place(x=10, y=445)
    Button(panatella, text="Continuar de Frente").place(x=210, y=445)
    Button(panatella, text="Continuar Derecha").place(x=400, y=445)
    return panatella
