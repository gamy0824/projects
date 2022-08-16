from IPython.core.display import JSON
import requests
from datetime import datetime


user = "gamy08"

GENDER = "male"
WEIGHT_KG = 94
HEIGHT_CM = 172.72
AGE = 39

appid = "9a162b38"
appkey = "b9532dff98977d164aaf2530b61b31cf"

exercise_text = input("Tell me which exercises you did: ")


url1 = f"https://trackapi.nutritionix.com/v2/natural/exercise"


headers = {
    "x-app-id": appid,
    "x-app-key": appkey,
}


parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url= url1,json=parameters,headers=headers)
result = response.json()
print(result)

# url2 = "https://api.sheety.co/ffe24e401df98dda68f7323b4e5724ee/yoryiWorkouts/workouts"

# response1 = requests.get(url=url2)
# response1.raise_for_status()
# response2 = response1.json()


today = datetime.now()
today_date = today.strftime("%x")
now_time = today.strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

url3 = "https://api.sheety.co/ffe24e401df98dda68f7323b4e5724ee/yoryiWorkouts/workouts"
post = requests.post(url=url3, json=sheet_inputs )
print(post.text)

# print(response2)







