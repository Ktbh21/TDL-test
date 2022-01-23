from locators import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class BasePage():
    
    def __init__(self, driver):
        self.driver = driver
        
        
class Landpage(BasePage):
    
    def check_title(self):
        #check page title on landing page, will return true if it matches assigned webtitle value
        webtitle = "To continue you will need to sign in first,"
        pagetitle = self.driver.find_element(*Frontpageelements.login_label)
        if webtitle == pagetitle.text:
            return True
        else:
            return False
        
    def findgitlogin(self):
        selectgit = self.driver.find_element(*Frontpageelements.gitlogin)
        selectgit.click()

    
    def logintogit(self,username):
        fillusername = WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located((Frontpageelements.git_username))
            )
        fillusername.clear()
        fillusername.send_keys(username)
        
    def logintogitpw(self,password):
        fillpw = WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located((Frontpageelements.git_pw))
            )
        fillpw.clear()
        fillpw.send_keys(password)
        
    def submitdetails(self):
        press_signin =WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located((Frontpageelements.gitsubmit))
            )
        press_signin.click()
        
        # ActionChains(self.driver).move_to_element(press_signin).click().perform()
    
class Afterlogin(BasePage):
    
    def check_label_aftlogin(self):
        landlab = "Todo Lists"
        aftloginlab = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((Afterloginelements.landing_label))
            )
        if landlab == aftloginlab.text:
            return True
        else:
            return False
        
    def insert_value_inbar(self):
        insvalbar = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((Afterloginelements.item_add))
            )
        addlist = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((Afterloginelements.button_add))
            )
    #loop adds 10 items to To do list
        for i in range(1, 11):
            insvalbar.clear()
            insvalbar.send_keys("{}".format(i))
            addlist.click()
    
    def select_logout(self):     
        logout = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((Afterloginelements.logout_btn))
            )
        ActionChains(self.driver).move_to_element(logout).click().perform()
    
    def delete_fifthitem(self):
        delfifth = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((Afterloginelements.fifth_delbtn))
            )
        i = 0
        while i != 4:
            ActionChains(self.driver).move_to_element(delfifth).click().perform()
            delfifth = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((Afterloginelements.fifth_delbtn))
            )
            print("clicked on delete {} times".format(i))
            i +=1
        ActionChains(self.driver).move_to_element(delfifth).click().perform()
        

        