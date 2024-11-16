from selenium.webdriver.common.by import By


# we have mplemented PageObject Pattern for locatar selection
# here is POM for Homepage

class HomePage:

    
    def __init__(self,driver):   # initialise Driver
        self.driver = driver


    SidebarLocator = (By.ID,"SideBar")

    TestCard = (By.ID,"indee-title-card-prj-01j912ej0rs3wwadvadhavpasx")

    SigoutLocator = (By.XPATH,"//a[@id='signOutSideBar']")

    def Card(self):  
        return self.driver.find_element(*HomePage.TestCard)
    
    def Sidebar(self):
         return self.driver.find_element(*HomePage.SidebarLocator)
    
    def Signout(self):
         return self.driver.find_element(*HomePage.SigoutLocator)
    
