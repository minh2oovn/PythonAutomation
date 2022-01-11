Description

OBJECTIVE:
Verified that Avaya Aura AS5300 UC Client on Destop can change can setup user, network and send IM to other user.

SETUP
Avaya Aura AS5300 UC Client (Version: 8.1.5.243.1)
- User A: Windows
- User B: Windows

PROCEDURE:
TC1-1
1. User A,B login to UCC
2. User A chooses who to send the message
3. User A can send IM to user B
4. User B reply IM

EXPECTED:
1. Login successfully
2. As normal
3. Send message successflly
4. Reply message successfully

*** Settings ***
Library                 Zoomba.DesktopLibrary
Library                 ../lib/asapp.py     WITH NAME    ASapp
Variables               ../Setup/dataconfig.py
Test Teardown           run keyword if test failed              Screenshot and Clean Up
Test Setup              Open UCC

*** Variables ***
${USER_A}              ${user_1}
${USER_B}              ${user_2}
${PASSWORD}            ${passwd_1}
${NETWORK}             ${network_1}
${SUBJECT_SEND}        ${subject_IM_1}
${CONTENT_SEND}        ${content_IM_1}
${CONTENT_REPLY}       ${content_IM_2}
${SUBJECT_REPLY}       ${subject_IM_2}

*** Test Cases ***
1. Send IM to other user and reply the message
    [Tags]  TC1-1
    Setup username and password                               ${USER_A}              ${NETWORK}
    Login to UCC                                              ${PASSWORD}
    Open UCC in remote machine
    Setup username and password in remote machine             ${USER_B}              ${NETWORK}
    Login to UCC in remote machine                            ${PASSWORD}
    Send IM                                                   ${USER_B}              ${SUBJECT_SEND}         ${CONTENT_SEND}
    Reply IM                                                  ${SUBJECT_REPLY}       ${CONTENT_REPLY}
    Check IM                                                  ${CONTENT_SEND}
    Logout
    Logout remote



