##Run unittests on SauceLabs

___________________

###With SauceLab:
- Run automated Python-based Selenium unit tests.
- review screenshots, vides and logs of test performance.


###Setup Test Environment:
- import example.py test
```
$ python -c "import urllib2; open('example.py', 'wb').write(urllib2.urlopen('http://saucelabs.com/examples/example.py').read().replace('_U_', '\"jayjaycody\"').replace('_K_', '\"cbb80a3c-3317-4cbf-885e-b108f3ef82b0\"'))"
```

- install dependencies
```
pip install selenium pytest pytest-xdist sauceclient
```

###Anatomy of a test
- setUp()
  - initializes the browser testing environment 
  - specifies the browser, version, and platform to test, 
- create a webdriver.Remote to run the tests remotely:

```python
        sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (USERNAME, ACCESS_KEY)
        )
```
- webdriver.Remote() - [from saucelab documentation](https://saucelabs.com/docs/onboarding)
	- The webdriver.Remote is a standard Selenium interface, so you can do anything that you could do with a local Selenium test. The only code specific to Sauce Labs was the URL that makes the test run using a browser on Sauce Labs' servers. 
	- Once connected to Sauce Labs, the test runs commands to remote-control a browser. This simple example test simply requests a page and makes a few simple assertions. It runs against several browsers simultaneously, to demonstrate parallelized testing, and reports its status to Sauce Labs when complete.

###Running Test - [from saucelab documentation](https://saucelabs.com/docs/onboarding)
- We recommend running tests in parallel using py.test. Since our example test runs in two browsers, lets run both at the same time with -n2:

```
$ py.test -n2 --boxed example.py
```