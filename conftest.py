import pytest
import requests
import tests.test_functionCollection as test

creden = test.load_json_data("params/credentials.json")
create = test.load_json_data("params/inputData/create.json")
id = test.load_json_data("params/inputData/getbyid.json")
update = test.load_json_data("params/inputData/update.json")
updateStat = test.load_json_data("params/inputData/updateStatus.json")

@pytest.fixture(scope="module", autouse=True)
def login():
    response = requests.post("https://practice.expandtesting.com/notes/api/users/login", json=creden)
    if response.status_code == 200:
        print("Login Successful!")
        reponsetext = response.json()
        token = reponsetext.get("data", {}).get("token") 
        accessToken = {
            "x-auth-token": f"{token}"
        }
    return accessToken

@pytest.fixture
def createNote(login):
    token = login
    responseStatus = [] 
    responseMessage = []
    for data in create:
        response = test.createNote(data, token)
        responseStatus.append(response.status_code)
        responseText = response.json()
        responseMessage.append(responseText.get("message", ""))
    return responseStatus, responseMessage

@pytest.fixture
def getNote(login):
    token = login
    response = test.getNote(token)
    responseStatus= response.status_code
    responseText = response.json()
    responseMessage = responseText.get("message", "")
    responseData = responseText.get("data", {})
    return responseStatus, responseMessage, responseData

@pytest.fixture
def getNotebyid(login):
    token = login
    responseStatus = [] 
    responseMessage = []
    for data in id:
        noteid = data["id"]
        response = test.getNotebyid(noteid, token)
        responseStatus.append(response.status_code)
        responseText = response.json()
        responseMessage.append(responseText.get("message", ""))
    return responseStatus, responseMessage

@pytest.fixture
def updateNote(login):
    token = login
    responseStatus = [] 
    responseMessage = []
    for data in id:
        noteid = data["id"]
    for data in update:
        response = test.updateNote(noteid, data, token)
        responseStatus.append(response.status_code)
        responseText = response.json()
        responseMessage.append(responseText.get("message", ""))
    return responseStatus, responseMessage

@pytest.fixture
def updateStatus(login):
    token = login
    responseStatus = [] 
    responseMessage = []
    noteid = id[2]["id"]
    for data in updateStat:
        response = test.updateStatus(noteid, data, token)
        responseStatus.append(response.status_code)
        responseText = response.json()
        responseMessage.append(responseText.get("message", ""))
    return responseStatus, responseMessage