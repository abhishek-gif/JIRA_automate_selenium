from selenium.webdriver.common.by import By

class CreateIssue(object):

    def __init__(self, driver):

        self.driver=driver

        self.project_xpath = "//*[contains(text(),'TestProject1_TA_Demo (TEST1)')]"
        self.issuetype_xpath = "(//div[contains(text(),'Bug')])[1]"
        self.issuesummary_name = "summary"
        self.issuedescription_cssselector = "div[id='description-container'] div[class='css-164r41r'] div[class='i3zfbj-0 jwubIj'] div div div div p"
        self.priority_xpath = "(//div[contains(@class,'css-1a7rm5r-control')])[3]"
        self.priority1_xpath = "(//div[contains(text(),'Highest')])[1]"
        self.environment_cssselector = "div[id='environment-container'] div[class='css-164r41r'] div[class='i3zfbj-0 jwubIj'] div div div div p"
        self.due_date_xpath = "(//div[contains(text(),'Select date')])[1]"
        self.create_button_xpath = "(//span[@class='css-19r5em7'][normalize-space()='Create'])[2]"
        self.issue_created_summary_cssselector = ".sc-1huqh8m-0.fbkMHZ[href='/browse/TEST1-8']"

    def verify_project_name(self):
        element_dropdown=self.driver.find_element(by=By.XPATH,value=self.project_xpath)
        print(f"{element_dropdown.text} is selected in Project dropdown.")

    def verify_issuetype(self):
        element_dropdown1=self.driver.find_element(by=By.XPATH, value=self.issuetype_xpath)
        print(f"{element_dropdown1.text} is selected in issue type dropdown.")

    def enter_issue_summary(self,summary):
        self.driver.find_element(by=By.NAME, value=self.issuesummary_name).send_keys(summary)

    def enter_issue_description(self,description):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.issuedescription_cssselector).send_keys(description)

    def set_priority(self):
        #self.driver.find_element(by=By.XPATH, value=self.priority_xpath)
        self.driver.find_element(by=By.XPATH,value=self.priority1_xpath).click()

    def enter_environment(self,environment):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.environment_cssselector).send_keys(environment)

    def set_due_date(self,duedate):
        self.driver.find_element(by=By.XPATH,value=self.due_date_xpath).send_keys(duedate)

    def click_create_button(self):
        self.driver.find_element(by=By.XPATH,value=self.create_button_xpath).click()




