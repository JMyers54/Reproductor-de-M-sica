from tkinter import PhotoImage, filedialog,ttk
import random
import mutagen
import pygame.mixer as mx


class Funciones():
    def __init__(self):
        def  archivo_mp3(self):
            global dirrecion, pos, n ,canción_actual
            pos = 0
            n = 0
            dirrecion = filedialog.askopenfilename(title="selección de archivos mp3",filetypes=[("mp3 files","*.mp3*"),("All files","*.*")])
            n = len(dirrecion)
            canción_actual = dirrecion[pos]
            nombre_cancion = canción_actual.split("/")
            nombre_cancion = nombre_cancion[-1]
            cancion_actual=''
            direccion=''

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

