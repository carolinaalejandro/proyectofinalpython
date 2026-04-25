# programa Python en repositorio mejorado
import tkinter as tk
from tkinter import font

ventana = tk.Tk()
ventana.title("Programa para subir a repositorio")
ventana.geometry("500x300")  # Hacemos la ventana un poco más grande

# Configurar una fuente grande y llamativa
fuente_grande = ("Helvetica", 16, "bold")  # Tipo, tamaño, estilo

# Crear etiqueta con colores y tipografía mejorada
etiqueta = tk.Label(
    ventana,
    text="Este programa es de Carolina y Alejandro",
    font=fuente_grande,
    fg="white",        # Color de texto
    bg="purple",        # Color de fondo de la etiqueta
    padx=10, pady=10    # Espacio interno
)
etiqueta.pack(pady=30, padx=20, fill="both")  # Ajusta tamaño y espacio

# Otra etiqueta opcional para subtítulo o avance
subtitulo = tk.Label(
    ventana,
    text="Avances al 24 de abril del 2026",
    font=("Arial", 12, "italic"),
    fg="yellow",
    bg="black",
    padx=5, pady=5
)
subtitulo.pack(pady=10, padx=20, fill="x")

ventana.mainloop()