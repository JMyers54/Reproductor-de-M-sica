import tkinter as tk
from tkinter import *
from Tooltip import Tooltip
from funciones import Funciones
import pygame.mixer as mx

class Reproductor():
    def __init__(self):

        self.funciones = Funciones()
        mx.init()

        mx.init()
        mx.init(frequency=44100)

        self.ventana = tk.Tk()
        self.ventana.title("Mi Reproductor")
        self.ventana.config(width=800, height=600, bg="#1F1F1F")
        self.ventana.resizable(0,0)

        self.iconoPlay = tk.PhotoImage(file=r"icons\control_play_blue.png")
        self.iconoPausa = tk.PhotoImage(file=r"icons\control_pause_blue.png")
        self.iconoStop = tk.PhotoImage(file=r"icons\control_stop_blue.png")
        self.iconoResume = tk.PhotoImage(file=r"icons\control_end_blue.png")

        self.estado = tk.Label(self.ventana, text="Cargando...")
        self.estado.place(relx=0.5, rely=0.5, anchor="center")

        self.btnPlay = tk.Button(self.ventana, image=self.iconoPlay)
        self.btnPlay.place(relx=0.5, rely=0.9, x=10, width=25, height=25)
        self.btnPlay.bind("<Button-1>", self.funciones.play)
        Tooltip(self.btnPlay, "Presione para reproducir la canción")

        self.btnPausa = tk.Button(self.ventana, image=self.iconoPausa, state="disabled")
        self.btnPausa.place(relx=0.5, rely=0.9, x=-35, width=25, height=25)
        self.btnPausa.bind("<Button-1>", self.funciones.pausa)
        Tooltip(self.btnPausa, "Presione para pausar la reproducción")

        self.btnStop = tk.Button(self.ventana, image=self.iconoStop, state="disabled")
        self.btnStop.place(relx=0.5, rely=0.9, x=-80, width=25, height=25)
        self.btnStop.bind("<Button-1>", self.funciones.stop)
        Tooltip(self.btnStop, "Presione para detener la reproducción")

        self.btnResume = tk.Button(self.ventana, image=self.iconoResume, state="disabled")
        self.btnResume.place(relx=0.5, rely=0.9, x=55, width=25, height=25)
        self.btnResume.bind("<Button-1>", self.funciones.resume)
        Tooltip(self.btnResume, "Presione para despausar la reproducción")

        self.btonImportar = tk.Button(self.ventana)
        self.btonImportar.place(relx=0.5,rely=0.9, x=80, width=25, height=25)

        self.ventana.mainloop()