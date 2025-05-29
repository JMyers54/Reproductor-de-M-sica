from tkinter import PhotoImage, filedialog,ttk
import random
import mutagen
import pygame.mixer as mx


class Funciones():
    def __init__(self, estado, btnPausa, btnStop, btnResume, btnPlay):
        self.estado = estado
        self.btnPausa = btnPausa
        self.btnStop = btnStop
        self.btnResume = btnResume
        self.btnPlay = btnPlay
        self.canciónActual = r"sounds\Pista.mp3"
        mx.music.load(self.canciónActual)
        self.pausado = False
    
    def archivoMP3(self, event=None):
        archivo = filedialog.askopenfilename(title="Abrir archivo de música",filetypes=[("archivos MP3","*.mp3")])
        if archivo:
            try:
                mx.music.load(archivo)
                mx.music.play()
                self.estado.config(text=f"Reproduciendo:{archivo.split('/')[-1]}")
            except Exception as e:
                self.estado.config(text=f"Error la reproducir: {e}")
    def play(self, event):
        if self.pausado:
            mx.music.unpause()
            self.pausado = False
        else:
            mx.music.play()

        self.estado.config(text="Reproduciendo...")
        self.btnPausa.config(state="normal")
        self.btnStop.config(state="normal")
        self.btnResume.config(state="normal")
        self.btnPlay.config(state="disabled")
    
    def stop(self, event):
        mx.music.stop()
        self.pausado = False
        self.estado.config(text="Reproducción detenida...")
        self.btnPlay.config(state="normal")
        self.btnPausa.config(state="disabled")
        self.btnStop.config(state="disabled")
        self.btnResume.config(state="disabled")

    def pausa(self, event):
        mx.music.pause()
        self.pausado = True
        self.estado.config(text="Reproducción pausada...")

    def resume(self, event):
        mx.music.unpause()
        self.estado.config(text="Reproduciendo...")

