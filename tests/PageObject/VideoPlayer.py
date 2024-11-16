from selenium.webdriver.common.by import By




# we have mplemented PageObject Pattern for locatar selection
# here is POM for VideoPlayerPage


class VideoPlayerPage:


    def __init__(self,driver):
        self.driver = driver


    FrameLocator = ("video_player")
#    self.driver.switch_to.frame("video_player")
    MediaPlayerLocator = (By.ID,'media-player')

    VideoLocator = (By.XPATH,"//video")
    # self.driver.find_element(By.XPATH,"//video")
    SettingLocator = (By.CLASS_NAME,'jw-icon-settings')
    # self.driver.find_element(By.CLASS_NAME,'jw-icon-settings').click()

    PlayBackIconLocator = (By.CLASS_NAME,'jw-icon-playback')
    # self.driver.find_element(By.CLASS_NAME,'jw-icon-playback').click()

    TimingLocator = (By.XPATH,"//div[text()='00:10']")

    ContinurWatchingLocator = (By.XPATH,"//button[@aria-label='Continue Watching']")

    Resolution480PLocator = (By.XPATH,"//button[@aria-label='480p']")

    Resolution720PLocator = (By.XPATH,"//button[@aria-label='720p']")

    BackButtonLocator = (By.XPATH,"//button[@aria-label='Go Back and continue playing video']")  

    def MediaPayer(self):
        return self.driver.find_element(*VideoPlayerPage.MediaPlayerLocator)
    
    def VideoJs(self):
        return self.driver.find_element(*VideoPlayerPage.VideoLocator)

    def Settings(self):
        return self.driver.find_element(*VideoPlayerPage.SettingLocator)
    
    def PlayPauseToggel(self):
        return self.driver.find_element(*VideoPlayerPage.PlayBackIconLocator)
    
    def ContinurWatching(self):
        return self.driver.find_element(*VideoPlayerPage.ContinurWatchingLocator)
    
    def ChangeTo480(self):
        return self.driver.find_element(*VideoPlayerPage.Resolution480PLocator)
    
    def ChangeTo720(self):
        return self.driver.find_element(*VideoPlayerPage.Resolution720PLocator)
    
    def GoBack(self):
        return self.driver.find_element(*VideoPlayerPage.BackButtonLocator)