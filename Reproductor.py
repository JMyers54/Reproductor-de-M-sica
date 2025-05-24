import tkinter as tk
from tkinter import PhotoImage, filedialog,ttk
import random
import mutagen
from tkinter import *
from Tooltip import Tooltip

import pygame.mixer as mx

class Reproductor():

    def  archivo_mp3(self):
        global dirrecion, pos, n ,canción_actual
        pos = 0
        n = 0
        dirrecion = filedialog.askopenfilename(title="selección de archivos mp3",filetypes=[("mp3 files","*.mp3"),("All files","*.*")])
        n = len(dirrecion)
        canción_actual = dirrecion[pos]

        nombre_cancion = canción_actual.split("/")
        nombre_cancion = nombre_cancion[-1]
    lista = []
    for i in range(50,200,10):
        lista.append(i)
    
    def play(self, event):
        mx.music.load(r"sounds\Pista.mp3")
        mx.music.play()
        self.estado.config(text="Reproduciendo...")
        self.btnPausa.config(state="normal")
        self.btnStop.config(state="normal")
        self.btnResume.config(state="normal")
        self.btnPlay.config(state="disabled")
    
    def stop(self, event):
        mx.music.stop()
        self.estado.config(text="Reproducción detenida...")
        self.btnPlay.config(state="normal")
        self.btnPausa.config(state="disabled")
        self.btnStop.config(state="disabled")
        self.btnResume.config(state="disabled")

    def pausa(self, event):
        mx.music.pause()
        self.estado.config(text="Reproducción pausada...")

    def resume(self, event):
        mx.music.unpause()
        self.estado.config(text="Reproduciendo...")

    def __init__(self):
        mx.init()

        mx.init()
        mx.init(frequency=44100)
        cancion_actual=''
        direccion=''

        self.ventana = tk.Tk()
        self.ventana.title("Mi Reproductor")
        self.ventana.config(width=800, height=600)
        self.ventana.resizable(0,0)

        self.iconoPlay = tk.PhotoImage(file=r"icons\control_play_blue.png")
        self.iconoPausa = tk.PhotoImage(file=r"icons\control_pause_blue.png")
        self.iconoStop = tk.PhotoImage(file=r"icons\control_stop_blue.png")
        self.iconoResume = tk.PhotoImage(file=r"icons\control_end_blue.png")

        self.estado = tk.Label(self.ventana, text="Cargando...")
        self.estado.place(relx=0.5, rely=0.5, anchor="center")

        self.btnPlay = tk.Button(self.ventana, image=self.iconoPlay)
        self.btnPlay.place(relx=0.5, rely=0.9, x=10, width=25, height=25)
        self.btnPlay.bind("<Button-1>", self.play)
        Tooltip(self.btnPlay, "Presione para reproducir la canción")

        self.btnPausa = tk.Button(self.ventana, image=self.iconoPausa, state="disabled")
        self.btnPausa.place(relx=0.5, rely=0.9, x=-35, width=25, height=25)
        self.btnPausa.bind("<Button-1>", self.pausa)
        Tooltip(self.btnPausa, "Presione para pausar la reproducción")

        self.btnStop = tk.Button(self.ventana, image=self.iconoStop, state="disabled")
        self.btnStop.place(relx=0.5, rely=0.9, x=-80, width=25, height=25)
        self.btnStop.bind("<Button-1>", self.stop)
        Tooltip(self.btnStop, "Presione para detener la reproducción")

        self.btnResume = tk.Button(self.ventana, image=self.iconoResume, state="disabled")
        self.btnResume.place(relx=0.5, rely=0.9, x=55, width=25, height=25)
        self.btnResume.bind("<Button-1>", self.resume)
        Tooltip(self.btnResume, "Presione para despausar la reproducción")

        self.ventana.mainloop()