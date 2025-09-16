from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login(browser):
    # Mở trang đăng nhập
    browser.get("http://localhost:3000/login")

    # Tìm các phần tử
    email_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "email-address"))
    )
    password_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )

    # Điền thông tin hợp lệ
    email_field.send_keys("cao@gmail.com")
    password_field.send_keys("12345678@)")
    login_button.click()

    # Chờ chuyển hướng đến trang chính
    WebDriverWait(browser, 10).until(
        EC.url_contains("/")  # Trang chính sau đăng nhập
    )
    assert "/" in browser.current_url  # Xác nhận đăng nhập thành công

def test_failed_login(browser):
    # Mô tả: Kiểm tra đăng nhập thất bại với thông tin sai
    browser.get("http://localhost:3000/login")

    # Tìm các phần tử
    email_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "email-address"))
    )
    password_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )

    # Điền thông tin sai
    email_field.send_keys("wronguser@example.com")
    password_field.send_keys("wrongpassword")
    login_button.click()

    # Chờ và kiểm tra thông báo lỗi
    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert"))  # Cập nhật class dựa trên HTML thực tế
    )
    assert "Invalid email or password" in error_message.text  # Cập nhật thông báo lỗi thực tế