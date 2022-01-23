import unittest
import pages
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



class TestPageSetup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://todo-list-login.firebaseapp.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        
    def test_landonpage(self):
        #check for title on landing page
        landing_page = pages.Landpage(self.driver)
        assert landing_page.check_title()
        
    #No test on this, login process
    def notfortest_login(self):
        driver = self.driver
        landing_page = pages.Landpage(driver)
        #start login process by pressing in sign in via git
        selectlogin = landing_page.findgitlogin()
        
        #switch process to pop up window
        window_before = self.driver.window_handles[0]
        window_after =self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        
        #insert login details here (insertuser = username) (insertpw = password)
        insertuser = landing_page.logintogit("INSERT USERNAME DETAILS HERE")
        insertpw = landing_page.logintogitpw("INSERT PASSWORD DETAILS HERE")
        landing_page.submitdetails()
        #returns to main window after pop up close
        self.driver.switch_to.window(window_before)
        
    def test_afterlogin(self):
        #initialise login
        TestPageSetup.notfortest_login(self)
        
        #Begin testing for adding tasks after logging in
        after_loginpg = pages.Afterlogin(self.driver)
        time.sleep(3)
        #Check labels on land page after login to assert login
        assert after_loginpg.check_label_aftlogin()
        
        #Insert value into text bar, select on add button
        after_loginpg.insert_value_inbar()
        
        #Logouts of account
        after_loginpg.select_logout()
        #check label after logout to assert if account has logged out.
        TestPageSetup.test_landonpage(self)
    
    def test_delitems(self):
        #initialise login
        TestPageSetup.notfortest_login(self)
        after_loginpg = pages.Afterlogin(self.driver)
        time.sleep(3)
        #deleting fifth item
        after_loginpg.delete_fifthitem()
        #log out after delete 5th item
        time.sleep(3)
        after_loginpg.select_logout()
        
    #Sleeps for 2 seconds before closing window after each individual test unit           
    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main()

