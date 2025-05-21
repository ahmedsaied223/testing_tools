def wait_for_element(driver, by, value, timeout=10):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        print(f"Timeout: Element not found by {by} with value {value}")
        return None

def take_screenshot(driver, file_name):
    driver.save_screenshot(file_name)
