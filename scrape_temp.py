from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(By.ID, "displaytimer")
    time.sleep(2)
    return int(element.text.split()[-1])


if __name__ == "__main__":
    print(main())
