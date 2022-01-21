from tkinter import *
import requests

#c7540f01e06be89458b63ac94a9dfe16
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def mostrar_respuesta(clima):
    nombre_ciudad = clima["name"]
    temp = clima["main"]["temp"]
    desc = clima["weather"][0]["description"]
    # print(ciudad)
    # print(temp)
    # print(desc)
    ciudad["text"] = nombre_ciudad
    temperatura["text"] = temp
    descripcion["text"] = desc
    
def clima_JSON(ciudad):
   
    API_Key = "584cab7a392df8bc3ddaebea0fa97b98"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {"APPID" : API_Key, "q" : ciudad, "units" :"metric", "lang" : "es"}
    response = requests.get(URL, params = parametros)
    clima = response.json()

    mostrar_respuesta(clima)
       
ventana=Tk()
ventana.geometry("350x550")

texto_ciudad = Entry(ventana, font = ("Courier", 20, "normal"), justify="center")
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text =  "obtener clima", font = ("Courier", 20, "normal"), command = lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font = ("Courier", 20, "normal"))
ciudad.pack(padx = 20, pady = 20)

temperatura = Label(font = ("Courier", 50, "normal"))
temperatura.pack(padx = 10, pady = 10)

descripcion = Label(font = ("Courier", 20, "normal"))
descripcion.pack(padx = 10, pady = 10)

ventana.mainloop()