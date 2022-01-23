To Do list Challenge

System requirements installed for assessment:
*Note that script is not compiled
1. [Install](https://www.python.org/downloads/) Python  
2. PIP installation steps [here](https://phoenixnap.com/kb/install-pip-windows)
3. Alternatively , [Install](https://pip.pypa.io/en/stable/installation/) pip like this
    >On python environment
    `get-pip.py`
___
## To Do List test walkthrough
Test will cover the following items :
1. Navigation to Weblink
2. Checking Labels on landing page
3. Login via GitHub
4. Check Labels on page (After Login)
5. Insert 10 items to list
6. Remove last 5 items from list
7. Logouts after addition and removal of items
____

## Description of code/script used for assessment 
### Required and used 
**Imported modules on python**

``` Import and use unit test
import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
```
**Created files used/imported **
```
main.py (Main file for test)
pages.py (Test instructions based on related page)
locators.py (Access elements stored based on related pages)
```

**Description on Classes used**

`class TestPageSetup(unittest.TestCase):`
>Main class used to contain all test cases, setup/ tear down codes. 

**Functions/ codes needed to run test case**
``` 
def setUp(self):
```
This function contains start up instructions for the test session
Instructions needed to get user to test site. From getting the webpage, to logging in and selecting the options to test site.


``` 
def tearDown(self):
```
The function that contains termination instructions. Used for ending test sessions after every instance


```sh
if __name__ == "__main__":
    unittest.main()
```
Used for starting the unit test.

___

### Main .py file
**Functions/ codes that are the test cases**
*Run these code individually to test the scenarios*


```
def test_landonpage(self):
```
Test cases used for checking page title.
  
  
```
def notfortest_login(self):
```
Login function created for user to login. In this function Locate the 2 lines as descibed below and insert login details.

Insert (GITHUB) ONLY login details here.
`insertuser = landing_page.logintogit(INSERT USERNAME DETAILS HERE")`
`insertpw = landing_page.logintogitpw("INSERT PASSWORD DETAILS HERE")`

```
def test_afterlogin(self):
```
Test case use to check if test is on correct page once logged in.
Test will beign with running < def notfortest_login(self): > to login
Test will then check label for (To do list)
Test will then proceed to insert items into to do list
Test will finally logout once completed
```
 def test_delitems(self):
```
Test will beign with running < def notfortest_login(self): > to login
Test will then beign deleting the last 5 items
Test will then logout
___

### Pages .py file
**Pages setup along with test instruction for main file

```
class BasePage():
```
Parent page which initialises the driver

```
def __init__(self, driver):
    self.driver = driver
```

Class that contains instruction for before login actions
Class that contains instruction for login process
```
class Landpage(BasePage):
```

Class that contains instruction for after login actions
Class that contains instruction for majority of test case
Includes insert items, delete 
```
class Afterlogin(BasePage)::
```
___

### Locators .py file
**Locators setup along with test instruction for page file 
**Contains elements found on respective pages

```
class Frontpageelements():
```
Contains instructions to access elements on first page before any login action is done.

```
class Afterloginelements():
```
Contains instructions to access elements on page after any login action is done.

