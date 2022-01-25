from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def read_file():
    input_user = {}
    with open('config.txt') as f:
        for line in f:
            (key, val) = line.split()
            input_user[key] = val
    input_user["day_selected"] = int(input_user["day_selected"])
    input_user["class_selected"] = int(input_user["class_selected"])
    input_user["gym_selected"] = int(input_user["gym_selected"])
    return input_user


def login(driver, user_input):
    username_input = driver.find_element(By.XPATH, '//*[@id="email"]')
    username_input.send_keys(user_input.get("username"))

    password_input = driver.find_element(By.XPATH, '//*[@id="member_password"]')
    password_input.send_keys(user_input.get("password"))

    login_click = driver.find_element(By.XPATH, '//*[@id="log-form"]/div[1]/form/button')
    login_click.click()


def click_on_schedule(driver):
    schedule_button = driver.find_element(By.XPATH, '//*[@id="do-schedule"]/div[2]')
    schedule_button.click()


def select_gym(driver, user_input):
    gym_selection_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="clubid"]'))
    gym_selection_dropdown.select_by_value(str(user_input.get("gym_selected")))


def select_class(driver, user_input):
    selected_day = '//*[@id="schedule-carousel"]/ul/li[' + str(user_input.get("day_selected")) + ']'
    day_schedule = driver.find_element(By.XPATH, selected_day)
    li_arr = day_schedule.find_elements(By.XPATH, './div[contains(@class, "schedule-class")]')
    li_arr[user_input.get("class_selected") - 1].find_element(By.XPATH,
                                                              '(./div[@class="col-xs-5 col-sm-12 text-right"])').click()


def accept_class(driver):
    box_button = driver.find_element(By.XPATH,
                                     '//*[@id="page-default"]/div[contains(@class, "modal fade in")]/div[contains(@class, "modal-dialog")]/div[contains(@class, "modal-content")]')
    confirm_button = box_button.find_element(By.XPATH, './div[contains(@class, "modal-footer")]')
    yes_button = confirm_button.find_element(By.XPATH, './a[contains(@class, "btn-book-class")]')
    yes_button.click()


def launch_browser(user_input):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://members.worldclass.ro/")

    login(driver, user_input)

    click_on_schedule(driver)

    select_gym(driver, user_input)

    select_class(driver, user_input)

    time.sleep(20)
    accept_class(driver)

    return driver


# columns are ordered from 1 to n
# class is numbered from 0 to n on website

us_input = read_file()
print(us_input)
launch_browser(us_input)
