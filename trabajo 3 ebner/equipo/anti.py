import tkinter as tk
from tkinter import scrolledtext
import re, requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def dividir_texto(texto,tamaño=15):
    palabras=texto.split()
    return [' '.join(palabras[i:i+tamaño]) for i in range(0,len(palabras),tamaño)]

def contiene_cita_o_enlace(texto):
    return bool(re.search(r'(http|www|\“.*?\”|".*?"|\'.*?\')',texto))

def es_texto_probable_ia(texto):
    frases=["en conclusión","es importante mencionar","la inteligencia artificial es",
            "en la actualidad","por otro lado","como se puede observar"]
    reps=sum(texto.lower().count(f) for f in frases)
    lprom=sum(len(p) for p in texto.split())/max(1,len(texto.split()))
    return reps>=3 or lprom>6.5

def estimar_porcentaje_plagio(texto):
    frags=dividir_texto(texto)
    total=len(frags)
    reps=sum(1 for f in frags if len(set(f.split()))<len(f.split())*0.7)
    return min(int((reps/total)*100)+20,100)

def buscar_sitio_google(fragmento):
    r=requests.get("https://www.google.com/search",
                   headers={"User-Agent":"Mozilla/5.0"},
                   params={"q":fragmento})
    soup=BeautifulSoup(r.text,"html.parser")
    div=soup.find("div",class_="yuRUbf")
    if div and div.a:
        return div.a["href"]
    return "No encontrado"

def analizar():
    texto=entrada.get("1.0",tk.END).strip()
    if not texto:
        salida.config(text="❗ No se ingresó texto.")
        return
    if contiene_cita_o_enlace(texto):
        salida.config(text="✅ Contiene cita o enlace. No se considera plagio.")
        return
    pct=estimar_porcentaje_plagio(texto)
    probable_ia=es_texto_probable_ia(texto)
    sitio=""
    if pct>40:
        frag=dividir_texto(texto)[0]
        sitio=buscar_sitio_google(frag)
    resultado=f"📄 Posible plagio: {pct}%\n"
    resultado+=f"🤖 Texto {'PUEDE' if probable_ia else 'probablemente NO'} haber sido generado por IA.\n"
    if sitio:
        resultado+=f"🌐 Sitio encontrado: {sitio}"
    salida.config(text=resultado)

ventana=tk.Tk()
ventana.title("Detector Plagio + IA con Fuente")
tk.Label(ventana,text="Introduce texto:").pack()
entrada=scrolledtext.ScrolledText(ventana,width=80,height=20)
entrada.pack(padx=10,pady=10)
tk.Button(ventana,text="Analizar",command=analizar).pack(pady=10)
salida=tk.Label(ventana,text="",fg="blue",wraplength=700,justify="left")
salida.pack()
ventana.mainloop()