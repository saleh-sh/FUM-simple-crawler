from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

def scroll(driver):
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, 5):
        driver.execute_script("window.scrollTo(0, {});".format(i))

url = "https://www.ketabrah.ir/"

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get(url)


try:
    categories = driver.find_element("id","RightCoulmnNavigatin")
    a_tags = categories.find_elements("tag name","a")
    for index,a in enumerate(a_tags):
        print(index, ": ", a.get_attribute("title"))
    user_option = int(input("enter a title number: "))
    if user_option > 3:
        driver.execute_script("arguments[0].scrollIntoView();", a_tags[10])
    a_tags[user_option].click()

except NoSuchElementException as e:
    print("Element not found: ", e)
except TimeoutException as e:
    print("Timeout occurred: ", e)
except Exception as e:
    print("An error occurred: ", e)


# Quit the driver
driver.quit()  