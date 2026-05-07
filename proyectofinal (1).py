import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# COLORES
# -------------------------
FONDO_MORADO = "#4B0082"
MORADO_BRILLANTE = "#8A2BE2"
NEGRO = "#000000"
BLANCO = "#FFFFFF"

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():

    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("400x450")
    reg.resizable(False, False)

    # Fondo morado
    reg.configure(bg=FONDO_MORADO)

    # -------------------------
    # ETIQUETAS Y CAMPOS
    # -------------------------
    lbl_id = tk.Label(
        reg,
        text="ID del Producto:",
        font=("Arial", 12, "bold"),
        bg=FONDO_MORADO,
        fg=BLANCO
    )
    lbl_id.pack(pady=5)

    txt_id = tk.Entry(reg, font=("Arial", 12), width=30)
    txt_id.pack(pady=5)

    lbl_desc = tk.Label(
        reg,
        text="Descripción:",
        font=("Arial", 12, "bold"),
        bg=FONDO_MORADO,
        fg=BLANCO
    )
    lbl_desc.pack(pady=5)

    txt_desc = tk.Entry(reg, font=("Arial", 12), width=30)
    txt_desc.pack(pady=5)

    lbl_precio = tk.Label(
        reg,
        text="Precio:",
        font=("Arial", 12, "bold"),
        bg=FONDO_MORADO,
        fg=BLANCO
    )
    lbl_precio.pack(pady=5)

    txt_precio = tk.Entry(reg, font=("Arial", 12), width=30)
    txt_precio.pack(pady=5)

    lbl_categoria = tk.Label(
        reg,
        text="Categoría:",
        font=("Arial", 12, "bold"),
        bg=FONDO_MORADO,
        fg=BLANCO
    )
    lbl_categoria.pack(pady=5)

    txt_categoria = tk.Entry(reg, font=("Arial", 12), width=30)
    txt_categoria.pack(pady=5)

    # -------------------------
    # FUNCIÓN GUARDAR
    # -------------------------
    def guardar_producto():

        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        # Validaciones
        if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
            messagebox.showwarning(
                "Campos Vacíos",
                "Por favor complete todos los campos."
            )
            return

        # Validar precio
        try:
            float(precio)
        except:
            messagebox.showerror(
                "Error",
                "El precio debe ser un número."
            )
            return

        # Guardar archivo
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(BASE_DIR, "productos.txt")

        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{id_prod}|{descripcion}|{precio}|{categoria}\n"
            )

        messagebox.showinfo(
            "Guardado",
            "Producto registrado correctamente."
        )

        # Limpiar campos
        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

    # -------------------------
    # BOTÓN GUARDAR
    # -------------------------
    btn_guardar = tk.Button(
        reg,
        text="Guardar Producto",
        command=guardar_producto,
        font=("Arial", 12, "bold"),
        bg=NEGRO,
        fg=BLANCO,
        activebackground=MORADO_BRILLANTE,
        activeforeground=BLANCO,
        relief="flat",
        cursor="hand2",
        padx=10,
        pady=8
    )

    btn_guardar.pack(pady=20)


def abrir_registro_ventas():
    messagebox.showinfo(
        "Registro de Ventas",
        "Aquí irá el módulo de registro de ventas."
    )


def abrir_reportes():
    messagebox.showinfo(
        "Reportes",
        "Aquí irá el módulo de reportes."
    )


def abrir_acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0"
    )


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - proyectofinalcarolinaalejandro")
ventana.geometry("500x600")
ventana.resizable(False, False)

# Fondo principal morado
ventana.configure(bg=FONDO_MORADO)

# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    imagen = Image.open(
        os.path.join(BASE_DIR, "logo.png")
    )

    imagen = imagen.resize((250, 250))

    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg=FONDO_MORADO
    )

    lbl_logo.pack(pady=20)

except:
    lbl_sin_logo = tk.Label(
        ventana,
        text="(Aquí va el logo del sistema)",
        font=("Arial", 14, "bold"),
        fg=BLANCO,
        bg=FONDO_MORADO
    )

    lbl_sin_logo.pack(pady=40)

# -------------------------
# ESTILO DE BOTONES
# -------------------------
estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure(
    "Custom.TButton",
    font=("Arial", 12, "bold"),
    padding=10,
    foreground=BLANCO,
    background=NEGRO,
    borderwidth=0
)

# Color al pasar o seleccionar
estilo.map(
    "Custom.TButton",
    background=[
        ("active", MORADO_BRILLANTE),
        ("pressed", MORADO_BRILLANTE)
    ],
    foreground=[
        ("active", BLANCO),
        ("pressed", BLANCO)
    ]
)

# -------------------------
# BOTONES PRINCIPALES
# -------------------------
btn_reg_prod = ttk.Button(
    ventana,
    text="Registro de Productos",
    style="Custom.TButton",
    command=abrir_registro_productos
)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = ttk.Button(
    ventana,
    text="Registro de Ventas",
    style="Custom.TButton",
    command=abrir_registro_ventas
)
btn_reg_ventas.pack(pady=10)

btn_reportes = ttk.Button(
    ventana,
    text="Reportes",
    style="Custom.TButton",
    command=abrir_reportes
)
btn_reportes.pack(pady=10)

btn_acerca = ttk.Button(
    ventana,
    text="Acerca de",
    style="Custom.TButton",
    command=abrir_acerca_de
)
btn_acerca.pack(pady=10)

# -------------------------
# INICIO DEL SISTEMA
# -------------------------
ventana.mainloop()