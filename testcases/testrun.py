from selenium import webdriver
import time
import unittest
from pages.loginpage import LoginPage
from pages.yourwork_page import YourWork_Page
from pages.issue_search_page import Issue_Search

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../utilities/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver=self.driver

        driver.get("https://ccngbt.atlassian.net/")
        login=LoginPage(driver)
        login.enter_username("ccngbt@gmail.com")
        login.click_continue_button()
        login.enter_password("Test@123")
        login.click_login_button()

    def test_projects_createissues(self):
        driver=self.driver

        project_dropdown=YourWork_Page(driver)
        project_dropdown.click_project_dropdown()

        project_dropdown.click_view_all_project()
        driver.implicitly_wait(10)

#project name page
        project_name=YourWork_Page(driver)
        project_name.click_project_name()
        driver.implicitly_wait(10)

#issue list page
        issue_project_tab=YourWork_Page(driver)
        issue_project_tab.print_project_name()
        issue_project_tab.click_createbutton()
        time.sleep(10)

#Create issue page
        creating_issue=YourWork_Page(driver)
        creating_issue.verify_project_name()

        creating_issue.verify_issuetype()
        creating_issue.enter_issue_summary("The application web page crashed.")
        driver.implicitly_wait(10)

        creating_issue.enter_issue_description('''
        The Application web page crashed upon launching.

        Steps to Reproduce:
        1. Launch application using application URL.
        2. Observe the application crash.

        Expected Result: Application should load successfully to home page.
        ''')

        creating_issue.set_priority()

        creating_issue.enter_environment('''
The environment setup used are below:
Platform : Windows
Browser: Chrome
Server: XYZ
''')

        creating_issue.set_due_date()

        creating_issue.click_create_issue()
        driver.refresh()

#Search a bug
    def test_searchpage_deleteissues(self):
        driver=self.driver

        searching_issue=Issue_Search(driver)
        searching_issue.enter_search_issue("The application web page crashed.")

#Delete a bug
        deleting_issue=Issue_Search(driver)
        deleting_issue.delete_issue()

        searching_deleted_issue=Issue_Search(driver)
        searching_deleted_issue.verify_deleted_issue()

        project_hyperlink_navigation=Issue_Search(driver)
        project_hyperlink_navigation.return_to_project_page()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
         cls.driver.close()
         print("Test Completed")

if __name__ == '__main__':
    unittest.main()
