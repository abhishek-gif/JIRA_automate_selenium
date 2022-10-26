from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProjectsPage():

    def __init__(self,driver):
        self.driver=driver

#        self.projectname_xpath="//a//span[text()='TestProject1_TA_Demo']"
#        self.projectname1_xpath="//span[normalize-space()='TestProject1_TA_Demo']"
        self.projectname2_xpath="//a[@href='/browse/TEST1']"

    def validate_projectname(self):
        self.driver.find_element(by=By.XPATH,value=self.projectname2_xpath).click()


