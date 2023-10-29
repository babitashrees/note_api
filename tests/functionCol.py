import requests
import json

baseurl = "https://practice.expandtesting.com/notes/api"

# function to load json files containing expected responses
def load_expected_responses(filename):
    response_file = f"params/response/{filename}Res.json"
    with open(response_file, "r") as file:
        expected_responses = json.load(file)
    return expected_responses

# function to load json files containing input data
def load_json_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

#These functions will send requests and return their response to the fixtures

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

def deleteNote(id, token):
    response = requests.delete(f"{baseurl}/notes/{id}", headers = token)
    return response