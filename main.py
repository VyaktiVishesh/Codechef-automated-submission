from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome()

browser.get("https://codechef.com")

username_element=browser.find_element_by_id("edit-name")
username_element.send_keys("garvis11")

password_element=browser.find_element_by_id("edit-pass")
password_element.send_keys("type_your_password _here") 


browser.find_element_by_id("edit-submit").click()

browser.get("https://www.codechef.com/submit/TEST")  

with open("Solution.cpp",'r') as f:  
    code=f.read()

code_element=browser.find_element_by_id("edit-program")
code_element.send_keys(code)

import time
time.sleep(10)
browser.find_element_by_id("edit-submit-1").click()   
