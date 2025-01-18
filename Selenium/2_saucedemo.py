from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import datetime
def make_screenshot(okno):
    teraz = datetime.datetime.now()
    filename = teraz.strftime('screeny\\screenshot_%H_%M_%S.png')
    okno.get_screenshot_as_file(filename)


driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')

username_field = driver.find_element('id', 'user-namea')
username_field.send_keys('standard_user')

password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('secret_sauce')
sleep(2)

login_button = driver.find_element(By.XPATH,
                '/html/body/div/div/div[2]/div[1]/div/div/form/input')
login_button.click()
sleep(2)
make_screenshot(driver)


driver.quit()