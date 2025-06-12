import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        notas = [
            float(entrada_contenido.get()),
            float(entrada_presentacion.get()),
            float(entrada_creatividad.get()),
            float(entrada_ortografia.get())
        ]
        if any(n < 0 or n > 10 for n in notas):
            raise ValueError
        promedio = sum(notas) / len(notas)
        resultado.config(text=f"Promedio final de {entrada_nombre.get()}: {promedio:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Las calificaciones deben ser números entre 0 y 10.")

ventana = tk.Tk()
ventana.title("Sistema de Rúbricas")
ventana.geometry("400x350")

tk.Label(ventana, text="Sistema de Evaluación por Rúbricas", font=("Arial", 14)).pack(pady=10)

tk.Label(ventana, text="Nombre del estudiante:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

tk.Label(ventana, text="Contenido (0-10):").pack()
entrada_contenido = tk.Entry(ventana)
entrada_contenido.pack(pady=5)

tk.Label(ventana, text="Presentación (0-10):").pack()
entrada_presentacion = tk.Entry(ventana)
entrada_presentacion.pack(pady=5)

tk.Label(ventana, text="Creatividad (0-10):").pack()
entrada_creatividad = tk.Entry(ventana)
entrada_creatividad.pack(pady=5)

tk.Label(ventana, text="Ortografía (0-10):").pack()
entrada_ortografia = tk.Entry(ventana)
entrada_ortografia.pack(pady=5)

tk.Button(ventana, text="Calcular promedio", command=calcular).pack(pady=10)

resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack()

ventana.mainloop()