*** Settings ***
##Library     SeleniumLibrary
Library     OperatingSystem
##Library     Selenium2Library
#Library     Process
Library     Zoomba.DesktopLibrary

*** Variables ***
${CHROMEDRIVER_PATH}    C:/usr/local/bin/chromedriver/chromedriver.exe
${FIREFOXDRIVER_PATH}   C:/usr/local/bin/firefoxdriver/geckodriver.exe

${winapp}               http://127.0.0.1:4723
${UCC_app}              C:/Program Files (x86)/Avaya Aura AS 5300 UC Client/bin/SMC.exe

*** Keywords ***
##Failure Callback
     ##Capture Page Screenshot
     ##Log Source    loglevel=WARN

*** Test Cases ***
1. Open AS5300 UCC APP for 1 new user
    ##open browser   ${URL_WEB1}    chrome   options=add_argument("--ignore-certificate-errors")  executable_path=${CHROMEDRIVER_PATH}
    ##run process    python   C:\\Users\\UC\\WinAppDriver.exe
    open application    ${winapp}       app=${UCC_app}

2. Login User and choose user cert (delay 10 seconds)


