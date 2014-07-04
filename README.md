##Web App Test Automation
prototype test plan and automation scripts for random webapp

________________________

###Project Overview
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

###Assessment Phase for the new Automation Engineer
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

###Create Project Plan From Assessment
1. Test Plan
2. Method
3. Prototype [github] - Selenium Builder, CI via Jenkins and Github
4. Feedback and Recommendations
5. Roadmap and Long Range
6. TimeLines
7. Build It

###Test Plan
- {magik here}

###Method
- test scripts - ([Selenium WebDriver], [Python])
- error reporting - ([pytest], [unittests], [SauceLabs])
- interface for developers - (command line)
- automated regression tests ([Jenkins], [SauceLabs], [Github], [pytest_sauce])


[interactive sketching notation]:http://www.linowski.ca/downloads/InteractiveSketchingNotation_0.1.pdf
[Selenium WebDriver]:http://docs.seleniumhq.org/docs/03_webdriver.jsp
[Python]:http://selenium-python.readthedocs.org
[pytest]:https://pypi.python.org/pypi/pytest/2.5.2
[unittests]:https://docs.python.org/2/library/unittest.html
[SauceLabs]:https://saucelabs.com
[Jenkins]:https://docs.saucelabs.com/ci-integrations/jenkins/
[Github]:http://sauceio.com/index.php/2013/03/building-a-ci-system-using-selenium-builder-github-travis-and-sauce-labs/
[pytest_sauce]:https://pypi.python.org/pypi/pytest_sauce