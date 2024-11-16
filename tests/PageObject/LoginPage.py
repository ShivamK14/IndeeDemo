from selenium.webdriver.common.by import By
from PageObject import HomePage


# we have mplemented PageObject Pattern for locatar selection
# here is POM for Login



class Login:
    def __init__(self,driver):
        self.driver = driver
    
    code = (By.ID,"access-code")
    SigninButton = (By.ID,"sign-in-button")
    # self.driver.find_element(By.ID,"access-code").send_keys(BaseClass.pin)
    # self.driver.find_element(By.ID,"sign-in-button").click()
    
   

    def EnterCode(self):
        return self.driver.find_element(*Login.code)
    
    def ClickSubmit(self):
        self.driver.find_element(*Login.SigninButton).click()
        Home = HomePage.HomePage(self.driver)
        return Home