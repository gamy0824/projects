from IPython.core.display import JSON
from typing import Text
from datetime import datetime
import requests


pixa_end_point = "https://pixe.la/v1/users"

para= {
    
    "token":"vampirelord",
    "username":"gamy08",
    "agreeTermsOfService":"yes",
    "notMinor": "yes"}

# create the account
# send = requests.post(url=pixa_end_point,json=para)
# print(send.text)

user = "gamy08"
pas = "vampirelord"

graph_end_point = f'https://pixe.la/v1/users/{user}/graphs'


para_grahp = {
    
    "id":"graph1",
    "name":"gamy_grahp",
    "unit":"minute",
    "type":"float",
    "color":"ajisai",

}

headers = {
    
    "X-USER-TOKEN":pas,
}

id="graph1"

increment = f"https://pixe.la/v1/users/{user}/graphs/{id}"

today = datetime.now()
today.strftime("%Y%m%d")


cantidad = input("introduce un numero ")
increment_para = {
          "date":today.strftime("%Y%m%d"),
          "quantity":cantidad,
}

post = requests.post(url=increment, json=increment_para,headers=headers)
print(post.text)


update_url =f"https://pixe.la/v1/users/{user}/graphs/{id}/20220804"


update_para = {
    
    "quantity":"100",
}

# Update the pixels 
# update = requests.put(url=update_url,json=update_para,headers=headers)
# print(update.text)


delete_url =f"https://pixe.la/v1/users/{user}/graphs/{id}/20220804"

# Delete the pixels
# delete = requests.delete(url=delete_url,headers=headers)
# print(delete.text)
