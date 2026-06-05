import pytest
from appium import webdriver

from config.config import load_config
from utils.logger import attach_screenshot, attach_html, attach_video


@pytest.fixture
def driver():
    config = load_config()

    caps = {
        'platformName': config.platform_name,
        'platformVersion': config.platform_version,
        'deviceName': config.device_name,
        'device': config.device_name,  # <-- добавил сюда
        'appPackage': config.app_package,
        'appActivity': config.app_activity,
        'automationName': 'UiAutomator2',
        'newCommandTimeout': 300
    }

    if config.app:
        caps['app'] = config.app

    if config.context == 'browserstack':
        caps['bstack:options'] = {
            'userName': config.browserstack_username,
            'accessKey': config.browserstack_access_key,
            'projectName': 'QA Guru Diploma',
            'buildName': 'Mobile Tests',
            'sessionName': 'Wikipedia Tests'
        }

    driver = webdriver.Remote(command_executor=config.remote_url, desired_capabilities=caps)
    driver.implicitly_wait(config.timeout)

    yield driver

    attach_screenshot(driver)
    attach_html(driver)
    attach_video(driver)
    driver.quit()
