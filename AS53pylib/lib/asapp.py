import logging
import sys
import unittest
from datetime import datetime

import PIL.Image
from keyboard import press
import self as self
from PIL.Image import Image
# from IPython.display import Image
from PIL._imaging import display
from Zoomba.DesktopLibrary import AppiumCommon
from jproperties import Properties
from robot.utils import is_string
import os
from PIL import ImageGrab
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait
import basicfunc
import pyautogui
# import win32gui, win32con
import pyscreenshot
import click
import keyboard
import subprocess
import importlib
from AppiumLibrary import AppiumLibrary
from appium import webdriver
from psutil import Process, NoSuchProcess
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException, TimeoutException, \
    WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
from appium.webdriver.common.touch_action import TouchAction
from time import sleep, time
from robot import utils
from base64 import b64decode
from selenium.webdriver.remote.webelement import WebElement

from pylogs import configure_log

base_path = os.environ['AS53_python']
logger = configure_log(logging.DEBUG, __name__)
url = 'http://127.0.0.1:4723'
remote = 'http://10.128.197.131:4723'


class asapp((unittest.TestCase)):

    def __init__(self):
        self.driver = self.open_application()

    @keyword("Open UCC in remote machine")
    def remote(self):
        driver = webdriver.Remote(str(remote), desired_capabilities={
            "app": r"C:\\Program Files (x86)\\Avaya Aura AS 5300 UC Client\\bin\\SMC.exe"})
        return driver

    @keyword("Open UCC")
    def open_application(self):
        driver = webdriver.Remote(str(url), desired_capabilities={
            "app": r"C:\\Program Files (x86)\\Avaya Aura AS 5300 UC Client\\bin\\SMC.exe"})
        return driver

    @keyword("Setup username and password")
    def setup_username_and_network(self, username, network):
        try:
            self.open_application().find_element_by_accessibility_id('5342').click()
        except NoSuchElementException:
            pass
        self.open_application().find_element(By.NAME, 'Tools').click()
        self.open_application().find_element(By.NAME, 'Preferences...').click()
        windows = self.open_application().window_handles[1]
        driver_preferences = webdriver.Remote(str(url),
                                              desired_capabilities={"appTopLevelWindow": windows})
        self.open_application().switch_to.window(windows)
        driver_preferences.find_element(By.NAME, 'User').click()
        driver_preferences.find_element_by_accessibility_id('5444').clear()
        driver_preferences.find_element_by_accessibility_id('5444').send_keys(username)
        driver_preferences.find_element(By.NAME, 'Network').click()
        driver_preferences.find_element_by_accessibility_id('5484').click()
        driver_preferences.find_element(By.NAME, network).click()
        driver_preferences.find_element_by_accessibility_id('5440').click()
        try:
            driver_preferences.find_element_by_accessibility_id('6').click()
        except NoSuchElementException:
            logger.info('User not change')
        logger.info('Change to username:' + username + ' and network:' + network)

    @keyword("Setup username and password in remote machine")
    def setup_username_and_network_remote(self, username, network):
        try:
            self.remote().find_element_by_accessibility_id('5342').click()
        except NoSuchElementException:
            pass
        self.remote().find_element(By.NAME, 'Tools').click()
        self.remote().find_element(By.NAME, 'Preferences...').click()
        windows = self.remote().window_handles[1]
        driver_preferences = webdriver.Remote(str(remote),
                                              desired_capabilities={"appTopLevelWindow": windows})
        self.remote().switch_to.window(windows)
        driver_preferences.find_element(By.NAME, 'User').click()
        driver_preferences.find_element_by_accessibility_id('5444').clear()
        driver_preferences.find_element_by_accessibility_id('5444').send_keys(username)
        driver_preferences.find_element(By.NAME, 'Network').click()
        driver_preferences.find_element_by_accessibility_id('5484').click()
        driver_preferences.find_element(By.NAME, network).click()
        driver_preferences.find_element_by_accessibility_id('5440').click()
        try:
            driver_preferences.find_element_by_accessibility_id('6').click()
        except NoSuchElementException:
            logger.info('User not change')
        logger.info('Change to username:' + username + ' and network:' + network)

    @keyword("Quit UCC")
    def quit_application(self):
        self.open_application().find_element(By.NAME, 'Close').click()
        self.open_application().find_element(By.NAME, 'OK').click()

    def quit_application_remote(self):
        self.remote().find_element(By.NAME, 'Close').click()
        self.remote().find_element(By.NAME, 'OK').click()

    @keyword("Send IM")
    def send_im(self, user_received_im, subject, content):
        self.open_application().find_element_by_accessibility_id('5353').click()
        windows = self.open_application().window_handles[1]
        driver_im = webdriver.Remote(str(url),
                                     desired_capabilities={"appTopLevelWindow": windows})
        self.open_application().switch_to.window(windows)
        driver_im.find_element_by_accessibility_id('5821').send_keys(user_received_im)
        driver_im.find_element_by_accessibility_id('5851').click()
        windows = self.open_application().window_handles[1]
        driver_im = webdriver.Remote(str(url),
                                     desired_capabilities={"appTopLevelWindow": windows})
        self.open_application().switch_to.window(windows)
        driver_im.find_element_by_accessibility_id('5077').clear()
        driver_im.find_element_by_accessibility_id('5077').send_keys(subject)
        driver_im.find_element_by_accessibility_id('5284').send_keys(content)
        driver_im.find_element_by_accessibility_id('5278').click()
        driver_im.find_element_by_accessibility_id('1').click()
        driver_im.find_element_by_accessibility_id('5281').click()
        try:
            driver_im.find_element_by_xpath(
                "//*[@Name='" + user_received_im + " is Unavailable. Please try again later.']").is_displayed()
            logger.info("Message sent failed because user aren't online. Please try again later.")
            raise AssertionError("Message sent failed because user aren't online. Please try again later.")
        except NoSuchElementException:
            try:
                driver_im.find_element_by_xpath(
                    "//*[@Name='" + user_received_im + " is Unknown. Please check the address and try again.']").is_displayed()
                logger.info("Message sent failed because aren't exist. Please try again later.")
                raise AssertionError("Message sent failed because aren't exist. Please try again later.")
            except NoSuchElementException:
                pass
            logger.info('Message sent successfully')
            sleep(3)

    @keyword("Reply IM")
    def reply_im(self, subject_reply, content_reply):
        windows = self.remote().window_handles[1]
        driver_im = webdriver.Remote(str(remote),
                                     desired_capabilities={"appTopLevelWindow": windows})
        self.remote().switch_to.window(windows)
        try:
            driver_im.find_element_by_accessibility_id('5077').send_keys(subject_reply)
            driver_im.find_element_by_accessibility_id('5284').send_keys(content_reply)
            driver_im.find_element_by_accessibility_id('5281').click()
        except NoSuchElementException:
            raise AssertionError("Can't reply the message. Please try again")

    @keyword("Check IM")
    def check_im(self, content):
        windows = self.remote().window_handles[1]
        driver_im = webdriver.Remote(str(remote),
                                     desired_capabilities={"appTopLevelWindow": windows})
        self.remote().switch_to.window(windows)
        try:
            driver_im.find_element_by_xpath("//*[@Name='" + content + "']").is_displayed()
        except NoSuchElementException:
            raise AssertionError("The message was sent incorrectly")

    @keyword("Make a call to other user")
    def make_a_call(self, user_received_call, subject=''):
        self.open_application().find_element_by_accessibility_id('5352').click()
        windows = self.open_application().window_handles[1]
        driver_make_a_call = webdriver.Remote(str(url),
                                              desired_capabilities={"appTopLevelWindow": windows})
        self.open_application().switch_to.window(windows)
        driver_make_a_call.find_element_by_accessibility_id('5821').clear()
        driver_make_a_call.find_element_by_accessibility_id('5821').send_keys(user_received_call)
        driver_make_a_call.find_element_by_accessibility_id('1001').send_keys(subject)
        driver_make_a_call.find_element_by_accessibility_id('5846').click()
        windows = self.open_application().window_handles[1]
        driver_make_a_call = webdriver.Remote(str(url),
                                              desired_capabilities={"appTopLevelWindow": windows})
        self.open_application().switch_to.window(windows)
        logger.info("Calling to " + user_received_call)
        # driver_make_a_call.find_element(By.NAME, 'Close').click()
        # logger.info("Make a call successfully")

    @keyword("Received a call in remote machine")
    def received_a_call(self):
        windows = self.remote().window_handles[1]
        driver_received_a_call = webdriver.Remote(str(remote),
                                              desired_capabilities={"appTopLevelWindow": windows})
        self.remote().switch_to.window(windows)
        driver_received_a_call.find_element_by_accessibility_id('5181').click()
        logger.info("Call is established between 2 users")
        sleep(3)

    @keyword("Hold call")
    def hold_call(self):
        try:
            windows = self.open_application().window_handles[1]
            driver_make_a_call = webdriver.Remote(str(url),
                                                  desired_capabilities={"appTopLevelWindow": windows})
            self.open_application().switch_to.window(windows)
            driver_make_a_call.implicitly_wait(10)
            driver_make_a_call.find_element_by_accessibility_id('5165').click()
            logger.info("Call on hold")
        except NoSuchElementException:
            raise AssertionError("Can't hold call")

    @keyword("Unhold call")
    def unhold_call(self):
        try:
            windows = self.open_application().window_handles[1]
            driver_make_a_call = webdriver.Remote(str(url),
                                                  desired_capabilities={"appTopLevelWindow": windows})
            self.open_application().switch_to.window(windows)
            driver_make_a_call.implicitly_wait(10)
            driver_make_a_call.find_element_by_accessibility_id('5165').click()
            logger.info("Cancel on hold")
            sleep(2)
        except NoSuchElementException:
            raise AssertionError("Cant unhold call")

    @keyword("End call")
    def end_call(self):
        windows = self.open_application().window_handles[1]
        driver_make_a_call = webdriver.Remote(str(url),
                                              desired_capabilities={"appTopLevelWindow": windows})
        self.open_application().switch_to.window(windows)
        driver_make_a_call.find_element_by_accessibility_id('5164').click()
        windows = self.open_application().window_handles[1]
        driver_make_a_call = webdriver.Remote(str(url),
                                              desired_capabilities={"appTopLevelWindow": windows})
        driver_make_a_call.find_element(By.NAME, 'Close').click()
        logger.info("Call ended")

    @keyword("Search GAB")
    def search_gab(self, type_search, input_text):
        self.open_application().find_element_by_accessibility_id('5355').click()
        self.open_application().find_element_by_accessibility_id('5924').click()
        self.open_application().find_element(By.NAME, 'Global Address Book').click()
        try:
            if type_search == 'Name' or 'First Name' or 'Last Name' or 'Phone Number' or 'SIP Address':
                self.open_application().find_element_by_accessibility_id('5927').click()
                self.open_application().find_element(By.NAME, type_search).click()
        except NoSuchElementException:
            raise AssertionError("Error! Please re-enter the search type")
        self.open_application().find_element_by_accessibility_id('5926').clear()
        self.open_application().find_element_by_accessibility_id('5926').send_keys(input_text)
        self.open_application().find_element_by_accessibility_id('5928').click()
        logger.info("Search successfully!!!")

    @keyword("Add 1 contact")
    def add_a_contact(self, user_added):
        self.open_application().find_element_by_accessibility_id('5929').click()
        try:
            self.open_application().find_element(By.NAME, user_added + "@dsn.mil").click()
        except NoSuchElementException:
            raise AssertionError("Not found user!!!")
        self.open_application().find_element_by_accessibility_id('5914').click()
        windows = self.open_application().window_handles[1]
        driver_add_contact = webdriver.Remote(str(url),
                                              desired_capabilities={"appTopLevelWindow": windows})
        self.open_application().switch_to.window(windows)
        try:
            driver_add_contact.find_element_by_accessibility_id('5897').click()
            logger.info("Add " + user_added + " to contact successfully")
        except NoSuchElementException:
            driver_add_contact.find_element_by_accessibility_id('5898').click()
            raise AssertionError("User " + user_added + " already exists in contact")

    @keyword("Login to UCC")
    def login_ucc(self, password):
        try:
            self.open_application().find_element_by_accessibility_id('2').click()
        except NoSuchElementException:
            pass
        self.open_application().find_element_by_accessibility_id('5373').click()
        try:
            self.open_application().find_element_by_accessibility_id('5336').clear()
            self.open_application().find_element_by_accessibility_id('5336').send_keys(password)
            self.open_application().find_element_by_accessibility_id('5341').click()
        except NoSuchElementException:
            pass
        try:
            self.open_application().find_element_by_accessibility_id('6').click()
        except NoSuchElementException:
            pass
        try:
            self.open_application().find_element_by_accessibility_id('1').click()
            self.open_application().find_element_by_accessibility_id('1').click()
            self.open_application().find_element_by_accessibility_id('1').click()
        except NoSuchElementException:
            pass
        logger.info('Login successful')

    @keyword("Logout")
    def logout(self):
        try:
            self.open_application().find_element_by_accessibility_id('5373').click()
        except NoSuchElementException:
            pass
        try:
            windows = self.open_application().window_handles[1]
            driver1 = webdriver.Remote(str(url),
                                       desired_capabilities={"appTopLevelWindow": windows})
            driver1.find_element(By.NAME, 'Close').click()
        except IndexError:
            pass
        try:
            self.quit_application()
        except NoSuchElementException:
            pass

    @keyword("Logout remote")
    def logout_remote(self):
        try:
            self.remote().find_element_by_accessibility_id('5373').click()
        except NoSuchElementException:
            pass
        try:
            windows = self.remote().window_handles[1]
            driver1 = webdriver.Remote(str(remote),
                                       desired_capabilities={"appTopLevelWindow": windows})
            driver1.find_element(By.NAME, 'Close').click()
        except IndexError:
            pass
        try:
            self.quit_application_remote()
        except NoSuchElementException:
            pass

    @keyword("Login to UCC in remote machine")
    def login_ucc_remote(self, password):
        try:
            self.remote().find_element_by_accessibility_id('2').click()
        except NoSuchElementException:
            pass
        self.remote().find_element_by_accessibility_id('5373').click()
        try:
            self.remote().find_element_by_accessibility_id('5336').clear()
            self.remote().find_element_by_accessibility_id('5336').send_keys(password)
            self.remote().find_element_by_accessibility_id('5341').click()
        except NoSuchElementException:
            pass
        try:
            self.remote().find_element_by_accessibility_id('6').click()
        except NoSuchElementException:
            pass
        try:
            self.remote().find_element_by_accessibility_id('1').click()
            self.remote().find_element_by_accessibility_id('1').click()
            self.remote().find_element_by_accessibility_id('1').click()
        except NoSuchElementException:
            pass
        logger.info('Login successful')

    @keyword("Clean Up")
    def cleanup(self):
        try:
            logger.info("Collect logs and take screenshot")
            basicfunc.take_screenshot(self, self.driver)
            # self.driver.close()
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Clean up failure %s') % (error))

    @keyword("Screenshot and Clean Up")
    def screenshot(self):
        screenshot = ImageGrab.grab(all_screens=True)
        save_path = base_path+ "Screenshot-" + datetime.now().strftime(
            "%Y-%m-%d_%H%M%S") + ".png"
        screenshot.save(save_path)
        try:
            self.open_application().find_element_by_accessibility_id('5373').click()
        except NoSuchElementException:
            pass
        try:
            windows = self.open_application().window_handles[1]
            driver1 = webdriver.Remote(str(url),
                                       desired_capabilities={"appTopLevelWindow": windows})
            driver1.find_element(By.NAME, 'Close').click()
        except IndexError:
            pass
        try:
            self.quit_application()
        except NoSuchElementException:
            pass
        try:
            self.remote().find_element_by_accessibility_id('5353').is_displayed()
            try:
                self.remote().find_element_by_accessibility_id('5373').click()
            except NoSuchElementException:
                pass
            try:
                windows = self.remote().window_handles[1]
                driver1 = webdriver.Remote(str(remote),
                                           desired_capabilities={"appTopLevelWindow": windows})
                driver1.find_element(By.NAME, 'Close').click()
            except IndexError:
                pass
            try:
                self.quit_application_remote()
            except NoSuchElementException:
                pass
        except NoSuchElementException:
            pass
        return PIL.Image.open(save_path)
