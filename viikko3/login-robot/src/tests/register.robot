*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists


Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Username is too short (minimum length: 3)

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle7  kalle123
    Output Should Contain  Username should contain only lower case letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  kalle  short
    Output Should Contain  Password is too short (minimum length: 8)

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  PasswordWithOnlyLetters
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Input New Command and Create User
    Input New Command
    Create User  kalle  kalle123