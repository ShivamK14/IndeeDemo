import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PageObject import LoginPage,HomePage,TestAutomationPage,VideoPlayer


# this is the main pyhon file Make sure to install Pytest and selenium

# here is main class that will run out all test 
@pytest.mark.usefixtures("setup")
class Test_indee():


    def test_signin(self,setup):   # this function is to login 
        
        self.driver.implicitly_wait(10)       # implement dynamic wait using Selenium’s WebDriverWait implicit wait to the driver which waits till 10 seconds
        login = LoginPage.Login(self.driver)
        login.EnterCode().send_keys(BaseClass.pin)
        Home = login.ClickSubmit()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((Home.TestCard)))    # implimenting Explicit Wait which will check until procence of element
        time.sleep(1)
        assert self.driver.title=='Home | Enterprise test FYC'


    def test_ClickTestAutomationProject(self,setup):  # this function is to  Navigate to the 'Test Automation Project':-
        HomePage.HomePage(self.driver).Card().click()   #After logging in,we  navigate to the "All Titles" screen.and Locate and click on the Test automation project
        

    def test_DetailsTab(self,setup):    #  we  Click on the Details tab and wait for 5-10 seconds
        TestAutomationPage.TestAutomationCard(self.driver).DetailsTab().click()
        time.sleep(5)        

    def test_VideosTab(self,setup):       # we are  Switch back to the Videos tab.
        TestAutomationPage.TestAutomationCard(self.driver).VideoTab().click()


 
    def test_PlayVideoandPause(self,setup):     # here we are Locating the video on the page and click play allowingthe video to play till 10 seconds
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located((TestAutomationPage.TestAutomationCard.FirstVideoLocator)))
        video = TestAutomationPage.TestAutomationCard(self.driver)
        video.PlayIcon().click()
        time.sleep(10)
        self.driver.switch_to.frame(VideoPlayer.VideoPlayerPage.FrameLocator)   # we are swtching the I-Frame
        Video = VideoPlayer.VideoPlayerPage(self.driver)
        ActionChains(self.driver).move_to_element(Video.MediaPayer()).perform()   # to hover on the video player so that options for play pause appears

        self.driver.execute_script("arguments[0].pause();",Video.VideoJs())    # we are using javascript executer to play and pause the vieo
        self.driver.execute_script("arguments[0].currentTime=0",Video.VideoJs())
        self.driver.execute_script("arguments[0].play();",Video.VideoJs())   # play the video from starting
        Video.Settings().click()     
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located(Video.TimingLocator))    # waiting till the 10 seconds to play video 
        Video.PlayPauseToggel().click()    # pause video after 10 seconds
        self.driver.switch_to.default_content()   

    def test_ContinueWatching(self,setup):     # continue the video to play after we paused 
       
        time.sleep(1)
        VideoPlayer.VideoPlayerPage(self.driver).ContinurWatching().click()

    def test_SetVolume(self,setup):     # set the volut to 50 %   
        self.driver.switch_to.frame(VideoPlayer.VideoPlayerPage.FrameLocator)
        Video = VideoPlayer.VideoPlayerPage(self.driver)
        self.driver.execute_script("arguments[0].volume=0.5;",Video.VideoJs())   #  using javascript executer to set vlume to 50%
    


    def test_ChangeResolution(self,setup):   # Here we are Opening the settings menu and changeing the video resolution to 480p.
        
        Video = VideoPlayer.VideoPlayerPage(self.driver)
        Video.Settings().click()
        Video.ChangeTo480().click()  # change the video resolution to 480p
        time.sleep(5)
        ActionChains(self.driver).move_to_element(Video.MediaPayer()).perform()
        Video.Settings().click()
        Video.ChangeTo720().click()     # changing  the resolution back to 720p.
        time.sleep(1)

    def test_PauseAndExit(self,setup):    #we are Pauseing the video after adjusting the resolution
       
        Video = VideoPlayer.VideoPlayerPage(self.driver)
        Video.Settings().click()
        Video.PlayPauseToggel().click()
        self.driver.switch_to.default_content()
        Video.GoBack().click()   #  Press the Back button at the top of the screen to navigate out of the project

    def test_Logout(self,setup):    #Locate and click the Logout button to sign out from the platform.
        time.sleep(5)
        home = HomePage.HomePage(self.driver)
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located(home.SidebarLocator))  
        ActionChains(self.driver).move_to_element(home.Sidebar()).perform()  #hiver iver the sidebar till the Signout Option Appears
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located(home.SigoutLocator))
        home.Signout().click()    
