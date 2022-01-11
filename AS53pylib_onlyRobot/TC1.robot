*** Settings ***
Library     SeleniumLibrary
##Library     OperatingSystem
##Library     Selenium2Library

*** Variables ***
${CHROMEDRIVER_PATH}    C:/usr/local/bin/chromedriver/chromedriver.exe
${FIREFOXDRIVER_PATH}   C:/usr/local/bin/firefoxdriver/geckodriver.exe

## All values will input
${URL_WEB1}             https://47.11.1.5:8443/prov
${URL_WEB2}             https://47.11.1.5/pa
${URL_WEB3}             https://47.11.1.5/restproxy/myrest/personalinfo
${userlogin}            admin
${passwordlogin}        admin
${username1}            25999
${password1}            1234
${firstname1}           k25
${lastname1}            999
${email1}               htkieu999@tma.com.vn
${bussiness_phone1}     99925
${home_phone}           9992525
${cell_phone}           999252525
${page}                 999
${fax}                  999

## All location and button
${user_login_dir}           xpath://div[contains(text(),'Username:')]//following-sibling::*
${pass_login_dir}           xpath://div[contains(text(),'Password:')]//following-sibling::*
${login_button}             xpath://input[@type='submit'and @name='login']
${agree_button}             xpath://input[@type='button'and @name='loginConfirm']
${AS_menu_portlet_dir}      xpath://td[@class='rich-toolbar-item ']//form[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8'and@name='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8']
${AS_User_Add_dir}          xpath://td[@class='rich-toolbar-item ']//span[@id='_js_MainMenuPortlet__MainMenuPortlet_:j_id_jsp_1273130114_0:j_id_jsp_1273130114_8:j_id1:anchor'and contains(text(),'Add')]
${domain_list_dir}          xpath://select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_1189744534_0pc7:j_id14']
${domain_dsnmil}            xpath://select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_1189744534_0pc7:j_id14']/option[@value='dsn.mil']
${user_style_dir}           xpath://select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_1189744534_0pc7:j_id15']
${Standalone_user}          xpath://select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_1189744534_0pc7:j_id15']/option[contains(text(),'Standalone')]
${user_form_button}         xpath://input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_1189744534_0pc7:j_id16']
${username_field}           xpath://input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_3pc8']
${password_field}           xpath://input[@type='password' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_10pc8']
${confirm_password_field}   xpath://input[@type='password' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_13pc8']
${service_style_dir}        xpath://select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_16pc8']
${stand_service_style}      xpath://select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_16pc8']/option[@value='_system_default_standalone_']
${firstname_field}          xpath://input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_30pc8']
${lastname_field}           xpath://input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_34pc8']
${email_field}              xpath://input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_37pc8']
${buss_phone_field}         xpath://input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_39pc8']
${home_phone_field}         xpath://input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_41pc8']
${cell_phone_field}         xpath://input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_43pc8']
${page_field}               xpath://input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_45pc8']
${fax_field}                xpath://input[@type='text' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_47pc8']
${timezone_dir}             xpath://select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_49pc8']
${gmt7}                     xpath://select[@name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id_jsp_1470995508_49pc8']/option[@value="GMT+07:00"]
${save_user_button}         xpath://input[@type='submit' and @name='_js_MainMenuPortlet__dp_2__UserPortlet_:j_id_jsp_374979482_0:addView:j_id_jsp_257174066_1pc5:j_id17']
${success_save_alarm}       xpath://li[contains(text(),'User Added Successfully')]
${pa_login_dir}             xpath://div[contains(text(),'Username:')]//following-sibling::*
${papass_login_dir}         xpath://div[contains(text(),'Password:')]//following-sibling::*
${palogin_button}           xpath://input[@type='submit' and @name='login']
${paagree_button}           xpath://input[@type='button' and @name='loginConfirm']
${pa_personal}              xpath://span[contains(text(),'Personal')]
${pa_contactinfo}           xpath://a[@class='button-link-menu' and contains(text(),'Contact info')]
${user_data}                xpath://html[1]/body[1]/pre[1]

*** Keywords ***
##Failure Callback
     ##Capture Page Screenshot
     ##Log Source    loglevel=WARN

KW1 Open AS5300web
  ##CREATE WEBDRIVER   Chrome  executable_path=C:/usr/local/bin/chrome/chromedriver.exe
  ##GO TO    ${URL}
  ##close browser
  open browser   ${URL_WEB1}    chrome   options=add_argument("--ignore-certificate-errors")  executable_path=${CHROMEDRIVER_PATH}
  ##open browser    ${URl_WEB}    firefox   executable_path=${FIREFOXDRIVER_PATH}

KW2 Login AS5300web
   input text      ${user_login_dir}     ${userlogin}
   input text      ${pass_login_dir}     ${passwordlogin}
   click button    ${login_button}
   click button    ${agree_button}
   ##sleep         1 minutes

KW3 Add new User
   mouse over       ${domain_list_dir}
   page should contain element      ${domain_dsnmil}     5s
   click element    ${domain_dsnmil}
   mouse over       ${user_style_dir}
   Page Should Contain Element      ${Standalone_user}   5s
   click element    ${Standalone_user}
   click element    ${user_form_button}
   input text       ${username_field}       ${username1}
   input text       ${password_field}       ${password1}
   input text       ${confirm_password_field}   ${password1}
   mouse over       ${service_style_dir}
   page should contain element          ${stand_service_style}    5s
   click element    ${stand_service_style}
   input text       ${firstname_field}      ${firstname1}
   input text       ${lastname_field}       ${lastname1}
   input text       ${email_field}          ${email1}
   input text       ${buss_phone_field}     ${bussiness_phone1}
   input text       ${home_phone_field}     ${home_phone}
   input text       ${cell_phone_field}     ${cell_phone}
   input text       ${page_field}           ${page}
   input text       ${fax_field}            ${fax}
   mouse over       ${timezone_dir}
   page should contain element          ${gmt7}             5s
   click element    ${gmt7}
   click element    ${save_user_button}

KW4 Login PA user
   open browser    ${URL_WEB2}    chrome   options=add_argument("--ignore-certificate-errors")  executable_path=${CHROMEDRIVER_PATH}
   input text      ${pa_login_dir}     ${username1}@dsn.mil
   input text      ${papass_login_dir}     ${password1}
   click button    ${palogin_button}
   click button    ${paagree_button}
   wait until element is visible    ${pa_personal}      10s
   click element   ${pa_personal}
   click element   ${pa_contactinfo}

KW5 Verify Value on User infor PA
   go to   ${URL_WEB3}
   Element Should Contain    ${user_data}       "firstName":"${firstname1}"
   Element Should Contain    ${user_data}       "lastName":"${lastname1}"
   Element Should Contain    ${user_data}       "email":"${email1}"
   Element Should Contain    ${user_data}       "officePhone":"${bussiness_phone1}"
   Element Should Contain    ${user_data}       "homePhone":"${home_phone}"
   Element Should Contain    ${user_data}       "cellPhone":"${cell_phone}"
   Element Should Contain    ${user_data}       "pager":"${page}"
   Element Should Contain    ${user_data}       "fax":"${fax}"
   Element Should Contain    ${user_data}       "timeZone":"GMT+07:00"

*** Test Cases ***
1. Open Website AS5300 PROV for 1 new user
    KW1 Open AS5300web
    sleep         3s

2. Login admin to browser and agree notification (delay 10 seconds)
    KW2 Login AS5300web

3. Mouse over item on menu and add new user (delay 1 minutes)
    mouse over      ${AS_menu_portlet_dir}
    Page Should Contain Element     ${AS_User_Add_dir}    7s
    Click Element   ${AS_User_Add_dir}
    ##sleep         1 minutes
    sleep           3s

4. Choose user data and add user infor
    KW3 Add new User
    sleep           3s

5. Get successfully PROV alarm and close web
   Element Text Should Be    ${success_save_alarm}    User Added Successfully
   close browser

6. Check user infor on PA
   KW4 Login PA user
   sleep            3s

7. Get database and check user infor
   KW5 Verify Value on User infor PA
   close browser

8. Finish run Testing
   close all browsers