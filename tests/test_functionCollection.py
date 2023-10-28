import requests
import json

baseurl = "https://practice.expandtesting.com/notes/api"

def load_expected_responses(filename):
    response_file = f"params/response/{filename}Res.json"
    with open(response_file, "r") as file:
        expected_responses = json.load(file)
    return expected_responses

def load_json_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def createNote(data, token):
    response = requests.post(f"{baseurl}/notes", json=data, headers = token)
    return response

def getNote(token):
    response = requests.get(f"{baseurl}/notes", headers = token)
    return response

def getNotebyid(id, token):
    response = requests.get(f"{baseurl}/notes/{id}", headers = token)
    return response

def updateNote(id, data, token):
    response = requests.put(f"{baseurl}/notes/{id}", json = data, headers = token)
    return response

def updateStatus(id, data, token):
    response = requests.patch(f"{baseurl}/notes/{id}", json = data, headers = token)
    return response