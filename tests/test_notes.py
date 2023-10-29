import pytest
import tests.functionCol as test

# Import the json files which contain the expected responses for different test cases
expected_createResponses = test.load_expected_responses("create")
expected_getResponses = test.load_expected_responses("get")
expected_getbyidResponses = test.load_expected_responses("getbyid")
expected_updateResponses = test.load_expected_responses("update")
expected_updateStatusResponses = test.load_expected_responses("updateStatus")
expected_deleteResponses = test.load_expected_responses("delete")

#This test case will test 'create note' function for both valid and invalid data ( TC_01 , TC_02 )
@pytest.mark.smoke
def test_createNote(createNote):
    responseStatus, responseMessage = createNote
    for i, (actual_status, actual_message) in enumerate(zip(responseStatus, responseMessage)):
        expected_response = expected_createResponses[i]
        assert actual_status == expected_response["status"]       
        assert actual_message == expected_response["message"]

#This test case will test 'get all notes' function for valid auth token ( TC_03 )
@pytest.mark.regression
def test_getNote(getNote):
    responseStatus, responseMessage = getNote
    expected_response = expected_getResponses
    assert responseStatus == expected_response["status"]       
    assert responseMessage in expected_response["message"]

#This test case will test 'get note by id' function for both valid and invalid data ( TC_04 , TC_05 )
@pytest.mark.regression
def test_getNotebyid(getNotebyid):
    responseStatus, responseMessage = getNotebyid
    for i, (actual_status, actual_message) in enumerate(zip(responseStatus, responseMessage)):
        expected_response = expected_getbyidResponses[i]
        assert actual_status == expected_response["status"]       
        assert actual_message == expected_response["message"]

#This test case will test 'update note' function for both valid and invalid data ( TC_06 , TC_07 )
@pytest.mark.regression
def test_updateNote(updateNote):
    responseStatus, responseMessage = updateNote
    for i, (actual_status, actual_message) in enumerate(zip(responseStatus, responseMessage)):
        expected_response = expected_updateResponses[i]
        assert actual_status == expected_response["status"]      
        assert actual_message == expected_response["message"]

#This test case will test 'update completed status' function for valid data ( TC_08 )
@pytest.mark.regression
def test_updateStatus(updateStatus):
    responseStatus, responseMessage = updateStatus
    for i, (actual_status, actual_message) in enumerate(zip(responseStatus, responseMessage)):
        expected_response = expected_updateStatusResponses[i]
        assert actual_status == expected_response["status"]      
        assert actual_message == expected_response["message"]

#This test case will test 'delete note' function for both valid and invalid data ( TC_09 , TC_10 )
@pytest.mark.regression
def test_deleteNote(deleteNote):
    responseStatus, responseMessage = deleteNote
    for i, (actual_status, actual_message) in enumerate(zip(responseStatus, responseMessage)):
        expected_response = expected_deleteResponses[i]
        assert actual_status == expected_response["status"]      
        assert actual_message == expected_response["message"]