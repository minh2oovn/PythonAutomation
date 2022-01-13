*** Settings ***
Documentation     Admin assign/unassign Assistant services and check on PA
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
1. Assign Assistant Console and check PA
    [Tags]  Assign Assitant Console
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start assign Assistant Console
    ASweb.Assign Assistant Console    ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Check Assistant Console on PA
    ASweb.Close Browser
2. Unassign Assistant Console and check PA
    [Tags]  Unassign Assistant Console
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start unassign Assistant Console
    ASweb.Unassign Assistant Console      ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Check Unassign Assistant Console on PA
    ASweb.Close Browser
3. Assign Assistant Support and check PA
    [Tags]  Assign Assistant Support
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start assign Assistant Support
    ASweb.Assign Assistant Support        ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Check Assistant Support on PA
    ASweb.Close Browser
4. Unassign Assistant Support and check PA
    [Tags]  Unassign Assistant Console
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start unassign Assistant Support
    ASweb.Unassign Assistant Support      ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Check Unassign Assistant Support on PA
    ASweb.Close Browser
5. Assign Assistant Console, Assistant Support and check PA
    [Tags]    Assign Assistant Console and Assign Assistant Support
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start assign Assistant Support
    ASweb.Assign Assistant Console        ${username}
    ASweb.Assign Assistant Support        ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Check Assistant Console on PA
    ASweb.Check Assistant Support on PA
    ASweb.Close Browser
6. Unassign Assistant Console, Assistant Support and check PA
    [Tags]    Assign Assistant Console and Assign Assistant Support
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start assign Assistant Support
    ASweb.Unassign Assistant Console      ${username}
    ASweb.Unassign Assistant Support      ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Check Unassign Assistant Console on PA
    ASweb.Check Unassign Assistant Support on PA
    ASweb.Close Browser




