import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from BaseClass import BaseClass
from PageObject import VideoPlayer




#we are setting up Fixture for setup  , here our webdriver is getting initialise
@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome(service=Service('C:\\Users\\shivakar\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\Indee\\chromedriver.exe'))
    driver.get(BaseClass.url)
    driver.maximize_window()
    request.cls.driver=driver
    yield    # after performing test we will be closing webdriver
    driver.close()   


