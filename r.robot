*** Settings ***
Documentation  Basic info
Library  Selenium2Library
#Library  C:/Users/sstuparu/PycharmProjects/robot-fwk-tutorial/components/authenticate.py
# Library  components.authenticate.Authenticate
Library    classes.py

*** Variables ***


*** Test Cases ***
User must sign out
    [Documentation]  This is basic info about test
    [Tags]  Smoke
    
   #Open Browser    http://www.amazon.com  chrome
   # Close Browser
    FOR    ${i}    IN RANGE    ${0}    ${10}
        Suma 
    END    
*** Keywords ***
