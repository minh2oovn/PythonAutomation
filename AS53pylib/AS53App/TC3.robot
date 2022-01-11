Description

OBJECTIVE:
Verified that Avaya Aura AS5300 UC Client on Destop can change can search with All Fields and add to contact

SETUP
Avaya Aura AS5300 UC Client (Version: 8.1.5.243.1)
- User A: Windows

PROCEDURE:
TC3-1
1. User A login to UCC
2. User A start search with Name/First Name/Last Name/ Phone Number/ SIP Address
TC3-2
3. Select a user to add to the contact

EXPECTED:
1. Login successfully
2. Search successfully
3. Add to contact successflly

*** Settings ***
Library                 Zoomba.DesktopLibrary
Library                 ../lib/asapp.py     WITH NAME    ASapp
Variables               ../Setup/dataconfig.py
Test Teardown           run keyword if test failed              Screenshot and Clean Up
Test Setup              Open UCC

*** Variables ***
${USER_A}               ${user_1}
${PASSWORD}             ${passwd_1}
${NETWORK}              ${network_1}
${TYPE_SEARCH}          ${search_type}
${INPUT_TEXT}           ${text}
${USER_ADDED}           ${number_added_1}

*** Test Cases ***
1. Search GAB and add contact for user
    [Tags]  TC3-1
    Setup username and password            ${USER_A}            ${NETWORK}
    Login to UCC                           ${PASSWORD}
    Search GAB                             ${TYPE_SEARCH}       ${INPUT_TEXT}

2. Add 1 contact to Personal Address Book
    [Tags]  TC3-2
    Add 1 contact                          ${USER_ADDED}
    Logout

