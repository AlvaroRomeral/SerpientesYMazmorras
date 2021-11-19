from tkinter import *
from Gestores import GestorNivel as GN
import os

from SerpientesYMazmorras.Personajes.Jugador import Jugador

jugador = Jugador(Jugador, 100)
# Crear instancia de pantalla
pantalla = Tk()


def nuevaPartida():
    global pantalla
    pantalla = GN.pantallaJuego()
    pantalla.mainloop()


def cargarPartida():
    pass


def salirJuego():
    pantalla.quit()


pantalla.title("Serpientes y Mazmorras")
pantalla.configure(width=500, height=500)
pantalla.resizable(False, False)
Label(pantalla, text="Bienvenido a Serpientes y Mazmorras").place(x=10, y=400)
canvas = Canvas(pantalla, width=500, height=400, background="black")
imgFondo = PhotoImage(master=canvas, width=400, height=400, file="Images/Fondo3.png")
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=imgFondo, anchor="nw")
Button(pantalla, text="Empezar a Jugar", command=nuevaPartida).place(x=10, y=445)
Button(pantalla, text="Cargar Partida").place(x=210, y=445)
Button(pantalla, text="Salir").place(x=400, y=445)
pantalla.mainloop()

