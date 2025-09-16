import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()  # ChromeDriver phải trong PATH
    # Nếu ChromeDriver không trong PATH, dùng:
    # driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver.exe")
    driver.maximize_window()
    yield driver
    driver.quit()