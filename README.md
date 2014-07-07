##Web App Test Automation
test plan, test cases, and automation strategies for Homejoy [prototype]

________________________

###Part 1:  Project Overview
1. Elucidate app's existing worklow  
    - what does it do?  
2. Transform the workflow into test scripts  
    - automate verification of what it supposed to do (Selenium WebDriver, Python)  
3. Regard test scripts as software worthy of maintainence and version-control
    - hey!  this is legitimate software devlopment
4. Automate regression testing based on changes to code base.
    - now automate the execution of the automated tests (Jenkins, github, SauceLabs)
5. Use the test results!
    - pipe test output as an input to appropriate players

_________________________

###Part 2:  Assessment Phase for the new Automation Engineer
1. Learn who's who.
    - introductions, roles, responsibilties
2. Learn the workflow and generate a UI sketch 
    - use [interactive sketching notation] and Illustrator
3. Define requirements for fucntional testing
    - Can't test everything, so what are we most concerned with? 
    - create the input, determine the output, compare to expected 
4. Determine what to do with test results?  Who receives the auto emails upon failure?  Texts?
    - Decision makers want timely reports!
5. Determine who writes the scripts, who runs the sripts, and who's waiting for results
6. Identify process and next steps

####Assessment for Version 2:
- Define and test the operational requirments (version 2 features)
    - eg. Performance, Stress and Volume

_____________________________

###Part 3:  Project Plan
1. Test Plan
2. Methods
3. Feedback and Recommendations
4. Roadmap and Long Range
5. TimeLines
6. Build It

_______________________________

###3.1 The Test Plan
####3.1.1 Objective
Continuously verify and validate that the Homejoy webapp functions according to specifications and requirements.
#####3.1.2 Scope  
This test plan covers basic UI and DB functionality as would be required for general user scenarios within a wide variety of environments and platforms.

#####**In-Scope:**
- **Platforms and Environments**
    - **MOBILE:**
        - All major mobile browsers for current and recent versions iOS and Android
    - **Desktop:**
        - All major browsers for all current and recent versions of Mac OS and Windows 
    
- **Features covered in this test plan**
    - Page Load
    - Login
    - Create New User Account
    - Setup Appointment
    - Cancel Appointment
    - Change Appointment Date
    - Add Service to Existing Appointment
    - Remove Service from Existing Appointment

#####**Out-of-Scope:**
- UX / usability / layout
- performance and load testing

####3.1.3 Approach
A Selenium-based multi-platform test automation suite written in Python and executed on [SauceLabs] test servers  
**Components:**  
- [Selenium Builder]
- [Selenium WebDriver]
- [Python]
- [SauceLabs]
- [unittest]
- [pytest]
- [Jenkins]
- [Github]



####3.1.4 Defect Management
- error reporting:
    - pytests
    - Dashboard on SauceLabs
    - triggered emails
    - In-office Alert System involving bright lights and loud sirens
         - [triggered when Raspberry Pi detects reported error]
- bug tracking
    - Homejoy's current system?
    - Asana
    - Jira 

__________________________

###3.2 Method
-  Step 1. Build test suite prototype with [Selenium Builder]
    - [se-builder-testSuite] - current location of test suite prototype
    - record and modify test cases
    - organize test cases as suite
    - execute test suite locally
    - execute test suite remotely on multi platforms
    - manage error reporting
    - pro: 
        - rapid prototyping, extensive platform coverage
    - con:
        - clumsy. lacks abstraction, won't scale
- Step 2. Create Python test scripts from prototype test suite
    - [unittests] - location of ported test cases
    - from [Selenium Builder] port test cases to Python
    - fix translation issues with [Selenium WebDriver] and [Python] caused by porting test cases
    - expand [unittest] features
    - modify test cases to run from command line
- Step 3. Modify Python test scripts to run multi-platform tests remotely
    - to run test cases on remote servers, add:
    ```
    webdriver.Remote()
    ```
    - update setUp() to extend test case testing environment by specifying browsers, versions and platform
    - add SauceLab account login for access to remote test servers
    - improve error reporting.  How?  Switch test framework from **unittest** to **[pytest]**
    - why use **[pytest]**
        - improved reporting
        - run test cases as a single test suite
        - test in parallel on multiple platforms
        - executing parallel tests from command line:
        ```
        $ py.test -n2 --boxed example.py
        ```
        - Example pytest response from parallel tests
        ```
            ============================== test session starts ==============================
            platform darwin -- Python 2.7.5 -- pytest-2.5.1
            plugins: xdist
            gw0 [2] / gw1 [2]
            scheduling tests via LoadScheduling
            ..
            =========================== 2 passed in 17.30 seconds ===========================
        ```
        - investigate [pytest_sauce]
- Step 4. Incorporate Continuous Integration Testing
    - objective:  trigger execution of test suite upon change to code base
    - connect [Github] <-> [Jenkins] <-> [SauceLabs]
    - Travis?
- Step 5. Improve test script resilience
    - make smart, resilient, robust test scripts 
    - create code abstraction
    - techniques:
        - [Page Object Model]
    - provide a test interface for developers and staff
- Step 6. Review alternative methodologies
    - test automation tools change daily, act accordingly
    - build an evolvable framework
    - **list of possible alternative**
        - [Robot Framework]
            - Robot Framework is a Python-based keyword-driven test automation framework with an easy-to-use tabular syntax for creating test cases. Its testing capabilities can be extended by test libraries implemented either with Python or Java. Users can also create new keywords from existing ones using the same simple syntax that is used for creating test cases.


_______________________________

###Resources and Notes
- [Page Object Model]
    - [Martin Fowler's article](http://martinfowler.com/bliki/PageObject.html)
        - A page object wraps an HTML page, or fragment, with an application-specific API, allowing you to manipulate page elements without digging around in the HTML.
    - [Page Objects on Selenium wiki](https://code.google.com/p/selenium/wiki/PageObjects)
- [unittests] - Unit Testing Framework
    - test fixture - represents prep needed to perform one or more tests
    - test case - smallest unit of testing
    - test suite - implmented with TestSuite class
    - test runner - executes the test and provides the feedback
    - to list all command line options:
```
python -m unittest -h
```
- [Python Testing Fundamentals](https://www.youtube.com/watch?v=jTJHQ-zQMk4) - basics of unittest, assert, and doctest
- [Intro to Robot Framework](https://www.youtube.com/watch?v=CrkfmqFbJpU) - video from uTest
    - Robot Framework, implemented with Selenium Library, allows for quick creation of keyword based Automation scripts
Implementation of a keyword library is simplified and allows for automation scripts that are human readable. Implemented correctly, users end up with executable documents that are automation scripts and documented requirements. Robot Framework includes several built in libraries and can be extended using python
- [Building a CI System Using SE-Builder Github, Travis and SauceLabs](http://sauceio.com/index.php/2013/03/building-a-ci-system-using-selenium-builder-github-travis-and-sauce-labs/)
    - The great thing about this setup is that if you put your site code and your tests into the same GitHub repository, then whenever you update the site code, and whenever you update the tests, Travis will rerun your Selenium tests on Sauce OnDemand – and then send you an email about whether or not they still work!
- [pytest usage and examples](http://pytest.org/latest/example/index.html#examples)

_______________________________

[se-builder-testSuite]:https://github.com/jayjaycody/web-app-tests/tree/master/se-builder-testSuite
[interactive sketching notation]:http://www.linowski.ca/downloads/InteractiveSketchingNotation_0.1.pdf
[Selenium WebDriver]:http://docs.seleniumhq.org/docs/03_webdriver.jsp
[Python]:http://selenium-python.readthedocs.org
[pytest]:https://pypi.python.org/pypi/pytest/2.5.2
[unittest]:https://docs.python.org/2/library/unittest.html
[SauceLabs]:https://saucelabs.com
[Jenkins]:https://docs.saucelabs.com/ci-integrations/jenkins/
[Github]:http://sauceio.com/index.php/2013/03/building-a-ci-system-using-selenium-builder-github-travis-and-sauce-labs/
[pytest_sauce]:https://pypi.python.org/pypi/pytest_sauce
[Selenium Builder]:http://sauceio.com/index.php/2013/03/building-a-ci-system-using-selenium-builder-github-travis-and-sauce-labs/
[Robot Framework]:https://github.com/robotframework/robotframework
[Page Object Model]:http://martinfowler.com/bliki/PageObject.html
[unittests]:https://github.com/jayjaycody/web-app-tests/tree/master/unittests