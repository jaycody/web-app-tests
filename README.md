##Web App Test Automation
prototype test plan and automation scripts for random webapp

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
    - pipe test output as an input into appropriate team (analytics)

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
3. Prototype [github] - Selenium Builder, CI via Jenkins and Github
4. Feedback and Recommendations
5. Roadmap and Long Range
6. TimeLines
7. Build It

_______________________________

####3.1 The Test Plan
- {magik here}

####3.2 Methods
- test script prototypes: 
    - [Selenium Builder]
- test scripts
    - ([Selenium WebDriver] via [Python])
    - [Page Object Model]
    - possible alternative = [Robot Framework]
        - Robot Framework is a Python-based keyword-driven test automation framework with an easy-to-use tabular syntax for creating test cases. Its testing capabilities can be extended by test libraries implemented either with Python or Java. Users can also create new keywords from existing ones using the same simple syntax that is used for creating test cases.
- error reporting - ([pytest], [unittests], [SauceLabs])
- interface for developers - (command line)
- prototype automated regression testing [Selenium Builder], [Jenkins]
- automated regression tests ([Jenkins], [SauceLabs], [Github], [pytest_sauce])

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

[interactive sketching notation]:http://www.linowski.ca/downloads/InteractiveSketchingNotation_0.1.pdf
[Selenium WebDriver]:http://docs.seleniumhq.org/docs/03_webdriver.jsp
[Python]:http://selenium-python.readthedocs.org
[pytest]:https://pypi.python.org/pypi/pytest/2.5.2
[unittests]:https://docs.python.org/2/library/unittest.html
[SauceLabs]:https://saucelabs.com
[Jenkins]:https://docs.saucelabs.com/ci-integrations/jenkins/
[Github]:http://sauceio.com/index.php/2013/03/building-a-ci-system-using-selenium-builder-github-travis-and-sauce-labs/
[pytest_sauce]:https://pypi.python.org/pypi/pytest_sauce
[Selenium Builder]:http://sauceio.com/index.php/2013/03/building-a-ci-system-using-selenium-builder-github-travis-and-sauce-labs/
[Robot Framework]:https://github.com/robotframework/robotframework
[Page Object Model]:http://martinfowler.com/bliki/PageObject.html
