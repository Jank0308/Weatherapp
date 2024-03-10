def ret_data(city):

    import requests
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "8eec4a33213199cae5d7a83f10410a0c"

    
    

    if True:
        city_name = city
        complete_url = base_url+"appid="+api_key+"&q="+city_name

        response = requests.get(complete_url)
        x = response.json()

    if x["cod"] == "404":
       data = 'Sorry,'+ city + ' not found\n Try things like bracets or similar'
       return data
       pass

    if x["cod"] != "404":
        y = x["main"]
        temp = y["temp"]
        press = y["pressure"]
        humid = y["humidity"]

        z = x["weather"]
        descrip = z[0]["description"]
        
        data = ("place:" + city +"\ncurrent Temp in C° = " +
              str(temp-273.15) +
              "\n\n pressure in hPa = " + 
              str(press) + 
              "\n\n humidity in % = " +
              str(humid) +
              "\n\n Weather = " + 
              str(descrip)          
              )


    
    return data
