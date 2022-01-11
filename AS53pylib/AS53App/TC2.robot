Description

OBJECTIVE:
Verified that Avaya Aura AS5300 UC Client on Destop can change can call and leave a message

SETUP
Avaya Aura AS5300 UC Client (Version: 8.1.5.243.1)
- User A: Windows
- User B: Windows

PROCEDURE:
TC2-1
1. User A,B login to UCC
2. User A chooses who to call
3. User B answer the call
4. User A hold/unhold call

EXPECTED:
1. Login successfully
2. As normal
3. Answer sucessfully
4. Hold/unhold successfully

*** Settings ***
Library                 Zoomba.DesktopLibrary
Library                 ../lib/asapp.py     WITH NAME    ASapp
Variables               ../Setup/dataconfig.py
Test Teardown           run keyword if test failed              Screenshot and Clean Up
Test Setup              Open UCC

*** Variables ***
${USER_A}               ${user_1}
${USER_B}               ${user_3}
${SUBJECT_CALL}         ${subject_call_1}
${PASSWORD}             ${passwd_1}
${NETWORK}              ${network_1}

*** Test Cases ***
1. Make a call to other user and check hold/unhold call
    [Tags]  TC2-1
    Setup username and password                               ${USER_A}        ${NETWORK}
    Login to UCC                                              ${PASSWORD}
    Open UCC in remote machine
    Setup username and password in remote machine             ${USER_B}        ${NETWORK}
    Login to UCC in remote machine                            ${PASSWORD}
    Make a call to other user                                 ${USER_B}        ${SUBJECT_CALL}
    Received a call in remote machine
    Hold call
    Unhold call
    End call
    Logout
    Logout remote

