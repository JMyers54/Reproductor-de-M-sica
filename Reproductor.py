import tkinter as tk
from tkinter import *
from Tooltip import Tooltip
from funciones import Funciones
import pygame.mixer as mx
import tkinter.ttk as ttk
from mutagen.mp3 import MP3
from tkinter import messagebox


class Reproductor():
    def __init__(self):
        mx.init(frequency=44100)

        self.ventana = tk.Tk()
        self.ventana.title("🎧Reproductor MP3 ")
        self.ventana.config(width=500, height=220, bg="#1e1e2f")
        self.ventana.resizable(0,0)

        """el funcionamiento del boton Resume y stop estan en viceverza
        por lo tanto se decidio modificar el logo de ambos para q el usuario no se confudiera"""
        self.iconoPlay = tk.PhotoImage(file=r"Reproductor-de-M-sica\icons\control_play_blue.png")
        self.iconoPausa = tk.PhotoImage(file=r"Reproductor-de-M-sica\icons\control_pause_blue.png")
        self.iconoStop = tk.PhotoImage(file=r"Reproductor-de-M-sica\icons\control_end_blue.png")
        self.iconoResume = tk.PhotoImage(file=r"Reproductor-de-M-sica\icons\control_stop_blue.png")
        self.iconoCarpeta = tk.PhotoImage(file=r"Reproductor-de-M-sica\icons\folder.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Reproductor-de-M-sica\icons/help.png")

        self.estado = tk.Label(self.ventana, text="Cargando...", font=("Arial", 10, "bold"), fg="white", bg="#1e1e2f")
        self.estado.place(relx=0.5, rely=0.38, anchor="center")
        
        self.btnAyuda = tk.Button(self.ventana, image=self.iconoAyuda, command=self.mostrar_ayuda,bg="#1e1e2f")
        self.btnAyuda.place(relx=0.93, rely=0.0, x=-20, y=10, width=35, height=35)
        Tooltip(self.btnAyuda,"Precione para abrir ayuda")
        
        self.btnPlay = tk.Button(self.ventana, image=self.iconoPlay,bg="#1e1e2f")
        self.btnPlay.place(relx=0.44, rely=0.8, x=10, width=35, height=35)
        Tooltip(self.btnPlay, "Presione para reproducir la canción")

        self.btnPausa = tk.Button(self.ventana, image=self.iconoPausa, state="disabled", bg="#1e1e2f")
        self.btnPausa.place(relx=0.44, rely=0.8, x=-35, width=35, height=35)
        Tooltip(self.btnPausa, "Presione para pausar la reproducción")

        self.btnStop = tk.Button(self.ventana, image=self.iconoStop, state="disabled", bg="#1e1e2f")
        self.btnStop.place(relx=0.44, rely=0.8, x=-80, width=35, height=35)
        Tooltip(self.btnStop, "Presione para pasar a la siguiente canción")

        self.btnResume = tk.Button(self.ventana, image=self.iconoResume, state="disabled", bg="#1e1e2f")
        self.btnResume.place(relx=0.44, rely=0.8, x=55, width=35, height=35)
        Tooltip(self.btnResume, "Presione para detener la reproducción")

        self.btnMp3 = tk.Button(self.ventana, image=self.iconoCarpeta, state="disabled", bg="#1e1e2f")
        self.btnMp3.place(relx=0.53, rely=0.8, x=55, width=35, height=35)
        Tooltip(self.btnMp3, "importar canción")

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TScale",
        background="#1e1e2f",
        troughcolor="#1e1e2f",
        bordercolor="#1e1e2f",
        lightcolor="#1e1e2f",
        darkcolor="#1e1e2f",
        sliderthickness=12,
        sliderlength=10
)

        self.progreso = ttk.Scale(self.ventana, from_=0, to=100, orient="horizontal", length=450, style="TScale")
        self.progreso.place(relx=0.5, rely=0.68, anchor="center")

        self.lblDuracion = tk.Label(self.ventana, text="00:00", font=("Arial", 12), fg="white", bg="#1e1e2f")
        self.lblDuracion.place(relx=0.9, rely=0.47)

        self.acciones = Funciones(self.estado, self.btnPausa, self.btnStop, self.btnResume, self.btnPlay, self.progreso, self.lblDuracion)

        self.volumen = ttk.Scale(self.ventana, from_=0, to=100, orient="horizontal",  command=self.acciones.cambioVolumen)
        self.volumen.set(50)
        self.volumen.place(x=25 , y=180,relwidth=0.2)
        Tooltip(self.volumen, "barra de volumen izq -, der +")


        self.btnPlay.bind("<Button-1>", self.acciones.play)
        self.btnPausa.bind("<Button-1>", self.acciones.pausa)
        self.btnStop.bind("<Button-1>", self.acciones.stop)
        self.btnResume.bind("<Button-1>", self.acciones.reproducirSiguienteCanción)
        self.btnMp3.bind("<Button-1>", self.acciones.carpeta)

        #atajos
        self.ventana.bind("<a>", self.acciones.play)
        self.ventana.bind("<space>", self.acciones.pausa)
        self.ventana.bind("<s>", self.acciones.stop)
        self.ventana.bind("<d>", self.acciones.reproducirSiguienteCanción)
        self.ventana.bind("<f>", self.acciones.carpeta)
        
        self.ventana.mainloop()

    def mostrar_ayuda(self):
        mensaje = (
        "   🎵 Bienvenido al Reproductor de Música 🎵\n\n"
        "- 📂 Importar canción: Selecciona un archivo MP3 desde tu equipo.\n"
        "- ▶️ Reproducir: Inicia la reproducción de la canción seleccionada.\n"
        "- ⏸️ Pausar: Detiene temporalmente la reproducción.\n"
        "- 🔁 Reanudar: Continua la canción desde donde se pausó.\n"
        "- ⏹️ Detener: Finaliza completamente la reproducción.\n"
        "- 🎚️ Barra de progreso: Muestra el avance de la canción.\n\n"
        "Asegúrate de importar una canción antes de intentar reproducirla.\n"
        "¡Disfruta tu música! 🎧"
    )
        messagebox.showinfo("Ayuda", mensaje)
