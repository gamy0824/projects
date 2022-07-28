import requests
import pandas as pd

lat = 18.735693
log = -70.162651

location = {
    "lat":lat,
    "Ing":log,
    "formatted":0,    
}

r  = requests.get(url="https://api.sunrise-sunset.org/json",params=location)
r.raise_for_status()
data = r.json()
sunset = data["results"]["sunset"]
sunrise = data["results"]["sunrise"]
new_sunrise = sunrise.split("T")
print(new_sunrise)

