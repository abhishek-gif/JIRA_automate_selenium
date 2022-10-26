from selenium.webdriver.common.by import By

class IssuePage():

    def __init__(self,driver):
        self.driver=driver

        self.project_tab_cssselector=".css-fgzm6b"
        self.createbutton_id="createGlobalItem"

    def print_project_name(self):
        project_tab=self.driver.find_element(by=By.CSS_SELECTOR,value=self.project_tab_cssselector)
        print(f"Project name selected in Project tab is : {project_tab.text}")


    def click_createbutton(self):
        self.driver.find_element(by=By.ID,value=self.createbutton_id).click()

