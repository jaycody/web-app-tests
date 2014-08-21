##Healthy Communities Institute - Website Test Plan
>a test automation plan for HCI's web page:
[www.healthycommunitiesinstitute.com](https://healthycommunitiesinstitute.com)

________________________

###Test Plan Overview:
[1. Objectives](#1-objectives)  
[2. Required Steps](#2-required-steps)  
[3. Assessment Phase](#3-assessment-phase)    
[4. Scope](#4-scope)    
[5. Proposed Approach](#5-proposed-approach)    
[6. Method](#6-method)    
[7. Defect Management](#7-defect-managment)    
[8. Resources and Notes](#8-resources-and-notes)  


_________________________________

###1. Objectives
- Continuously verify and validate HCI webapp functionality according to specs and requirements. 
- Build and deploy a test automation framework capable of continuous verification and validation of the HCI webapp.

_________________________________

###2. Required Steps
1. **Elucidate app's existing workflow**  
    - what does it do?  
2. **Transform the workflow into test scripts**  
    - automate verification of what it supposed to do (Selenium WebDriver, Python)  
3. **Prioritize the maintenance and version-control of test scripts**
4. **Automate test run on checkin via github plugin**
    - now automate the execution of the automated tests (Jenkins, github, SauceLabs)
5. **Use the test results!**
    - pipe test output as an input to appropriate players

_________________________

###3. Assessment Phase
1. **Learn who's who.** [Automation Engineer]
    - introductions, roles, responsibilities
2. **Learn the workflow and generate a UI sketch** [Automation Engineer] 
    - use [interactive sketching notation] and Illustrator
3. **Define requirements for functional testing** [HCI] 
    - Can't test everything, so what are we most concerned with? 
    - create the input, determine the output, compare to expected 
4. **Determine what to do with test results?**   [HCI]
    - Who receives the auto-emailed failure notifications?  SMS?
    - Decision makers want timely reports!
5. **Determine who writes the scripts, who runs the sripts, and who's waiting for results**  [HCI]
6. **Identify process and next steps** [Automation Engineer]

#####Assessment for Version 2 of the automation project:
- Define and test the operational requirments (version 2 features)
    - eg. Performance, Stress and Volume

_____________________________

###4. Scope  
This test plan covers basic UI and DB functionality as would be required for general user scenarios within a wide variety of environments and platforms.

####**In-Scope:**
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

####**v.2:**
- UX/usability
- performance and load testing

___________________________________

###5. Proposed Approach for v.1
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

___________________________________



###6. Method
####Step 1. Build test suite prototype with [Selenium Builder]
- current location of test suite prototype ==> [se-builder-testSuite] 
- record and modify test cases
- organize test cases as suite
- execute test suite locally
- execute test suite remotely on multi platforms
- manage error reporting
- pro: 
    - rapid prototyping, extensive platform coverage
- con:
    - clumsy. lacks abstraction, won't scale

####Step 2. Create Python test scripts from prototype test suite
- current location of ported test cases ==> [unittests]
- from [Selenium Builder] port test cases to Python
- fix translation issues with [Selenium WebDriver] and [Python] caused by porting test cases
- expand [unittest] features
- modify test cases to run from command line

####Step 3. Modify Python test scripts to run multi-platform tests remotely
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

####Step 4. Incorporate Continuous Integration Testing
- objective:  trigger execution of test suite upon change to code base
- connect [Github] <-> [Jenkins] <-> [SauceLabs]
- [Travis] - continuous integration platform

####Step 5. Improve test script resilience
- make smart, resilient, robust test scripts 
- create code abstraction
- techniques:
    - [Page Object Model]
- provide a test interface for developers and staff

####Step 6. Feedback - Recommendations - Alternatives
this is not a final step - it's an ongoing process  

**Feedback:**  
- actively pursue it.  invite it.  assume it's non-optional  

**Recommendations:**    
- remain open to the outcome rather than attached to the process (regardless of who created it from scratch)  

**Alternatives:**   
- Review alternative test methodologies and frameworks  
- test automation tools change daily, act accordingly  
- build an evolvable framework  

**list of alternatives:**    
#####[Robot Framework]
- Robot Framework is a Python-based keyword-driven test automation framework with an easy-to-use tabular syntax for creating test cases. Its testing capabilities can be extended by test libraries implemented either with Python or Java. Users can also create new keywords from existing ones using the same simple syntax that is used for creating test cases.
- [Intro to Robot Framework](https://www.youtube.com/watch?v=CrkfmqFbJpU) - video from uTest
- Robot Framework, implemented with Selenium Library, allows for quick creation of keyword based Automation scripts
Implementation of a keyword library is simplified and allows for automation scripts that are human readable. Implemented correctly, users end up with executable documents that are automation scripts and documented requirements. Robot Framework includes several built in libraries and can be extended using python
- [RIDE] - the test data editor for Robot Framework test data
- acceptance testing framework
- **keyword** driven
- selenium plugins
- installation:
  - pip install robotframeworks
- good at separating test cases from the test code.
- simple test case
  - user can create an account and login.  ACTION: create valid user.  
- data drive the tests:
  - Test Cases:  passwordsTooLong..  passwordsTooShort
- Jenkins integration with Jenkins Plugins
- [robot + selenium video tutorials]
- rebot plugin aggregates all reporting feedback

#####[multi-mechanize] - performance test framework
- scripts written similar to Martin's padospeed.  
- only way to test scalalbitity and stability before your users do
- what does it provide?
  - report genration
  - graphs
  - aggregrates statistics
  - easily scalable
  - pure python
- setup the config.cfg file
  - run_time, rampup, results_ts_interval, progress_bar, xml_report
- performance trend feedback from JENKINS

#####lettuce
- python's version of Ruby's Cucumber
- Behavior Driven Development (BDD) done as Test Driven Development (TDD) in **Gherkin**
- uses *Gherkin* - "business readable, domain specific language"
```
Given I have the input foo
When I compute the bar of foo
Then I see the expected number bus
```



__________________________________


###7. Defect Management
- error reporting:
    - pytests
    - Dashboard on SauceLabs
    - triggered emails
    - In-office Alert System involving bright lights and loud sirens
         - [triggered when Raspberry Pi detects reported error]
- bug tracking
    - HCI's current system?
    - Asana
    - Jira 

_______________________________

###8. Resources and Notes
- [Page Object Model]
    - [Martin Fowler's article](http://martinfowler.com/bliki/PageObject.html)
        - A page object wraps an HTML page, or fragment, with an application-specific API, allowing you to manipulate page elements without digging around in the HTML.
    - [Page Objects on Selenium wiki](https://code.google.com/p/selenium/wiki/PageObjects)
- [Python Testing Fundamentals](https://www.youtube.com/watch?v=jTJHQ-zQMk4) - basics of unittest, assert, and doctest
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
[Automation Engineer]:http://linkedin.com/in/videoalchemy/
[HCI]:http://healthycommunitiesinstitute.com
[robot + selenium video tutorials]:http://robotframework.org/#documentation
[RIDE]:https://github.com/robotframework/RIDE/wiki
[multi-mechanize]:http://testutils.org/multi-mechanize/
[Travis]:https://travis-ci.org
