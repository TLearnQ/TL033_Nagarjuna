import requests

def create_user_and_get_id_length():
    url = "https://reqres.in/api/users"
    
    headers = {
        "Authorization": "Bearer reqres-token",
        "Content-Type": "application/json"
    }
    
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    
    user_id = data["id"]
    print(len(user_id))

create_user_and_get_id_length()
