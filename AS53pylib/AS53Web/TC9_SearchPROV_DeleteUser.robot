Description

OBJECTIVE:
Verified that PROV can add new user and login PA successfully

SETUP
SP15.5.1

PROCEDURE:
1. Check PROV search 1 if Admin search username with number only
2. Check PROV search 2 if Admin search username with domain only
3. Check PROV search 3 if Admin search username with symbol only
4. Check PROV search 4 if Admin search username both name and domain
5. Check PROV search 5 if Admin search blank field
6. Delete user

EXPECTED:
PROV can search and display alarm correctly. Admin can delete user

*** Settings ***
Documentation     Admin search User on PROV and delete user
Library     ../lib/asweb.py    WITH NAME   ASweb
Variables   ../Setup/dataconfig.py
Test Teardown   Run Keyword If Test Failed    Clean Up

*** Variables ***
${Server_Web}           ${ServerWeb}
${userlogin}            ${adminlogin}
${passwordlogin}        ${passwordlogin}
${username}             ${username1}
${password}             ${password1}
${remotetest}           ${Hubserver}

*** Keywords ***

*** Test Cases ***
1. Admin access PROV to search user
    [Tags]      Search
    ASweb.Login PROV    ${ServerWeb}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    3s
    Log To Console      Search User on PROV
    ASweb.Search user on PROV    ${username}
    ASweb.Close Browser

2. Admin delete user
    [Tags]      DelUser
    ASweb.Login PROV    ${ServerWeb}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    3s
    Log To Console   Delete User on PROV
    ASweb.Delete user on PROV    ${username}    admin
    ASweb.Close Browser





