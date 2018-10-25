# coding=utf-8
import selenium.webdriver.chrome.webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback

USER_NAME = '*********'
USER_PASS = '**********'


def main_fun():
    options = Options()
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.add_argument("no-sandbox")
    browser = Chrome(options=options)
    browser.set_window_size(1280, 1024)
    browser.maximize_window()
    browser.delete_all_cookies()
    try:
        hh_worker(browser)
    except Exception as ex:
        print(ex)
        traceback.print_exc()
    finally:
        browser.delete_all_cookies()
        browser.close()
        browser.quit()


def hh_worker(browser: selenium.webdriver.chrome.webdriver.WebDriver):
    browser.get("http://hh.ru/")
    wait = WebDriverWait(browser, 20)
    wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//label[@class = 'login-input']/input[contains(@name, 'username')]")),
               'can not find input form on page')
    browser.find_element(By.XPATH, "//label[@class = 'login-input']/input[contains(@name, 'username')]").send_keys(
        USER_NAME)
    browser.find_element(By.XPATH, "//label[@class = 'login-input']/input[contains(@name, 'password')]").send_keys(
        USER_PASS)
    browser.find_element(By.XPATH, "//div[@class = 'login-submit-form']/input[contains(@value, 'Войти')]").click()
    resume_updater(browser, wait)


def resume_updater(browser: selenium.webdriver.chrome.webdriver.WebDriver, wait: WebDriverWait):
    browser.get("https://hh.ru/applicant/resumes")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'resumelist__resume')]")))
    resume_list = browser.find_elements(By.XPATH, "//button[contains(@class, 'bloko-icon-link')]")
    for res in resume_list:
        try:
            res.click()
        except Exception as ex:
            print(ex)
    print("ok")


if __name__ == '__main__':
    main_fun()
