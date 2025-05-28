from tkinter import PhotoImage, filedialog,ttk
import random
import mutagen
import pygame.mixer as mx


class Funciones():
    def __init__(self,estado,):
        self.estado = estado

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

