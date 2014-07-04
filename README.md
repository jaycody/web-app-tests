##Web App Tests
prototype test plan and automation scripts for random webapp

________________________

###Keys to a Success
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
    - Write test scripts (Selenium WebDriver)
    - Create reporting mechanism (pytest, unittests)
    - create command line tools for developers to use the tests
    - automate the regression tests with Jenkins / Saucelab automated regression tests
####Version 2 Features:
- Define and test the operational requirments (version 2 features)
    - eg. Performance, Stress and Volume


###Create Project Plan From Assessment
1. Test Plan
2. Method
3. Prototype
4. Feedback and Recommendations
5. Roadmap and Long Range
6. TimeLines
7. Build It

###Test Plan

###Method
- write test scripts - (Selenium Webdrivr, Python)
- create error reporting mechanism - (pytest, unittests)
- provide interface for developers - command line
- automate regression tesss (Jenkins, SauceLabs, Github)


[interactive sketching notation]:http://www.linowski.ca/downloads/InteractiveSketchingNotation_0.1.pdf
