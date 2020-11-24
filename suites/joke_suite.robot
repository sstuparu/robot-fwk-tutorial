*** Settings ***
Documentation  Basic info
Library    Selenium2Library
Library    ApiLibrary      
Library    DateTime

*** Test Cases ***
Verify joke type
    [Documentation]
    ...    Retrieve 10 random jokes by type and for each joke verify if the type is correct. If not, raise an error.
    
    ${general_jokes} =    Get Jokes By Type    general    ten
    Verify Type Of Joke   ${general_jokes}    general
    
    ${programming_jokes} =     Get Jokes By Type    programming    ten
    Verify Type Of Joke    ${programming_jokes}    programming
    