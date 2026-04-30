import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
   messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
   messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
   messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
   messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - proyectofinalcarolinaalejandro")
ventana.geometry("500x600")
ventana.resizable(False, False)

# Fondo que combina con morado
ventana.configure(bg="#2c003e")  # morado muy oscuro

# -------------------------
# LOGO
# -------------------------
try:
   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   imagen = Image.open(os.path.join(BASE_DIR,"logo.png"))
   imagen = imagen.resize((250, 250))
   img_logo = ImageTk.PhotoImage(imagen)

   lbl_logo = tk.Label(ventana, image=img_logo, bg="#2c003e")
   lbl_logo.pack(pady=20)
except:
   lbl_sin_logo = tk.Label(
       ventana,
       text="(Aquí va el logo del sistema)",
       font=("Arial", 14),
       fg="white",
       bg="#2c003e"
   )
   lbl_sin_logo.pack(pady=40)

# -------------------------
# ESTILO DE BOTONES
# -------------------------
estilo = ttk.Style()
estilo.theme_use("default")

estilo.configure(
    "Custom.TButton",
    font=("Arial", 12),
    padding=10,
    foreground="white",
    background="#4b0082",  # morado oscuro
    borderwidth=0
)

# Simulación de “brillo” al pasar el mouse
estilo.map(
    "Custom.TButton",
    background=[("active", "#6a0dad")],  # morado más claro al pasar el mouse
    foreground=[("active", "white")]
)

# -------------------------
# BOTONES
# -------------------------
btn_reg_prod = ttk.Button(ventana, text="Registro de Productos", style="Custom.TButton", command=abrir_registro_productos)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = ttk.Button(ventana, text="Registro de Ventas", style="Custom.TButton", command=abrir_registro_ventas)
btn_reg_ventas.pack(pady=10)

btn_reportes = ttk.Button(ventana, text="Reportes", style="Custom.TButton", command=abrir_reportes)
btn_reportes.pack(pady=10)

btn_acerca = ttk.Button(ventana, text="Acerca de", style="Custom.TButton", command=abrir_acerca_de)
btn_acerca.pack(pady=10)

# -------------------------
# INICIO
# -------------------------
ventana.mainloop()