Desciption
1. Search user on PROV with symbol, space, ...
2. Delete user

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





