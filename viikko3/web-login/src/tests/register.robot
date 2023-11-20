*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Form
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Form
    Registering Should Fail With Message  Username is too short (minimum length: 3)

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  PasswordWithOnlyCharacters
    Set Password Confirmation  PasswordWithOnlyCharacters
    Submit Form
    Registering Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  NonMatchingPassword123
    Submit Form
    Registering Should Fail With Message  Given passwords doesn't match

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Form
    Registering Should Succeed
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed


Login After Failed Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  NonMatchingPassword123
    Submit Form
    Registering Should Fail With Message  Given passwords doesn't match
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Registering Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Form
    Click Button  Register
