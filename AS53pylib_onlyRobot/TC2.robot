*** Settings ***
Library                 Zoomba.DesktopLibrary
Library                 OperatingSystem
Test Setup              OpenUCC
Library                 SeleniumLibrary

*** Variables ***
${APP}                  "C:\\Program Files (x86)\\Avaya Aura AS 5300 UC Client\\bin\\SMC.exe"
${URL}                  http://127.0.0.1:4723
${MAIN}                 SMC_Main_80517063-C175-4935-86FA-4BF1F2247287
${PREFERENCES}          User Preferences
${IM}                   Afx:00400000:20:00000000:00000010:00000000
${MAKEACALL}            Afx:00400000:20:00000000:00000010:00000000
${MAKEACALL2}           Afx:00400000:20:00000000:00000006:002C02E5
${CHROMEDRIVER_PATH}    C:/usr/local/bin/chromedriver/chromedriver.exe
${URL_WEB2}             https://10.255.251.162/pa
${pa_login_dir}         xpath://div[contains(text(),'Username:')]//following-sibling::*
${papass_login_dir}     xpath://div[contains(text(),'Password:')]//following-sibling::*
${palogin_button}           xpath://input[@type='submit' and @name='login']
${paagree_button}           xpath://input[@type='button' and @name='loginConfirm']
${pa_personal}              xpath://span[contains(text(),'Personal')]

#NETWORK AND USER
${USERNAME}             99003
${PASSWORD}             k1234
${NETWORK}              10.255.251.168

#IM
${RECEIVED1}            99103
${SUBJECT1}             TC1
${CONTENT}              TC1

#MAKEACALL
${RECEIVED2}            99108
${SUBJECT2}             TC2

#ID
${cert1_button}                         accessibility_id=1
${existing_button}                      accessibility_id=2
${cert2_button}                         accessibility_id=6
${subject_call_textbox}                 accessibility_id=1001
${subject_IM_textbox}                   accessibility_id=5077
${ID5164}                               accessibility_id=5164
${clear_IM_button}                      accessibility_id=5278
${send_IM_button}                       accessibility_id=5281
${content_IM_textbox}                   accessibility_id=5284
${password_textbox}                     accessibility_id=5336
${OK_password_button}                   accessibility_id=5341
${make_a_call_services}                 accessibility_id=5352
${IM_services}                          accessibility_id=5353
${PA_services}                          accessibility_id=5364
${logout_user_button}                   accessibility_id=5397
${OK_in_preferences_button}             accessibility_id=5440
${username_textbox}                     accessibility_id=5444
${network_combobox}                     accessibility_id=5484
${user_received_textbox}                accessibility_id=5821
${start_call_button}                    accessibility_id=5846
${start_IM_session_button}              accessibility_id=5851
${answercall_button}                    accessibility_id=5181
#NEVER CHANGE
${MAIN_FORM}                            //Window[contains(@ClassName, "${MAIN}")]
${PREFERENCES_FORM}                     //Window[contains(@Name, "${PREFERENCES}")]
${IM_FORM}                              //Window[contains(@ClassName, "${IM}")]
${IM_SESSION_FORM}                      //Window[contains(@Name, "${RECEIVED1}")]
${MAKE_A_CALL_FORM}                     //Window[contains(@ClassName, "${MAKEACALL}")]
${MAKE_A_CALL_SESSION_FORM}             //Window[contains(@ClassName, "${MAKEACALL2}")]
${CALL_RECEIVE_TAB}                     //Window[contains(@Name, "99003")]

*** Test Cases ***
1. Open UCC ad send message
    OpenUCC
#    run keyword and return status           Verify-Alarm
#    Sleep                                   5seconds
#    Switch Application By Locator           ${URL}        ${MAIN_FORM}
#    run keyword and return status           PopUp-Cancel
#    run keyword and return status           Check-Logout
#    run keyword and return status           PopUp-Cancel
#    Wait For And Click Element              name=Tools
#    Wait For And Click Element              name=Preferences...
#    Switch Application By Locator           ${URL}       ${PREFERENCES_FORM}
#    Wait For And Click Element              name=User
#    Wait For And Clear Text                 ${username_textbox}
#    Input Text                              ${username_textbox}    ${USERNAME}
#    Wait For And Click Element              name=Network
#    Click Element                           ${network_combobox}
#    Wait For And Click Element              name=${NETWORK}
#    Click Element                           ${OK_in_preferences_button}
#    run keyword and return status           PopUp-ChangeUserConfirm
#    Switch Application By Locator           ${URL}                          ${MAIN_FORM}
#    Wait For And Click Element              name=Login
#    run keyword and return status           Enter-Password
#    run keyword and return status           Verify-Cert-Login
#    Wait For And Click Element              ${cert1_button}
#    Wait For And Click Element              ${cert1_button}
#    Wait For And Click Element              ${cert1_button}
#    Wait Until Page Contains Element        ${IM_services}
#    Wait For And Click Element              ${IM_services}
#    Switch Application By Locator           ${URL}                          ${IM_FORM}
#    Input Text                              ${user_received_textbox}        ${RECEIVED1}
#    Wait For And Click Element              ${start_IM_session_button}
#    Switch Application By Locator           ${URL}                          ${IM_SESSION_FORM}
#    Wait For And Click Element              ${clear_IM_button}
#    Wait For And Click Element              ${cert1_button}
#    Wait For And Input Text                 ${subject_IM_textbox}           ${SUBJECT1}
#    Input Text                              ${content_IM_textbox}           ${CONTENT}
#    Click Element                           ${send_IM_button}
#    Page Should Not Contain Text            ${RECEIVED1} is Unavailable. Please try again later.
#    ## Quit Application
#
#2.Make 1 call and leave message
##    Switch Application By Locator           ${URL}                          ${MAIN_FORM}
#    Wait For And Click Element              ${make_a_call_services}
#    Switch Application By Locator           ${URL}                          ${MAKE_A_CALL_FORM}
#    Input Text                              ${user_received_textbox}        ${RECEIVED2}
#    Input Text                              ${subject_call_textbox}         ${SUBJECT2}
#    Wait For And Click Element              ${start_call_button}
#    Switch Application By Locator           ${URL}                         ${MAKE_A_CALL_SESSION_FORM}
#    sleep                                   30seconds
#    Wait For And Click Element              ${ID5164}

3. Make call by PA and leave message
    KW4 Login PA user and call
    OpenUCC
    sleep    6s
    Switch Application By Locator           ${URL}                      ${CALL_RECEIVE_TAB}
    #Wait For And Click Element              ${CALL_RECEIVE_TAB}
    log to console    abc
    sleep    3s

    Wait For And Click Element              ${answercall_button}

*** Keywords ***
OpenUCC
    Open Application                        ${URL}      app=${APP}
PopUp-Cancel
    Wait For And Click Element              name=Cancel
PopUp-ChangeUserConfirm
    Click Element                           ${cert2_button}
Verify-Alarm
    Wait For And Click Element              ${existing_button}
Verify-Cert-Login
    Wait For And Click Element              ${cert2_button}
Enter-Password
    Wait For And Clear Text                 ${password_textbox}
    Input Password                          ${password_textbox}             ${PASSWORD}
    Wait For And Click Element              ${OK_password_button}
Check-Logout
    Click Element                           name=Login
    Wait For And Click Element              ${logout_user_button}
IM-Send-Successful
    log to console    "Message sent successfully"

KW4 Login PA user and call
   open browser    ${URL_WEB2}    chrome   options=add_argument("--ignore-certificate-errors")  executable_path=${CHROMEDRIVER_PATH}
   SeleniumLibrary.input text      ${pa_login_dir}     ${USERNAME}@dsn.mil
   SeleniumLibrary.input text      ${papass_login_dir}     ${PASSWORD}
   SeleniumLibrary.click button    ${palogin_button}
   SeleniumLibrary.click button    ${paagree_button}
   sleep    5s
   SeleniumLibrary.input text              xpath://tbody/tr[2]/td[2]/div[1]/app-clicktocall-form[1]/form[1]/div[1]/div[4]/input[1]     99001@dsn.mil
   sleep    5s
   SeleniumLibrary.click button            xpath:/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/app-clicktocall-form[1]/form[1]/div[1]/div[6]/button[1]


