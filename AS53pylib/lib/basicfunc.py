import datetime
import logging
import time

from selenium.common.exceptions import WebDriverException
from pylogs import configure_log
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options

logger = configure_log(logging.DEBUG, __name__)
url = "10.128.197.131:4444/wd/hub"

def openChrome(RemoteIPorNone:str):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument('--disable-dev-shm-usage')
        if RemoteIPorNone=="None":
            driver = webdriver.Chrome(options=chrome_options, executable_path=r'C:\usr\local\bin\chromedriver\chromedriver.exe')
            time.sleep(5)
        else:
            driver = webdriver.Remote(command_executor=RemoteIPorNone + ":4444/wd/hub",desired_capabilities={"app": r"C:\Program Files\Google\Chrome\Application\chrome.exe"},options=chrome_options)
            time.sleep(5)
        return driver
    except WebDriverException as ex:
        logger.error('There is an exception while opening Chrome and Driver')
        logger.error('Exception ' + str(ex))
        return False

def take_screenshot_app(self, driver):
    try:
        logger.info('Taking screenshot...')
        screenshot_name = 'Screenshot-' + str(datetime.datetime.now()).replace(":", "-") + '.png'
        screenshot_name = screenshot_name.replace(" ", "-")
        logger.info('screenshot_name: ' + str(screenshot_name))
        if driver.save_screenshot(screenshot_name):
            logger.info('Take screenshot successfully with path: ' + str(screenshot_name))
            logger.info('<' + str(screenshot_name) + '>')
            return screenshot_name
        else:
            logger.info('Failed to take screenshot')
            return 'error'
    except WebDriverException as ex:
        logger.error('There is an exception while performing clean_up')
        logger.error('Exception ' + str(ex))
        return False

def take_screenshot_web(self, driver, screenshot_directory):
    try:
        logger.info('Taking screenshot...')
        screenshot_name = screenshot_directory + 'Screenshot-' + str(datetime.datetime.now()).replace(":", "-") + '.png'
        screenshot_name = screenshot_name.replace(" ", "-")
        logger.info('screenshot_name: ' + str(screenshot_name))
        if driver.save_screenshot(screenshot_name):
            logger.info('Take screenshot successfully with path: ' + str(screenshot_name))
            logger.info('<' + str(screenshot_name) + '>')
            return screenshot_name
        else:
            logger.info('Failed to take screenshot')
            return 'error'
    except WebDriverException as ex:
        logger.error('There is an exception while performing clean_up')
        logger.error('Exception ' + str(ex))
        return False

def closeWeb(self):
    try:
        logger.info("Close browsers after testing")
        self.driver.quit()
    except WebDriverException as ex:
        logger.error('Exception ' + str(ex))
        return False