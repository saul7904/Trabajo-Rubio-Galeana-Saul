import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup

def obtener_clima_web():
    url = "https://www.pronosticoextendido.net/pronosticos/ahora/m%C3%A9xico/ixtapaluca/"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
    except:
        return "Error al conectar. Intenta más tarde."
    soup = BeautifulSoup(r.text, "html.parser")
    temp = soup.find(text=lambda t: t and "°" in t and t.strip().replace("°", "").isdigit())
    cond_h1 = soup.find_all("h1")
    condiciones = ""
    for h1 in cond_h1:
        if "El tiempo en Ixtapaluca" not in h1.text:
            p = h1.find_next("p")
            if p:
                condiciones = p.text.strip()
                break
    viento = soup.find(string=lambda t: t and "Viento" in t)
    humedad = soup.find(string=lambda t: t and "Humedad" in t)
    if not (temp and condiciones and viento and humedad):
        return "No se pudo extraer todos los datos."
    return (f"Clima actual en Ixtapaluca:\n"
            f"Temperatura: {temp.strip()}\n"
            f"{condiciones}\n"
            f"{viento.strip()}\n"
            f"{humedad.strip()}")

def mostrar_clima():
    respuesta = obtener_clima_web()
    area_chat.insert(tk.END, f"{respuesta}\n\n")
    area_chat.see(tk.END)

ventana = tk.Tk()
ventana.title("Clima en Ixtapaluca")
ventana.geometry("500x450")

area_chat = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, font=("Arial", 11))
area_chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

btn_clima = tk.Button(ventana, text="Mostrar Clima", font=("Arial", 11), command=mostrar_clima)
btn_clima.pack(padx=10, pady=(0, 10))

ventana.mainloop()