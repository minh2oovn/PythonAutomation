Desciption
1. Add new user
2. Login new user to PA

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
${remotetest}           ${Hubserver}

*** Keywords ***

*** Test Cases ***
1. Admin access PROV to add new user and verify it successfully
    [Tags]      Add
    ASweb.Login PROV    ${ServerWeb}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    3s
    Log To Console      Add new User on PROV
    ASweb.Add ASuser    ${username}     ${password}
    ASweb.Close Browser

2. New user login and verify user information display on PA
    [Tags]      PA
    ASweb.Login PA      ${ServerWeb}    ${username}        ${password}      ${remotetest}
    sleep    3s
    Log To Console      Verify User infor display on PA
    Check user PA infor     ${ServerWeb}    ${username}
    ASweb.Close Browser

