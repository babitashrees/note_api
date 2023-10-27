import pytest
import json

with open("params/response/createRes.json", "r") as createRes_file:
    expected_createResponses = json.load(createRes_file)

with open("params/response/getRes.json", "r") as getRes_file:
    expected_getResponses = json.load(getRes_file)

@pytest.mark.smoke
def test_createNote(createNote):
    responseStatus, responseMessage = createNote
    for i, (actual_status, actual_message) in enumerate(zip(responseStatus, responseMessage)):
        expected_response = expected_createResponses[i]
        assert actual_status == expected_response["status"]       
        assert actual_message == expected_response["message"]
    print("create note passed !!")

@pytest.mark.smoke
def test_getNote(getNote):
    responseStatus, responseMessage = getNote
    expected_response = expected_getResponses
    assert responseStatus == expected_response["status"]       
    assert responseMessage in expected_response["message"]
    print("get all notes passed !!")

