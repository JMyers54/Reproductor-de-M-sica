from tkinter import PhotoImage, filedialog,ttk
import random
import mutagen
import pygame.mixer as mx
import tkinter.ttk as ttk
from mutagen.mp3 import MP3
import time

class Funciones():
    def __init__(self, estado, btnPausa, btnStop, btnResume, btnPlay, progreso, lblDuracion):
        self.estado = estado
        self.btnPausa = btnPausa
        self.rutaActual = r"Reproductor-de-M-sica\sounds\Pista.mp3"
        self.btnStop = btnStop
        self.btnResume = btnResume
        self.btnPlay = btnPlay
        self.progreso = progreso
        self.lblDuracion = lblDuracion
        self.canciónActual = r"Reproductor-de-M-sica\sounds\Pista.mp3"
        mx.music.load(self.canciónActual)
        self.pausado = False
    
    def archivoMP3(self, event=None):
        archivo = filedialog.askopenfilename(title="Abrir archivo de música",filetypes=[("archivos MP3","*.mp3")])
        if archivo:
            try:
                self.rutaActual = archivo
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
            audio = MP3(self.rutaActual)
        self.duracion = int(audio.info.length)
        self.progreso.config(to=self.duracion)

        minutos = self.duracion // 60
        segundos = self.duracion % 60
        tiempo_formateado = f"{minutos:02}:{segundos:02}"
        self.lblDuracion.config(text=tiempo_formateado)

        self.BarraDeProgreso()


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

    def BarraDeProgreso(self):
        if mx.music.get_busy():
            pos = mx.music.get_pos() // 1000
            self.progreso.set(pos)
            self.estado.after(1000, self.BarraDeProgreso)