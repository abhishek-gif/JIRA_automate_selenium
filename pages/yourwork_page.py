import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import datetime

class YourWork_Page():

    def __init__(self, driver):

        self.driver=driver
#Handle projects page
        self.project_dropdown_xpath="//span[normalize-space()='Projects']"
        self.view_all_project_xpath="//span[contains(text(),'View all projects')]"
        self.project_name_xpath="//a[@href='/browse/TEST1']"
        self.project_tab_xpath = "//span[text()='TestProject1_TA_Demo']"
        self.createbutton_id = "createGlobalItem"

#create issue page
        self.project_xpath = "//*[contains(text(),'TestProject1_TA_Demo (TEST1)')]"
        self.issuetype_xpath = "(//div[contains(text(),'Bug')])[1]"
        self.issuesummary_name = "summary"
        self.issuedescription_cssselector = "div[id='description-container'] div[class='css-164r41r'] div[class='i3zfbj-0 jwubIj'] div div div div p"
        self.priority_xpath = "(//div[contains(@class,'css-1a7rm5r-control')])[3]"
        self.priority1_xpath = "(//div[contains(text(),'Highest')])[1]"
        self.environment_cssselector="div[id='environment-container'] div[class='css-164r41r'] div[class='i3zfbj-0 jwubIj'] div div div div p"

#set_due_date
        self.duedate_menuxpath="(//div[contains(@class,'css-1b6odlt')])[8]"
        self.duedate_submenuxpath="//div[contains(text(),'Select date')]"
        self.duedate_submenu1xpath="(//div[@class='css-hufjvw'])[5]"
        self.duedate_submenu2cssselector="body > div:nth-child(130) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(4) > div:nth-child(12) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)"

        self.create_button_cssselector = "button[type='submit'] span[class='css-19r5em7']"
        self.issue_created_summary_cssselector = ".sc-1huqh8m-0.fbkMHZ[href='/browse/TEST1-8']"

    def click_project_dropdown(self):
        self.driver.find_element(by=By.XPATH, value=self.project_dropdown_xpath).click()

    def click_view_all_project(self):
        self.driver.find_element(by=By.XPATH,value=self.view_all_project_xpath).click()

    #Projects list page
    def click_project_name(self):

        element=self.driver.find_element(by=By.XPATH,value=self.project_name_xpath)
        print(f"The project name clickable is: {element.text}")
        element.click()

    #Issue list page
    def print_project_name(self):
        project_tab=self.driver.find_element(by=By.XPATH,value=self.project_tab_xpath)
        print(f"Project name selected in Project tab is : {project_tab.text}")

    def click_createbutton(self):
        self.driver.find_element(by=By.ID,value=self.createbutton_id).click()

    #Create issue page
    def verify_project_name(self):
        element_dropdown=self.driver.find_element(by=By.XPATH,value=self.project_xpath)
        print(f"{element_dropdown.text} is selected in Project dropdown.")

    def verify_issuetype(self):
        element_dropdown1=self.driver.find_element(by=By.XPATH, value=self.issuetype_xpath)
        print(f"{element_dropdown1.text} is selected in issue type dropdown.")

    def enter_issue_summary(self,summary):
        #self.driver.find_element(by=By.NAME, value=self.issuesummary_name).send_keys(summary)
        summary1=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,self.issuesummary_name)))
        summary1.send_keys(summary)

    def enter_issue_description(self,description):
        description_field=self.driver.find_element(by=By.CSS_SELECTOR, value=self.issuedescription_cssselector)
        description_field.click()
        description_field.send_keys(description)

    def set_priority(self):
        time.sleep(3)
        element_select=self.driver.find_element(by=By.XPATH, value=self.priority_xpath)
        element_select.click()
        self.driver.find_element(by=By.XPATH,value=self.priority1_xpath).click()

    def enter_environment(self,environment):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.environment_cssselector).send_keys(environment)

    def set_due_date(self):
        set_date_menu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.duedate_menuxpath)))
        set_date_submenu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.duedate_submenuxpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(set_date_menu)
        actions.click(set_date_submenu)
        actions.send_keys("5/27/2022",Keys.RETURN)
        actions.perform()

    def click_create_issue(self):
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.create_button_cssselector).click()
        print("Issue Created successfully")














