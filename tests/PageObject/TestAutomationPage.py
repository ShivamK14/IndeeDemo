from selenium.webdriver.common.by import By

# we have mplemented PageObject Pattern for locatar selection
# here is POM for TestAutomationCard


class TestAutomationCard:
    def __init__(self,driver):
        self.driver = driver
        


    Details = (By.ID,'detailsSection')
    # self.driver.find_element(By.ID,'detailsSection').click()

    Video = (By.ID,'videosSection')
    #self.driver.find_element(By.ID,'videosSection').click()

    FirstVideoLocator = (By.ID,'vid-01j912gbvdnr5er79gqeb8k30w')
    # self.driver.find_element(By.ID,'vid-01j912gbvdnr5er79gqeb8k30w')

    PlayIconLocator = (By.CLASS_NAME,'icon-width-gen')
    #  video.find_element(By.CLASS_NAME,'icon-width-gen').click()


    def DetailsTab(self):
        return self.driver.find_element(*TestAutomationCard.Details)
    

    def VideoTab(self):
        return self.driver.find_element(*TestAutomationCard.Video)
    

    def FirstVideo(self):
        return self.driver.find_element(*TestAutomationCard.FirstVideoLocator)
    
    def PlayIcon(self):
        play = self.driver.find_element(*TestAutomationCard.FirstVideoLocator)
        return play.find_element(*TestAutomationCard.PlayIconLocator)    
    
