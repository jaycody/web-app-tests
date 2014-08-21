##Selenium unittests via Python
webapp test automation for homejoy

_______________

###Overview:
Test cases in this directory represent the simplest form of Selenium unittests save for those executed by the Selenium and Selenium Builder IDE.  Each test case started as a series of behaviors recorded by SE-Builder as a .json file (see wep-app-tests/se-builder-testSuite).  The test cases were exported from SE-Builder as .py files, updated, and stored here.

###Method:
- created with SE-Builder in Firefox
- exported to python unittest version
- updated .py file to run as a standalone test case.
- uses python unittest conventions

###Executing a test:
- execute test cases individually from command line
```
$ testPresenceOfContactPage.py
```
- generic error handling provided by unittest framework

Test Cases:
- testFunctionOfBookAppointmentButton.py
	- Verify the presence and functionality of the Book Appointment Button
- testPresenceOfContactInfoPage.py
	- verify presence of client's contact info page
- testPresenceOfContact[Us]Page.py
	- verify presence of Homejoy's "Contact Us" page

