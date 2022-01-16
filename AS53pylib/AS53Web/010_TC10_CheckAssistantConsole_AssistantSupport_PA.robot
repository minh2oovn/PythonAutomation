Description

OBJECTIVE:
Verified that PA can display Assistant Console and Assistant Support services.

SETUP
SP15.5.1

PROCEDURE:
1. Assisgn Assistant Console on PROV
2. Verify PA can display Assistant Console
3. Assisgn Assistant Support on PROV
4. Verify PA can display Assistant Support
5. Unassisgn Assistant Console on PROV
6. Verify PA can't display Assistant Console
7. Unassisgn Assistant Support on PROV
8. Verify PA can't display Assistant Support
9. Assisgn Assistant Console, Assistant Support on PROV
10. Verify PA can display Assistant Console, Asisstant Support
11. Unassisgn Assistant Console, Assistant Support on PROV
12. Verify PA can't display Assistant Console, Asisstant Support

EXPECTED:
2. Verify PA can display Assistant Console
4. Verify PA can display Assistant Support
6. Verify PA can't display Assistant Console
8. Verify PA can't display Assistant Support
10. Verify PA can display Assistant Console, Asisstant Support
12. Verify PA can't display Assistant Console, Asisstant Support
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
${remotetest}           None

*** Keywords ***

*** Test Cases ***
1. Assign and check Assistant Console services on PA
    [Tags]  Assign and check Assistant Console services on PA
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start assign Assistant Console
    ASweb.Assign Assistant Console    ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Verify Assistant Console on PA
    ASweb.Close Browser
2. Unassign and check Assistant Console services on PA
    [Tags]  Unassign and check Assistant Console services on PA
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start unassign Assistant Console
    ASweb.Unassign Assistant Console      ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Verify Unassign Assistant Console on PA
    ASweb.Close Browser
3. Assign and check Assistant Support services on PA
    [Tags]  Assign and check Assistant Support services on PA
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start assign Assistant Support
    ASweb.Assign Assistant Support        ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Verify Assistant Support on PA
    ASweb.Close Browser
4. Unassign and check Assistant Support services on PA
    [Tags]  Unassign and check Assistant Support services on PA
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start unassign Assistant Support
    ASweb.Unassign Assistant Support      ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Verify Unassign Assistant Support on PA
    ASweb.Close Browser
5. Assign and check Assistant Console,Assistant Support services on PA
    [Tags]    Assign and check Assistant Console,Assistant Support services on PA
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start assign Assistant Support
    ASweb.Assign Assistant Console        ${username}
    ASweb.Assign Assistant Support        ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Verify Assistant Console on PA
    ASweb.Verify Assistant Support on PA
    ASweb.Close Browser
6. Unassign and check Assistant Console,Assistant Support services on PA
    [Tags]    Unassign and check Assistant Console,Assistant Support services on PA
    ASweb.Login PROV    ${Server_Web}     ${userlogin}     ${passwordlogin}      ${remotetest}
    sleep    5s
    Log To Console      Start assign Assistant Support
    ASweb.Unassign Assistant Console      ${username}
    ASweb.Unassign Assistant Support      ${username}
    ASweb.Close Browser
    ASweb.Login PA      ${ServerWeb}      ${username}      ${password}           ${remotetest}
    sleep    5s
    ASweb.Verify Unassign Assistant Console on PA
    ASweb.Verify Unassign Assistant Support on PA
    ASweb.Close Browser




