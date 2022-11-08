import time
from selenium import webdriver
#  Selenium custom exception that gets raised when an element cannot be found
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

zeut_number = ZEUT_NUMBER
phone_number = PHONE_NUMBER

# If you don't know the id number of the post office branch, you can check it here,
# The id number is the number next to the name
# post_office_list_to_check_the_branch_number_id_url='https://israelpost.co.il/%D7%A9%D7%99%D7%A8%D7%95%D7%AA%D7%99%D7%9D/%D7%90%D7%99%D7%AA%D7%95%D7%A8-%D7%A1%D7%A0%D7%99%D7%A4%D7%99%D7%9D-%D7%95%D7%96%D7%99%D7%9E%D7%95%D7%9F-%D7%AA%D7%95%D7%A8-%D7%91%D7%A7%D7%9C%D7%99%D7%A7/'
# print(post_office_list_to_check_the_branch_number_id_url)

post_office_index = "705"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = f"https://israelpost.co.il/%D7%A9%D7%99%D7%A8%D7%95%D7%AA%D7%99%D7%9D/%D7%90%D7%99%D7%AA%D7%95%D7%A8-%D7%A1%D7%A0%D7%99%D7%A4%D7%99%D7%9D-%D7%95%D7%96%D7%99%D7%9E%D7%95%D7%9F-%D7%AA%D7%95%D7%A8-%D7%91%D7%A7%D7%9C%D7%99%D7%A7/%D7%A1%D7%A0%D7%99%D7%A3/?no={post_office_index}"
driver.get(url)

# address_post_office = driver.find_element(By.ID, "branchaddress").text
# name_post_office_id = driver.find_element(By.CSS_SELECTOR, ".form-title.R.branchname").text

# next 2 lines wait until the element is available or 5 sec or until get appointment is clickable.
# and then wait for 1 sec before clicking on it ( to avoid being mark as a bot.
wait = WebDriverWait(driver, 8)
get_appointment = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary.apptButton')))
time.sleep(1)

# get_appointment.send_keys(Keys.ENTER)
ActionChains(driver).move_to_element(get_appointment).click(on_element=get_appointment).perform()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~next window- stage 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Choose the service type ( there is only one option)
# wait for up to 5  seconds for an element matching the given criteria to be found and the button is clickable
wait = WebDriverWait(driver, 10)
time.sleep(1.2)

# here there is difference between post office id=325 and id 705
choose_service_type = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".serviceIcon1")))
ActionChains(driver).move_to_element(get_appointment).click(on_element=choose_service_type).perform()
time.sleep(1)
continue_to_next_page = driver.find_element(By.CSS_SELECTOR, ".btn-ok.pull-left.btn-primary.btn")
ActionChains(driver).move_to_element(continue_to_next_page).click(on_element=continue_to_next_page).perform()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~next window- stage 2- done manualy  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''This part it done manually by the main user '''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~next page- 3rd stage~~~~~~~~~~~~~~~~~~~~~~~

# we are continued to the 3rd step of the process
# wait until the element is clickable or 90 seconds (time to fill the appointment time)
telephone_number1 = WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'userTelephone')))
ActionChains(driver).move_to_element(telephone_number1).click().send_keys(phone_number).perform()

time.sleep(1)
# inserting the phone number ones again:
telephone_number2 = driver.find_element(By.ID, "userTelephoneConfirmation")
ActionChains(driver).move_to_element(telephone_number2).click().send_keys(phone_number).perform()

telephone_continue = driver.find_element(By.ID, "nextstage")
ActionChains(driver).move_to_element(telephone_continue).click().perform()

time.sleep(20)
driver.quit()
