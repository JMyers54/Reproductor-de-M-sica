from tkinter import PhotoImage, filedialog, ttk
import random
import mutagen
import pygame
import pygame.mixer as mx
import tkinter.ttk as ttk
from mutagen.mp3 import MP3
import time
import os

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
        mx.init()
        pygame.init()
        pygame.display.set_mode((1,1))
        mx.music.load(self.canciónActual)
        self.pausado = False

    def carpeta(self, event=None):
        carpeta = filedialog.askdirectory(title="Abrir la carpeta de música")
        if not carpeta:
            return

        self.listaCanción = [f for f in os.listdir(carpeta) if f.endswith(".mp3")]
        self.listaCanción.sort()
        self.UbicaciónActual = 0
        self.carpetaActual = carpeta

        if self.listaCanción:
            self.reproducirSiguienteCanción()
        else:
            self.estado.config(text="No hay archivos MP3 en esta carpeta.")

    def reproducirSiguienteCanción(self, event=None):
        if self.UbicaciónActual >= len(self.listaCanción):
            self.estado.config(text="Se terminó la lista de reproducción.")
            return

        archivo = os.path.join(self.carpetaActual, self.listaCanción[self.UbicaciónActual])
        self.rutaActual = archivo
        self.canciónActual = archivo

        try:
            mx.music.load(archivo)
            mx.music.play()
            self.estado.config(text=f"Reproduciendo: {os.path.basename(archivo)}")

            audio = MP3(archivo)
            self.duracion = int(audio.info.length)
            self.progreso.config(to=self.duracion)

            minutos = self.duracion // 60
            segundos = self.duracion % 60
            tiempo_formateado = f"{minutos:02}:{segundos:02}"
            self.lblDuracion.config(text=tiempo_formateado)

            self.BarraDeProgreso()

            # Configura evento al terminar la canción
            mx.music.set_endevent(pygame.USEREVENT)
            self.estado.after(500, self.verificarEvento)

        except Exception as e:
            self.estado.config(text=f"Error: {e}")

    def verificarEvento(self, event=None):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.UbicaciónActual += 1
                self.reproducirSiguienteCanción()
                return
        self.estado.after(500, self.verificarEvento)

    def play(self, event=None):
        if self.pausado:
            mx.music.unpause()
            self.pausado = False
        else:
            mx.music.play()
            audio = MP3(self.canciónActual)
            self.duracion = int(audio.info.length)
        self.progreso.config(to=self.duracion)

        minutos = self.duracion // 60
        segundos = self.duracion % 60
        tiempo_formateado = f"{minutos:02}:{segundos:02}"
        self.lblDuracion.config(text=tiempo_formateado)

        self.BarraDeProgreso()

        self.estado.config(text=f"{self.canciónActual}")
        self.btnPausa.config(state="normal")
        self.btnStop.config(state="normal")
        self.btnResume.config(state="normal")
        self.btnPlay.config(state="disabled")

    def stop(self, event=None):
        mx.music.stop()
        self.pausado = False
        self.estado.config(text="Reproducción detenida...")
        self.btnPlay.config(state="normal")
        self.btnPausa.config(state="disabled")
        self.btnStop.config(state="disabled")
        self.btnResume.config(state="disabled")

    def pausa(self, event=None):
        mx.music.pause()
        self.pausado = True
        self.estado.config(text="Reproducción pausada...")
    
    def BarraDeProgreso(self):
        if mx.music.get_busy():
            pos = mx.music.get_pos() // 1000
            self.progreso.set(pos)
            self.estado.after(1000, self.BarraDeProgreso)
    
    def cambioVolumen(self,valor):
        self.volumen = float(valor)/100
        mx.music.set_volume(self.volumen)
