import requests

RANDOM_USER_URL = "https://randomuser.me/api/?nat=br"

def fetch_random_user():
    response = requests.get(RANDOM_USER_URL)
    data = response.json()
    user = data["results"][0]

    return {
        "gender": user["gender"],
        "name": user["name"],
        "location": user["location"],
        "email": user["email"],
        "dob": user["dob"],
        "registered": user["registered"],
        "phone": user["phone"],
        "cell": user["cell"],
        "id_info": user["id"],
        "picture": user["picture"],
        "nat": user["nat"]
    }