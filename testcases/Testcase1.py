from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("../utilities/chromedriver.exe")

#Testcase1
page_launch= driver.get("https://ccngbt.atlassian.net/")

#Testcase2
driver.maximize_window()
login=driver.find_element(by=By.NAME, value="username")
login.send_keys("ccngbt@gmail.com")
driver.implicitly_wait(2)

continue_button=driver.find_element(by=By.ID, value="login-submit")
continue_button.click()

password = driver.find_element(by=By.NAME, value="password")
password.send_keys("Test@123")
driver.implicitly_wait(3)

login_button2=driver.find_element(by=By.ID, value="login-submit").click()

#Testcase3

project_dropdown=driver.find_element(by=By.XPATH, value="//span[normalize-space()='Projects']")
project_dropdown.click()
driver.implicitly_wait(10)

view_all_project=driver.find_element(by=By.XPATH,value="//span[contains(text(),'View all projects')]").click()

#Testcase4
project_name=driver.find_element(by=By.XPATH,value="(//span[normalize-space()='TestProject1_TA_Demo'])[1]")
validate=project_name.text
print(f"The project name : {validate} is available!")

#Testcase5
project_name.click()

#Testcase6
issue=driver.find_element(by=By.XPATH, value="//h1[normalize-space()='Issues']")
validate2=issue.text
print(f"{validate2} page loaded successfully!")

driver.implicitly_wait(10)
project_tab=driver.find_element(by=By.CSS_SELECTOR,value="button[class='css-1eus1fj'] span[class='sc-18tnwxk-1 jODjwb']")
validate3=project_tab.text
print(f"{validate3} tab is available in project page!")

#Testcase7
create_button=driver.find_element(by=By.ID,value="createGlobalItem")
create_button.click()
driver.implicitly_wait(10)

verify_projectname=driver.find_element(by=By.CSS_SELECTOR,value="div[id='issue-create.ui.modal.create-form.project-picker.project-select'] div[class='xkgbo7-3 aWXco']")
validate4=verify_projectname.text
print(f"The project name to create issue is: {validate4}")

issue_type=driver.find_element(by=By.XPATH,value="(//div[contains(text(),'Bug')])[1]")
validate5=issue_type.text
print(f"The issue type selected is: {validate5}")
driver.implicitly_wait(20)
#Your new issue shoud have a random summary,
# a random description, highest priority, random environment and a
# due date which should only be selected from the calendar control.

issue_summary=driver.find_element(by=By.NAME,value="summary")
issue_summary.send_keys("The application web page crashed.")
driver.implicitly_wait(10)

issue_description=driver.find_element(by=By.CSS_SELECTOR,value="div[id='description-container'] div[class='css-164r41r'] div[class='i3zfbj-0 jwubIj'] div div div div p")
issue_description.click()

issue_brief='''
The Application web page crashed upon launching. 

Steps to Reproduce:
1. Launch application using application URL.
2. Observe the application crash. 

Expected Result: Application should load successfully to home page. 
'''
issue_description.send_keys(issue_brief)
driver.implicitly_wait(30)


priority_dropdown=driver.find_element(by=By.XPATH,value="(//div[contains(@class,'css-1a7rm5r-control')])[3]")
priority_dropdown.click()
#driver.implicitly_wait(10)
priority_dropdown1=driver.find_element(by=By.XPATH,value="(//div[contains(text(),'Highest')])[1]")
priority_dropdown1.click()


environment=driver.find_element(by=By.CSS_SELECTOR,value="div[id='environment-container'] div[class='css-164r41r'] div[class='i3zfbj-0 jwubIj'] div div div div p")
environment.click()
environment_brief='''
The environment setup used are below:
Platform : Windows
Browser: Chrome
Server: XYZ
'''

environment.send_keys(environment_brief)
driver.implicitly_wait(30)

due_date=driver.find_element(by=By.XPATH,value="(//div[contains(@class,'css-1b6odlt')])[8]")

# due_date.send_keys(Keys.CONTROL, "a")
# due_date.send_keys(Keys.BACKSPACE)
due_date.clear()
due_date.send_keys("5/5/2022")

# print_date=due_date.text
# print(print_date)






