from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class Issue_Search():
    def __init__(self, driver):

        self.driver=driver
        self.search_bar_xpath = "//input[@placeholder='Search issues']"

    #delete issue
        self.delete_created_issue_cssselector = "body > div:nth-child(103) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(12) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)"
        self.delete_button_cssselector = "#issueaction-delete-issue"
        self.delete_button_xpath="//span[contains(text(),'Delete')]"
        self.delete_confirmation_id = "delete-issue-submit"
        self.deleted_issue_verify_xpath="//p[normalize-space()='No issues were found matching your search']"
        self.project_hyperlink_xpath="(//span[@class='css-1we84oz'][normalize-space()='Projects'])[1]"
        self.issue_deleted_xpath="//div[@class='css-gipljn']"


    def enter_search_issue(self,search_text):
        enter_search=self.driver.find_element(by=By.XPATH,value=self.search_bar_xpath)
        enter_search.click()
        enter_search.send_keys(search_text,Keys.RETURN)
        time.sleep(5)

    def delete_issue(self):
        menu_dropdown_button = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.delete_created_issue_cssselector)))
        menu_dropdown_button.click()

        delete_button=self.driver.find_element(by=By.XPATH,value="//span[contains(text(),'Delete')]")
        self.driver.execute_script("arguments[0].click()",delete_button)

        delete_confirmation_popup = self.driver.find_element(by=By.ID, value=self.delete_confirmation_id)
        delete_confirmation_popup.click()

        issue_deleted_validation=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.issue_deleted_xpath)))
        print(issue_deleted_validation.text)

        self.driver.refresh()

    def verify_deleted_issue(self):
        verify_issue_deleted=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.deleted_issue_verify_xpath)))
        print(verify_issue_deleted.text)

    def return_to_project_page(self):
        project_hyperlink=self.driver.find_element(by=By.XPATH,value=self.project_hyperlink_xpath)
        project_hyperlink.click()



