import pytest
import json
import tests.test_functionCollection as test

with open("params/credentials.json", "r") as creden_file:
    creden = json.load(creden_file)

with open("params/inputData/create.json", "r") as create_file:
    create = json.load(create_file)

@pytest.fixture
def createNote():
    token = test.login(creden)
    responseStatus = [] 
    responseMessage = []
    for data in create:
        response = test.createNote(data, token)
        responseStatus.append(response.status_code)
        responseText = response.json()
        responseMessage.append(responseText.get("message", ""))
    return responseStatus, responseMessage

@pytest.fixture
def getNote():
    token = test.login(creden)
    response = test.getNote(token)
    responseStatus= response.status_code
    responseText = response.json()
    responseMessage = responseText.get("message", "")
    return responseStatus, responseMessage