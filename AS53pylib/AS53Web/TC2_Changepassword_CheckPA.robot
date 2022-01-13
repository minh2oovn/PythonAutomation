Description

OBJECTIVE:
Verified that PA can change user password successfully

SETUP
SP15.5.1

PROCEDURE:
1. Change your user password to AS5300 server with null
2. Change your user password to AS5300 server without old password
3. Change your user password to AS5300 server without new password
4. Change your user password to AS5300 server with PW not match
5. Change your user password to AS5300 server

EXPECTED:
PA can display alarm and change password successfully

*** Settings ***
Documentation     Admin add new User on PROV and check user infor on PA
Library     ../lib/asweb.py    WITH NAME   ASweb
Variables   ../Setup/dataconfig.py
Test Teardown   Run Keyword If Test Failed    Clean Up Web

*** Variables ***
${Server_Web}           ${ServerWeb}
${userlogin}            ${adminlogin}
${passwordlogin}        ${passwordlogin}
${username}             ${username1}
${password}             ${password1}
${newpassword}          k1234
${remotetest}           ${Hubserver}

*** Keywords ***

*** Test Cases ***
1. Change and verify new password on PA
    [Tags]      PW
    ASweb.Login PA      ${ServerWeb}    ${username}        ${password}      ${remotetest}
    sleep    3s
    Log To Console      Verify User change password on PA
    Verify user password on PA          ${username}        ${password}        ${newpassword}
    ASweb.Close Browser

