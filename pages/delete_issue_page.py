from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Delete_Issue():
    def __init__(self, driver):
        self.driver = driver

        self.delete_created_issue_cssselector = "body > div:nth-child(103) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(12) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)"
        self.delete_button_cssselector = "#issueaction-delete-issue"
        self.delete_button_xpath = "//span[contains(text(),'Delete')]"
        self.delete_confirmation_id = "delete-issue-submit"
        self.deleted_issue_verify_xpath = "(//a[normalize-space()='The application web page crashed.'])[1]"

    def delete_issue(self):
        menu_dropdown_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.delete_created_issue_cssselector)))
        menu_dropdown_button.click()

        delete_button = self.driver.find_element(by=By.XPATH, value="//span[contains(text(),'Delete')]")
        self.driver.execute_script("arguments[0].click()", delete_button)

    def verify_issue_deleted(self):
        self.driver.refresh()

        issue_summary=self.driver.find_element(by=By.XPATH,value=self.deleted_issue_verify_xpath)
        print(issue_summary.text)



