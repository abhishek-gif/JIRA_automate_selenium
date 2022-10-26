from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self,driver):
        self.driver=driver

        self.username_name="username"
        self.continue_button_id="login-submit"
        self.password_name="password"
        self.login_button_id="login-submit"

    def enter_username(self,username):
        self.driver.find_element(by=By.NAME,value=self.username_name).clear()
        self.driver.find_element(by=By.NAME, value=self.username_name).send_keys(username)

    def click_continue_button(self):
        self.driver.find_element(by=By.ID,value=self.continue_button_id).click()

    def enter_password(self,password):
        self.driver.find_element(by=By.NAME, value=self.password_name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(by=By.ID, value=self.login_button_id).click()


