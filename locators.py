from selenium.webdriver.common.by import By


class Frontpageelements():
    login_label =(By.CSS_SELECTOR, "h1.login-head")
    gitlogin = (By.CSS_SELECTOR, "a.btn.btn-social.btn-github")
    git_username =(By.ID, "login_field")
    git_pw =(By.ID, "password")
    gitsubmit =(By.CSS_SELECTOR, "input[type='submit'][name='commit']")

class Afterloginelements():
    landing_label =(By.CLASS_NAME, "brownhill")
    item_add =(By.XPATH, "/html/body/ng-view/div/div[2]/div[1]/input")
    button_add =(By.XPATH, "/html/body/ng-view/div/div[2]/div[2]/button")
    logout_btn=(By.CSS_SELECTOR, "button.btn.btn-default")
    fifth_delbtn=(By.XPATH, "/html/body/ng-view/div/div[3]/div/ul/li[6]/div/div[2]/button")
    


