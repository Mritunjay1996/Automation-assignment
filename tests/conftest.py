"""
This module contains shared fixtures for web UI tests.
For now, only Chrome browser is supported.
"""

import json
import pytest
import allure
import os
import chromedriver_autoinstaller
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

CONFIG_PATH = 'resources/config.json'
Browser_path = "Scripts/chromedriver.exe"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome']
SUPPORTED_EXECUTORS = ['mobile', 'desktop']

@allure.step('Reading config from json file')
@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

@allure.step('Configuring browser')
@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    # To extend the browser support in future
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']

@allure.step('Configuring executor')
@pytest.fixture(scope='session')
def config_executor(config):
    # Validate and return the browser choice from the config data
    # To extend the browser support in future
    if 'executor' not in config:
        raise Exception('The config file does not contain "executor"')
    elif config['executor'] not in SUPPORTED_EXECUTORS:
        raise Exception(f'"{config["executor"]}" is not a supported executor')
    return config['executor']

@allure.step('Configuring the wait time for browser')
@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME



@allure.step('Initializing the configured browser')
@pytest.fixture(scope='session')
def browser(config_browser, config_wait_time, config_executor, request):
    # Initialize WebDriver
    global driver
    if config_browser == 'chrome':
        if config_executor == "mobile":
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '10'
            desired_caps['deviceName'] = 'myphone'
            desired_caps['browserName'] = 'Chrome'
            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        elif config_executor == "desktop":
            chromedriver_autoinstaller.install()
            options = Options()
            options.add_argument('log-level=3')
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-extensions")
            options.add_argument("--start-maximized")
            # options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            driver = Chrome(options=options)
        else:
            raise Exception(f'"{config_executor}" is not a supported executor')
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')
    driver.implicitly_wait(config_wait_time)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))