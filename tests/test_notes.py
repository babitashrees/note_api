import pytest
import tests.test_functionCollection as test

expected_createResponses = test.load_expected_responses("create")
expected_getResponses = test.load_expected_responses("get")
expected_getbyidResponses = test.load_expected_responses("getbyid")
expected_updateResponses = test.load_expected_responses("update")
expected_updateStatusResponses = test.load_expected_responses("updateStatus")

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
    responseStatus, responseMessage, response = getNote
    expected_response = expected_getResponses
    assert responseStatus == expected_response["status"]       
    assert responseMessage in expected_response["message"]
    print("get all notes passed !!")

@pytest.mark.smoke
def test_getNotebyid(getNotebyid):
    responseStatus, responseMessage = getNotebyid
    for i, (actual_status, actual_message) in enumerate(zip(responseStatus, responseMessage)):
        expected_response = expected_getbyidResponses[i]
        assert actual_status == expected_response["status"]       
        assert actual_message == expected_response["message"]
    print("get note by id passed !!")

@pytest.mark.regression
def test_updateNote(updateNote):
    responseStatus, responseMessage = updateNote
    for i, (actual_status, actual_message) in enumerate(zip(responseStatus, responseMessage)):
        expected_response = expected_updateResponses[i]
        assert actual_status == expected_response["status"]      
        assert actual_message == expected_response["message"]
    print("update note passed !!")

@pytest.mark.regression
def test_updateStatus(updateStatus):
    responseStatus, responseMessage = updateStatus
    for i, (actual_status, actual_message) in enumerate(zip(responseStatus, responseMessage)):
        expected_response = expected_updateStatusResponses[i]
        assert actual_status == expected_response["status"]      
        assert actual_message == expected_response["message"]
    print("update status passed !!")

