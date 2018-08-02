import time
from selenium import webdriver


def dummy():

    # Driver set-up
    driver_path = ".\\Drivers\\ChromeDriver\\chromedriver.exe"
    driver = webdriver.Chrome(driver_path)

    driver.get('http://www.google.com')
    time.sleep(10)


if __name__ == "__main__":
    dummy()
