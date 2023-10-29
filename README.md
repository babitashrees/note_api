# note_api

This api enables authenticated user to:
- create notes
- retrieve all notes
- retrieve note by id
- update a note
- update completed status of a note
- delete a note by id

## Project Setup
### Prerequistite
Python must be already installed

### Steps
1. At the location of this project, create a virtual environment
```
python -m venv <env_name>
```
3. Activate the virtual environment
```
.\<env-name>\Scripts\activate
```
5. Install 'pytest' and 'requests'
```
-pip install pytest requests
```
7. Run the test file
```
# for simple test run
pytest

# to see details of test run 
pytest --verbose

# to run only smoke or regression test 
pytest -k smoke
 or 
pytest -k regression
```

## Additional Information
- Json file containing valid credential i.e.'credential.json' is not included, so that file has to be set up under 'params' folder before execution.
- The valid note-id would have to be modified accordingly since the valid note-id included is unique to the individual user.
- A html test report is included under 'test_reports' folder.
- An input field is only tested once. So if the specific input field is tested for different input data in another test cases, the current test case has only one valid data. The same input field is not tested for different input data again.
