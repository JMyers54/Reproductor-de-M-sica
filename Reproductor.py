import tkinter as tk
from tkinter import *
from Tooltip import Tooltip
from funciones import Funciones
import pygame.mixer as mx
import tkinter.ttk as ttk
from mutagen.mp3 import MP3
import time
from tkinter import messagebox

class Reproductor():
    def __init__(self):
        mx.init(frequency=44100)

        self.ventana = tk.Tk()
        self.ventana.title("🎧Mi Reproductor")
        self.ventana.config(width=800, height=600, bg="#1e1e2f")
        self.ventana.resizable(0,0)

        self.iconoPlay = tk.PhotoImage(file=r"icons\control_play_blue.png")
        self.iconoPausa = tk.PhotoImage(file=r"icons\control_pause_blue.png")
        self.iconoStop = tk.PhotoImage(file=r"icons\control_stop_blue.png")
        self.iconoResume = tk.PhotoImage(file=r"icons\control_end_blue.png")
        self.iconoCarpeta = tk.PhotoImage(file=r"icons\folder.png")
        self.iconoAyuda = tk.PhotoImage(file=r"icons/help.png")

        self.estado = tk.Label(self.ventana, text="Cargando...", font=("Arial", 20, "bold"), fg="white", bg="#1e1e2f")
        self.estado.place(relx=0.5, rely=0.48, anchor="center")
        
        self.btnAyuda = tk.Button(self.ventana, image=self.iconoAyuda, command=self.mostrar_ayuda)
        self.btnAyuda.place(relx=0.95, rely=0.0, x=-10, y=10, width=35, height=35)
        Tooltip(self.btnAyuda,"Precione para abrir ayuda")
        
        self.btnPlay = tk.Button(self.ventana, image=self.iconoPlay)
        self.btnPlay.place(relx=0.48, rely=0.8, x=10, width=35, height=35)
        Tooltip(self.btnPlay, "Presione para reproducir la canción")

        self.btnPausa = tk.Button(self.ventana, image=self.iconoPausa, state="disabled")
        self.btnPausa.place(relx=0.48, rely=0.8, x=-35, width=35, height=35)
        Tooltip(self.btnPausa, "Presione para pausar la reproducción")

        self.btnStop = tk.Button(self.ventana, image=self.iconoStop, state="disabled")
        self.btnStop.place(relx=0.48, rely=0.8, x=-80, width=35, height=35)
        Tooltip(self.btnStop, "Presione para detener la reproducción")

        self.btnResume = tk.Button(self.ventana, image=self.iconoResume, state="disabled")
        self.btnResume.place(relx=0.48, rely=0.8, x=55, width=35, height=35)
        Tooltip(self.btnResume, "Presione para despausar la reproducción")

        self.btnMp3 = tk.Button(self.ventana, image=self.iconoCarpeta, state="disabled" )
        self.btnMp3.place(relx=0.54, rely=0.8, x=55, width=35, height=35)
        Tooltip(self.btnMp3, "importar canción")

        self.progreso = ttk.Scale(self.ventana, from_=0, to=100, orient="horizontal", length=450)
        self.progreso.place(relx=0.5, rely=0.7, anchor="center")
        self.acciones = Funciones(self.estado, self.btnPausa, self.btnStop, self.btnResume, self.btnPlay, self.progreso)

        self.btnPlay.bind("<Button-1>", self.acciones.play)
        self.btnPausa.bind("<Button-1>", self.acciones.pausa)
        self.btnStop.bind("<Button-1>", self.acciones.stop)
        self.btnResume.bind("<Button-1>", self.acciones.resume)
        self.btnMp3.bind("<Button-1>", self.acciones.archivoMP3)
        
        self.ventana.mainloop()
       
   
