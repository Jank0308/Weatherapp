import requests, json,tkinter as tk
base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "8eec4a33213199cae5d7a83f10410a0c"

if True:
    city_name = "hmsdfhgfd"
    complete_url = base_url+"appid="+api_key+"&q="+city_name

    response = requests.get(complete_url)
    x = response.json()

while x["cod"] == "404":
    city_name = input("Stadt Name:")
    complete_url = base_url+"appid="+api_key+"&q="+city_name

    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] == "404": print("\nSorry Stadt nicht Gefunden")
if x["cod"] != "404":
    y = x["main"]
    temp = y["temp"]
    press = y["pressure"]
    humid = y["humidity"]

    z = x["weather"]
    descrip = z[0]["description"]
    print("current Temp in C° = " +
          str(temp-273.15) +
          "\n\n pressure in hPa = " + 
          str(press) + 
          "\n\n humidity in % = " +
          str(humid) +
          "\n\n Weather = " + 
          str(descrip)          
          )
root = tk.Tk()
def Ausgabe():
    lab1 = tk.Label(root,text = "Temperatur in C° = " + str(int(temp-273.15)))
    lab2 = tk.Label(root,text = "momentaner Druck in hPa = " + str(press))
    lab3 = tk.Label(root,text = "Feuchtigkeit in % = " + str(humid))
    lab4 = tk.Label(root,text = "Himmel = " + str(descrip))
