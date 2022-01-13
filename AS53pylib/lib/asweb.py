import logging, sys, os, unittest
import time

from appium import webdriver
from robot.api.deco import keyword
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pylogs import configure_log
import basicfunc
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

logger = configure_log(logging.DEBUG, __name__)
as53log_path = os.environ['AS53_python']
# AS53_python will be C:\..PycharmProjects\..\AS53pylib\Collectlogs\
class asweb(unittest.TestCase):

    @keyword("Login PROV")
    def loginprov(self, web: str, Username: str, password: str, remoteIPorNone:str):
        logger.info("Accessing PROV Web with chrome")
        try:
            self.driver = basicfunc.openChrome(remoteIPorNone)
            self.driver.get("https://"+web+":8443/prov")
            logger.info("Successfully access to PROV")
            self.driver.find_element_by_xpath("//div[contains(text(),'Username:')]//following-sibling::*").send_keys(Username)
            self.driver.find_element_by_xpath("//div[contains(text(),'Password:')]//following-sibling::*").send_keys(password)
            self.driver.find_element_by_xpath("//input[@type='submit'and @name='login']").click()
            logger.info("Successfully login to PROV")
            self.driver.find_element_by_xpath("//input[@type='button'and @name='loginConfirm']").click()
            logger.info("Successfully confirm to PROV")
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Login AS53 PROV failure %s') % (error))
            raise

    @keyword("Add ASuser")
    def adduser(self, username: str, password: str):
        logger.info("Adding User")
        try:
            logger.info("Move to Add tab")
            menuhover = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item ']//form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8'and@name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8']"))
            menuhover.perform()
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item ']//span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8:j_id1:anchor'and contains(text(),'Add')]").click()
            logger.info("Select domain to User")
            domainhover = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_1189744534_0pc7:j_id14']"))
            domainhover.perform()
            self.driver.find_element_by_xpath("//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_1189744534_0pc7:j_id14']/option[@value='dsn.mil']").click()
            logger.info("Select Type to User")
            typehover = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_1189744534_0pc7:j_id15']"))
            typehover.perform()
            self.driver.find_element_by_xpath("//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_1189744534_0pc7:j_id15']/option[contains(text(),'Standalone')]").click()
            self.driver.find_element_by_xpath("//input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_1189744534_0pc7:j_id16']").click()
            self.driver.find_element_by_xpath("//input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_3pc8']").send_keys(username)
            self.driver.find_element_by_xpath("//input[@type='password' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_10pc8']").send_keys(password)
            self.driver.find_element_by_xpath("//input[@type='password' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_13pc8']").send_keys(password)
            logger.info("Select service style to User")
            servicestyle = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_16pc8']"))
            servicestyle.perform()
            self.driver.find_element_by_xpath("//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_16pc8']/option[@value='_system_default_standalone_']").click()
            self.driver.find_element_by_xpath("//input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_30pc8']").send_keys("f"+username)
            self.driver.find_element_by_xpath("//input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_34pc8']").send_keys("l"+username)
            self.driver.find_element_by_xpath("//input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_37pc8']").send_keys(username+"@tma.com.vn")
            self.driver.find_element_by_xpath("//input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_39pc8']").send_keys("b"+username)
            self.driver.find_element_by_xpath("//input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_41pc8']").send_keys("h"+username)
            self.driver.find_element_by_xpath("//input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_43pc8']").send_keys("c"+username)
            self.driver.find_element_by_xpath("//input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_45pc8']").send_keys("p"+username)
            self.driver.find_element_by_xpath("//input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_47pc8']").send_keys("f"+username)
            logger.info("Select timezone to User")
            timezone = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_49pc8']"))
            timezone.perform()
            self.driver.find_element_by_xpath("//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_49pc8']/option[@value='GMT+07:00']").click()
            logger.info("save user data to Web")
            self.driver.find_element_by_xpath("//input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id17']").click()
            alarm = self.driver.find_element_by_xpath("//ul[@class='messageBold']/li").text
            logger.info("Verify alarm on page after save page:"+alarm)
            self.assertTrue("User Added Successfully" in alarm, "Verify new user failure: "+alarm)
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Add new User failure %s') % (error))
            raise

    @keyword("Login PA")
    def loginpa(self, web: str, pauser: str, papass: str, remoteIPorNone:str):
        logger.info("Accessing PA Web with chrome")
        try:
            self.driver = basicfunc.openChrome(remoteIPorNone)
            self.driver.get("https://" + web + "/pa")
            time.sleep(5)
            logger.info("Successfully access to PA")
            self.driver.find_element_by_xpath("//div[contains(text(),'Username:')]//following-sibling::*").send_keys(pauser+"@dsn.mil")
            self.driver.find_element_by_xpath("//div[contains(text(),'Password:')]//following-sibling::*").send_keys(papass)
            self.driver.find_element_by_xpath("//input[@type='submit' and @name='login']").click()
            alarm = self.driver.find_element_by_xpath("*//div[@class='login-content']/div[@class='error-message']").text
            logger.info("Get alarm on page after login PA page:" + alarm)
            self.assertTrue("" in alarm, "Verify login PA failure: " + alarm)
            self.driver.find_element_by_xpath("//input[@type='button' and @name='loginConfirm']").click()
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Login PA failure %s') % (error))
            raise

    @keyword("Check user PA infor")
    def userPAinfor(self,asserver:str, username:str):
        logger.info("Move to User tab")
        try:
            self.driver.find_element_by_xpath("//span[contains(text(),'Personal')]").click()
            self.driver.find_element_by_xpath("//a[@class='button-link-menu' and contains(text(),'Contact info')]").click()
            logger.info("Verify your user data from AS5300 server")
            self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
            self.driver.get("https://"+asserver+"/restproxy/myrest/personalinfo")
            asdatabase = self.driver.find_element_by_xpath("//html[1]/body[1]/pre[1]").text
            self.assertTrue('"firstName"' + ":" + '"f' + username + '"' in asdatabase, "Verify firstName in as5300date failure")
            self.assertTrue('"lastName"' + ":" + '"l' + username + '"' in asdatabase, "Verify lastName in as5300date failure")
            self.assertTrue('"email"' + ":" + '"' + username + '@tma.com.vn"' in asdatabase, "Verify email in as5300date failure")
            self.assertTrue('"officePhone"' + ":" + '"b' + username + '"' in asdatabase, "Verify bussinessphone in as5300date failure")
            self.assertTrue('"homePhone"' + ":" + '"h' + username + '"' in asdatabase, "Verify homePhone in as5300date failure")
            self.assertTrue('"cellPhone"' + ":" + '"c' + username + '"' in asdatabase, "Verify cellPhone in as5300date failure")
            self.assertTrue('"pager"' + ":" + '"p' + username + '"' in asdatabase, "Verify pager in as5300date failure")
            self.assertTrue('"fax"' + ":" + '"f' + username + '"' in asdatabase, "Verify fax in as5300date failure")
            self.assertTrue('"timeZone"' + ":" + '"GMT+07:00"' in asdatabase, "Verify timezone in as5300date failure")
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Verify user PA information  failure %s') % (error))
            raise

    @keyword("Verify user password on PA")
    def userpassword(self, pauser:str, oldpass:str, newpass:str):
        logger.info("Move to password tab")
        try:
            self.driver.find_element_by_xpath("//span[contains(text(),'Personal')]").click()
            self.driver.find_element_by_xpath("//a[@class='button-link-menu' and contains(text(),'Password')]").click()
            logger.info("Change your user password to AS5300 server with null")
            self.driver.find_element_by_xpath("//div[@class='buttonArea']/button[@class='button']/span[contains(text(),'Apply')]").click()
            time.sleep(3)
            alarm = self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[2]/mat-dialog-content").text
            logger.info("Verify alarm 1 on page after null password:" + alarm)
            self.assertTrue('Password cannot be null.' in alarm, "Failed PA should NOT agree to change password with null")
            self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[3]/button[@class='button']/span[contains(text(),'OK')]").click()

            logger.info("Change your user password to AS5300 server without old password")
            self.driver.find_element_by_xpath("//input[@formcontrolname='newPassword' and @type='password']").send_keys(newpass)
            self.driver.find_element_by_xpath("//input[@formcontrolname='confirmNewPassword' and @type='password']").send_keys(newpass)
            self.driver.find_element_by_xpath("//div[@class='buttonArea']/button[@class='button']/span[contains(text(),'Apply')]").click()
            time.sleep(3)
            alarm = self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[2]/mat-dialog-content").text
            logger.info("Verify alarm 2 on page without old password:" + alarm)
            self.assertTrue('Password cannot be null.' in alarm, "Failed PA should NOT agree to change password without old password")
            self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[3]/button[@class='button']/span[contains(text(),'OK')]").click()
            self.driver.find_element_by_xpath("//input[@formcontrolname='newPassword' and @type='password']").send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath("//input[@formcontrolname='newPassword' and @type='password']").send_keys(Keys.BACKSPACE)
            self.driver.find_element_by_xpath("//input[@formcontrolname='confirmNewPassword' and @type='password']").send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath("//input[@formcontrolname='confirmNewPassword' and @type='password']").send_keys(Keys.BACKSPACE)

            logger.info("Change your user password to AS5300 server without new password")
            self.driver.find_element_by_xpath("//input[@formcontrolname='oldPassword' and @type='password']").send_keys(oldpass)
            self.driver.find_element_by_xpath("//div[@class='buttonArea']/button[@class='button']/span[contains(text(),'Apply')]").click()
            time.sleep(3)
            alarm = self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[2]/mat-dialog-content").text
            logger.info("Verify alarm 3 on page without new password:" + alarm)
            self.assertTrue('Password cannot be null.' in alarm,"Failed PA should NOT agree to change password without new password")
            self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[3]/button[@class='button']/span[contains(text(),'OK')]").click()

            logger.info("Change your user password to AS5300 server with PW not match")
            self.driver.find_element_by_xpath("//input[@formcontrolname='oldPassword' and @type='password']").send_keys(oldpass)
            self.driver.find_element_by_xpath("//input[@formcontrolname='newPassword' and @type='password']").send_keys("13579")
            self.driver.find_element_by_xpath("//input[@formcontrolname='confirmNewPassword' and @type='password']").send_keys("24680")
            self.driver.find_element_by_xpath("//div[@class='buttonArea']/button[@class='button']/span[contains(text(),'Apply')]").click()
            time.sleep(3)
            alarm = self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[2]/mat-dialog-content").text
            logger.info("Verify alarm 4 on page with PW not match:" + alarm)
            self.assertTrue('New passwords do not match' in alarm,"Failed PA should NOT agree to change password with PW not match")
            self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[3]/button[@class='button']/span[contains(text(),'OK')]").click()
            self.driver.find_element_by_xpath("//input[@formcontrolname='oldPassword' and @type='password']").send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath("//input[@formcontrolname='oldPassword' and @type='password']").send_keys(Keys.BACKSPACE)
            self.driver.find_element_by_xpath("//input[@formcontrolname='newPassword' and @type='password']").send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath("//input[@formcontrolname='newPassword' and @type='password']").send_keys(Keys.BACKSPACE)
            self.driver.find_element_by_xpath("//input[@formcontrolname='confirmNewPassword' and @type='password']").send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath("//input[@formcontrolname='confirmNewPassword' and @type='password']").send_keys(Keys.BACKSPACE)

            logger.info("Change your user password to AS5300 server ")
            self.driver.find_element_by_xpath("//input[@formcontrolname='oldPassword' and @type='password']").send_keys(oldpass)
            self.driver.find_element_by_xpath("//input[@formcontrolname='newPassword' and @type='password']").send_keys(newpass)
            self.driver.find_element_by_xpath("//input[@formcontrolname='confirmNewPassword' and @type='password']").send_keys(newpass)
            self.driver.find_element_by_xpath("//div[@class='buttonArea']/button[@class='button']/span[contains(text(),'Apply')]").click()
            time.sleep(3)
            alarm = self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[2]/mat-dialog-content").text
            logger.info("Verify alarm 5 on page:" + alarm)
            self.assertTrue('Password updated successfully' in alarm,"Failed PA should NOT agree to change password ")
            self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[3]/button[@class='button']/span[contains(text(),'OK')]").click()
            logger.info("Log out and check new password on PA")
            self.driver.find_element_by_xpath("//div[@class='menu']/p[@class='menuText']/a[contains(text(),'Logout')]").click()
            self.driver.find_element_by_xpath("//div[contains(text(),'Username:')]//following-sibling::*").send_keys( pauser+ "@dsn.mil")
            self.driver.find_element_by_xpath("//div[contains(text(),'Password:')]//following-sibling::*").send_keys(newpass)
            self.driver.find_element_by_xpath("//input[@type='submit' and @name='login']").click()
            alarm = self.driver.find_element_by_xpath("*//div[@class='login-content']/div[@class='error-message']").text
            logger.info("Get alarm on page after login PA page:" + alarm)
            self.assertTrue("" in alarm, "Verify login PA failure: " + alarm)
            self.driver.find_element_by_xpath("//input[@type='button' and @name='loginConfirm']").click()

            logger.info("Finish test and repair Setup")
            time.sleep(3)
            self.driver.find_element_by_xpath("//span[contains(text(),'Personal')]").click()
            self.driver.find_element_by_xpath("//a[@class='button-link-menu' and contains(text(),'Password')]").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//input[@formcontrolname='oldPassword' and @type='password']").send_keys(newpass)
            self.driver.find_element_by_xpath("//input[@formcontrolname='newPassword' and @type='password']").send_keys(oldpass)
            self.driver.find_element_by_xpath("//input[@formcontrolname='confirmNewPassword' and @type='password']").send_keys(oldpass)
            self.driver.find_element_by_xpath("//div[@class='buttonArea']/button[@class='button']/span[contains(text(),'Apply')]").click()
            time.sleep(3)
            alarm = self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[2]/mat-dialog-content").text
            logger.info("Verify alarm 6 on page:" + alarm)
            self.assertTrue('Password updated successfully' in alarm, "Failed PA should NOT agree to change password ")
            self.driver.find_element_by_xpath("//app-acknowledge-modal-form[@class='ng-star-inserted']/div[3]/button[@class='button']/span[contains(text(),'OK')]").click()
            logger.info("Log out and check new password on PA")
            self.driver.find_element_by_xpath("//div[@class='menu']/p[@class='menuText']/a[contains(text(),'Logout')]").click()
            self.driver.find_element_by_xpath("//div[contains(text(),'Username:')]//following-sibling::*").send_keys(pauser + "@dsn.mil")
            self.driver.find_element_by_xpath("//div[contains(text(),'Password:')]//following-sibling::*").send_keys(oldpass)
            self.driver.find_element_by_xpath("//input[@type='submit' and @name='login']").click()
            alarm = self.driver.find_element_by_xpath("*//div[@class='login-content']/div[@class='error-message']").text
            logger.info("Get alarm on page after login PA page:" + alarm)
            self.assertTrue("" in alarm, "Verify login PA failure: " + alarm)
            self.driver.find_element_by_xpath("//input[@type='button' and @name='loginConfirm']").click()
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Verify user PA information  failure %s') % (error))
            raise

    @keyword("Search user on PROV")
    def searchuser(self, username:str):
        logger.info("Searching User")
        try:
            logger.info("Check PROV search 1 if Admin search username with number only")
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys(username)
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='submit' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_32']").click()
            alarm = self.driver.find_element_by_xpath("//ul[@class='messageBold']/li").text
            logger.info("Verify alarm 1 on page after search number to page:" + alarm)
            self.assertTrue('User name is invalid. Must be of form user@domain' in alarm,"Failed PROV should NOT agree username with number only")
            time.sleep(3)
            logger.info("Check PROV search 2 if Admin search username with domain only")
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys(Keys.BACKSPACE)
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys("@dsn.mil")
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='submit' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_32']").click()
            alarm = self.driver.find_element_by_xpath("//ul[@class='messageBold']/li").text
            logger.info("Verify alarm 2 on page after search domain to page:" + alarm)
            self.assertTrue('Invalid User Name @dsn.mil .Please provide the fully qualified User Name i.e. user@domain .' in alarm,"Failed PROV should NOT agree username with domain only")
            time.sleep(3)
            logger.info("Check PROV search 3 if Admin search username with symbol only")
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys(Keys.BACKSPACE)
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys("!@#$%^&*()_+")
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='submit' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_32']").click()
            alarm = self.driver.find_element_by_xpath("//ul[@class='messageBold']/li").text
            logger.info("Verify alarm 3 on page after search symbol to page:" + alarm)
            self.assertTrue('Invalid Domain. Domain #$%^&*()_+ not found.' in alarm, "Failed PROV should NOT agree username with symbol only")
            time.sleep(3)
            logger.info("Check PROV search 4 if Admin search username both name and domain")
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys(Keys.BACKSPACE)
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys(username + "@dsn.mil")
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='submit' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_32']").click()
            alarm = self.driver.find_element_by_xpath("//div[@class='portlet-content-center']/div[@id='js_MainMenuPortlet__dp_2__UserPortlet_' and contains(text(),'User Details for: "+username+"@dsn.mil')]").text
            logger.info("Verify alarm 4 on page after search name and domain to page:" + alarm)
            self.assertTrue('User Details for: '+ username +'@dsn.mil' in alarm, "Failed PROV can NOT find "+username+"@dsn.mil")
            time.sleep(3)
            logger.info("Check PROV search 5 if Admin search blank field")
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys(Keys.BACKSPACE)
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='submit' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_32']").click()
            alarm = self.driver.find_element_by_xpath("//ul[@class='messageBold']/li").text
            logger.info("Verify alarm 5 on page after search blank field to page:" + alarm)
            self.assertTrue('User name is invalid. Must be of form user@domain' in alarm, "Failed PROV should NOT agree username with blank infor")
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Verify to search user on PROV failure %s') % (error))
            raise

    @keyword("Delete user on PROV")
    def deleteuser(self, username:str, adminpass:str):
        logger.info("deleting User")
        try:
            logger.info("Verify this user and move to User")
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='text' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_31']").send_keys(username + "@dsn.mil")
            self.driver.find_element_by_xpath("//td[@class='rich-toolbar-item  ']/span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_29']/form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30']/input[@type='submit' and @name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_30:j_id_jsp_1273130114_32']").click()
            alarm = self.driver.find_element_by_xpath("//div[@class='portlet-content-center']/div[@id='js_MainMenuPortlet__dp_2__UserPortlet_' and contains(text(),'User Details for: "+username+"@dsn.mil')]").text
            logger.info("Verify alarm on page after search domain to page:" + alarm)
            self.assertTrue('User Details for: '+username+'@dsn.mil in alarm', "Failed PROV can NOT find "+username+"@dsn.mil")
            Web_before = self.driver.window_handles[0]
            logger.info("Delete this user")
            self.driver.find_element_by_xpath("//td[@class='rich-tabhdr-side-cell']/table/tbody/tr/td[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:j_id_jsp_183778380_19_lbl']").click()
            self.driver.find_element_by_xpath("//td[@class='rich-tabpanel-content  ']/form[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:ActionsID:j_id_jsp_1752607741_1pc12']/table/tbody/tr/td/a[contains(text(),'Delete User')]").click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.find_element_by_xpath("//input[@type='password' and @name='password']").send_keys("admin")
            self.driver.find_element_by_xpath("//input[@type='submit' and @value='Confirm']").click()
            logger.info("Verify delete user successfully")
            self.driver.switch_to.window(Web_before)
            alarm = self.driver.find_element_by_xpath("//ul[@class='messageBold']/li").text
            logger.info("Verify alarm on page after search domain to page:" + alarm)
            self.assertTrue('	User deleted Successfully ',"Failed delete User" + username + "@dsn.mil")
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Verify to search user on PROV failure %s') % (error))
            raise

    @keyword('Assign Assistant Console')
    def assign_assistant_console(self, username: str):
        logger.info('Assign Assistant Console')
        try:
            self.driver.find_element_by_xpath(
                "//td[@class='rich-toolbar-item ']//form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8'and@name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//td[@class='rich-toolbar-item ']//span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8:j_id0:anchor'and contains(text(),'Search')]").click()
            logger.info("Select domain to User")
            domainhover = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(
                "//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id_jsp_22168579_5pc2']"))
            domainhover.perform()
            self.driver.find_element_by_xpath(
                "//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id_jsp_22168579_5pc2']//option[@value='dsn.mil']").click()
            self.driver.find_element_by_xpath(
                "//select[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria']").click()
            self.driver.find_element_by_xpath(
                "//select[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria']//option[@value='userName']").click()
            self.driver.find_element_by_xpath(
                "//input[@type='text'and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchForTextValue']").send_keys(
                username)
            self.driver.find_element_by_xpath(
                "//input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id13']").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//a[contains(text()," + username + ")]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//td[@class ='rich-tab-bottom-line ']//form[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:j_id_jsp_183778380_6:_form']//td[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:j_id_jsp_183778380_15_cell']").click()
            if self.driver.find_element_by_xpath(
                    "//td[@class='rich-table-cell ']//input[@type='checkbox' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_7pc10:6:j_id_jsp_558791977_16pc10']").is_selected():
                pass
            else:
                self.driver.find_element_by_xpath(
                    "//td[@class='rich-table-cell ']//input[@type='checkbox' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_7pc10:6:j_id_jsp_558791977_16pc10']").click()
                self.driver.find_element_by_xpath(
                    "//input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_25pc10']").click()
                logger.info("Add Assistant Console successfully")
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Verify arlam when assign Assistant Console %s') % (error))

    @keyword('Unassign Assistant Console')
    def unassign_assistant_console(self, username: str):
        logger.info('Assign Assistant Console')
        try:
            self.driver.find_element_by_xpath(
                "//td[@class='rich-toolbar-item ']//form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8'and@name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//td[@class='rich-toolbar-item ']//span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8:j_id0:anchor'and contains(text(),'Search')]").click()
            logger.info("Select domain to User")
            domainhover = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(
                "//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id_jsp_22168579_5pc2']"))
            domainhover.perform()
            self.driver.find_element_by_xpath(
                "//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id_jsp_22168579_5pc2']//option[@value='dsn.mil']").click()
            self.driver.find_element_by_xpath(
                "//select[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria']").click()
            self.driver.find_element_by_xpath(
                "//select[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria']//option[@value='userName']").click()
            self.driver.find_element_by_xpath(
                "//input[@type='text'and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchForTextValue']").send_keys(
                username)
            self.driver.find_element_by_xpath(
                "//input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id13']").click()
            time.sleep(3)
            self.driver.find_element_by_xpath(
                "/html/body/div[2]/div/div[2]/div/div/div[3]/div/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td[1]/table/tbody/tr/td/form/div/table/tbody/tr/td[2]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//td[@class ='rich-tab-bottom-line ']//form[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:j_id_jsp_183778380_6:_form']//td[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:j_id_jsp_183778380_15_cell']").click()
            if self.driver.find_element_by_xpath(
                    "//td[@class='rich-table-cell ']//input[@type='checkbox' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_7pc10:6:j_id_jsp_558791977_16pc10']").is_selected():
                self.driver.find_element_by_xpath(
                    "//td[@class='rich-table-cell ']//input[@type='checkbox' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_7pc10:6:j_id_jsp_558791977_16pc10']").click()
                self.driver.find_element_by_xpath(
                    "//input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_25pc10']").click()
            else:
                pass
                logger.info("Unassign Assistant Console successfully")
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Verify arlam when unassign Assistant Console %s') % (error))

    @keyword('Check Assistant Console on PA')
    def check_assistant_console_on_pa(self):
        try:
            self.driver.find_element_by_xpath(
                "//label[@class='labelStyle-bold ng-star-inserted' and contains(text(), 'Boss Display')]").is_displayed()
        except NoSuchElementException:
            raise AssertionError("Assistant Console doesn't show on PA")

    @keyword('Check Unassign Assistant Console on PA')
    def check_unassistant_console_on_pa(self):
        try:
            self.driver.find_element_by_xpath(
                "//label[@class='labelStyle-bold ng-star-inserted' and contains(text(), 'Boss Display')]").is_displayed()
            raise AssertionError("Assistant Console still display when unassigned")
        except NoSuchElementException:
            logger.info("Check unassign Assistant Console on PA successfully")

    @keyword('Check Assistant Support on PA')
    def check_assistant_support_on_pa(self):
        try:
            self.driver.find_element_by_xpath(
                "//label[@class='labelStyle-bold ng-star-inserted' and contains(text(), 'Primary Assistant')]").is_displayed()
            self.driver.find_element_by_xpath(
                "//label[@class='labelStyle-bold ng-star-inserted' and contains(text(), 'Alternate Assistant')]").is_displayed()
            self.driver.find_element_by_xpath(
                "//label[@class='labelStyle-bold ng-star-inserted' and contains(text(), 'Assistant Route')]").is_displayed()
        except NoSuchElementException:
            raise AssertionError("Assistant Support doesn't show on PA")

    @keyword('Check Unassign Assistant Support on PA')
    def check_unassistant_support_on_pa(self):
        try:
            self.driver.find_element_by_xpath(
                "//label[@class='labelStyle-bold ng-star-inserted' and contains(text(), 'Primary Assistant')]").is_displayed()
            self.driver.find_element_by_xpath(
                "//label[@class='labelStyle-bold ng-star-inserted' and contains(text(), 'Alternate Assistant')]").is_displayed()
            self.driver.find_element_by_xpath(
                "//label[@class='labelStyle-bold ng-star-inserted' and contains(text(), 'Assistant Route')]").is_displayed()
            raise AssertionError("Assistant Support still display when unassigned")
        except NoSuchElementException:
            logger.info("Check unassign Assistant Support on PA successfully")

    @keyword('Assign Assistant Support')
    def assign_assistant_support(self, username: str):
        logger.info('Assign Assistant Support')
        try:
            self.driver.find_element_by_xpath(
                "//td[@class='rich-toolbar-item ']//form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8'and@name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//td[@class='rich-toolbar-item ']//span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8:j_id0:anchor'and contains(text(),'Search')]").click()
            logger.info("Select domain to User")
            domainhover = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(
                "//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id_jsp_22168579_5pc2']"))
            domainhover.perform()
            self.driver.find_element_by_xpath(
                "//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id_jsp_22168579_5pc2']//option[@value='dsn.mil']").click()
            self.driver.find_element_by_xpath(
                "//select[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria']").click()
            self.driver.find_element_by_xpath(
                "//select[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria']//option[@value='userName']").click()
            self.driver.find_element_by_xpath(
                "//input[@type='text'and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchForTextValue']").send_keys(
                username)
            self.driver.find_element_by_xpath(
                "//input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id13']").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//a[contains(text()," + username + ")]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//td[@class ='rich-tab-bottom-line ']//form[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:j_id_jsp_183778380_6:_form']//td[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:j_id_jsp_183778380_15_cell']").click()
            if self.driver.find_element_by_xpath(
                    "//td[@class='rich-table-cell ']//input[@type='checkbox' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_7pc10:7:j_id_jsp_558791977_16pc10']").is_selected():
                pass
            else:
                self.driver.find_element_by_xpath(
                    "//td[@class='rich-table-cell ']//input[@type='checkbox' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_7pc10:7:j_id_jsp_558791977_16pc10']").click()
                self.driver.find_element_by_xpath(
                    "//input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_25pc10']").click()
                logger.info("Assign Assistant Support successfully")
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Verify arlam when assign Assistant Support %s') % (error))

    @keyword('Unassign Assistant Support')
    def unassign_assistant_support(self, username: str):
        logger.info('Assign Assistant Support')
        try:
            self.driver.find_element_by_xpath(
                "//td[@class='rich-toolbar-item ']//form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8'and@name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//td[@class='rich-toolbar-item ']//span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8:j_id0:anchor'and contains(text(),'Search')]").click()
            logger.info("Select domain to User")
            domainhover = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(
                "//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id_jsp_22168579_5pc2']"))
            domainhover.perform()
            self.driver.find_element_by_xpath(
                "//select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id_jsp_22168579_5pc2']//option[@value='dsn.mil']").click()
            self.driver.find_element_by_xpath(
                "//select[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria']").click()
            self.driver.find_element_by_xpath(
                "//select[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchCriteria']//option[@value='userName']").click()
            self.driver.find_element_by_xpath(
                "//input[@type='text'and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:searchForTextValue']").send_keys(
                username)
            self.driver.find_element_by_xpath(
                "//input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:searchView:j_id_jsp_22168579_0pc2:j_id13']").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//a[contains(text()," + username + ")]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//td[@class ='rich-tab-bottom-line ']//form[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:j_id_jsp_183778380_6:_form']//td[@id='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:j_id_jsp_183778380_15_cell']").click()
            if self.driver.find_element_by_xpath(
                    "//td[@class='rich-table-cell ']//input[@type='checkbox' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_7pc10:7:j_id_jsp_558791977_16pc10']").is_selected():
                self.driver.find_element_by_xpath(
                    "//td[@class='rich-table-cell ']//input[@type='checkbox' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_7pc10:7:j_id_jsp_558791977_16pc10']").click()
                self.driver.find_element_by_xpath(
                    "//input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_183778380_0:Services:j_id_jsp_558791977_1pc10:j_id_jsp_558791977_25pc10']").click()
            else:
                pass
                logger.info("Unassign Assistant Support successfully")
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Verify arlam when unassign Assistant Support %s') % (error))

    @keyword("Clean Up Web")
    def cleanup_web(self):
        try:
            logger.info("Collect logs and take screenshot")
            basicfunc.take_screenshot_web(self, self.driver, as53log_path)
            self.driver.close()
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Clean up failure %s') % (error))
            raise

    @keyword("Close Browser")
    def closeAllWeb(self):
        try:
            logger.info("Close all Browsers")
            basicfunc.closeWeb(self)
        except (NoSuchElementException, TimeoutException, WebDriverException) as error:
            logger.error(('Close all browsers failure %s') % (error))
            raise

