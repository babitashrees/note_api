import requests

baseurl = "https://practice.expandtesting.com/notes/api"

def login(data):
    response = requests.post(f"{baseurl}/users/login", json=data)
    if response.status_code == 200:
        print("Login Successful!")
        reponsetext = response.json()
        token = reponsetext.get("data", {}).get("token") 
        accessToken = {
            "x-auth-token": f"{token}"
        }
    return accessToken

def createNote(data, token):
    response = requests.post(f"{baseurl}/notes", json=data, headers = token)
    return response

def getNote(token):
    response = requests.get(f"{baseurl}/notes", headers = token)
    return response
