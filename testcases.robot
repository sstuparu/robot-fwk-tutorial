*** Settings ***
Documentation  Basic info
Library    Selenium2Library
Library    ApiLibrary      
Library    DateTime
Test Setup    Run Keywords    Create Driver    AND     Get To Web Address  
Test Teardown    Run Keyword    Close Driver

*** Test Cases ***
Verify latest python release
    [Documentation]
    ...    Steps:
    ...    1. Go to 'Downloads' -> 'All releases' page
    ...    2. Extract the latest python release and verify it is 3.9

    ${my_python_release}=    Set Variable    3.9    
    
    @{row1}    Create List    3.9    bugfix    2020-10-05    2025-10    PEP 596
    @{row2}    Create List    3.8    bugfix    2019-10-14    2024-10    PEP 569
    @{row3}    Create List    3.7    security    2018-06-27    2023-06-27    PEP 537
    @{row4}    Create List    3.6    security    2016-12-23    2021-12-23    PEP 494
    @{row5}    Create List    2.7    end-of-life    2010-07-03    2020-01-01    PEP 373
    @{my_list}    Create List    ${row1}    ${row2}    ${row3}    ${row4}    ${row5}
    
      
    Select Base Page Tab And Click Subtab       downloads    All releases
    
    &{releases}=    Scrape Webpage For Table    Python version    
    
    ${newest_python_release}=    Set Variable    ${releases}[content][0][0]
    Should Be Equal    ${my_python_release}    ${newest_python_release}    Python releases aren't the same
    
    Compare Available Releases    ${my_list}    ${releases}[content]
    
Verify example count is 5
    [Documentation]    
    ...     Steps:
    ...     1. Search for word 'decorator' on main page
    ...     2. Click on first result
    ...     3. Verify the no. of displayed examples is 5

    ${my_example_count}=    Set Variable    ${5}
    
    Search For Keyword    decorator
    Click First Result
    Click On Examples Link
    
    ${actual_example_no}=    Count Number Of Examples
    
    Should Be Equal    ${my_example_count}    ${actual_example_no}    Example counts aren't equal    
    
Compare table cells
    [Documentation]    
    ...    1. Go to 'Downloads' -> 'All releases' page
    ...    2. Extract the two tables present on the page
    ...    3. Compare the date cells from the first row of both tables and see that are similar
    
    Select Base Page Tab And Click Subtab       downloads    All releases
     
     &{table1}    Scrape Webpage For Table    Python version
     &{table2}    Scrape Webpage For Table    Release version
     
     ${date1}=    Convert Date Custom    ${table1}[content][0][2]    %Y-%m-%d
     ${date2}=    Convert Date Custom   ${table2}[content][0][1]    %b. %d, %Y
     
    Should Be Equal    ${date1}    ${date2}    
     
 Verify correspondence between tables
    [Documentation]  
    ...    1. Go to 'Downloads' -> 'All releases' page
    ...    2. Extract the two tables present on the page   
    ...    3. Verify each version of Python from the first table has at least one correspondence in the second table
    
    Select Base Page Tab And Click Subtab       downloads    All releases
    
    &{table1}    Scrape Webpage For Table    Python version
    &{table2}    Scrape Webpage For Table    Release version

    Validate Correspondece Between Tables Releases    ${table1}    ${table2}
    
Click on table cells
    [Documentation]    
    ...    1. Go to 'Downloads' -> 'All releases' page
    ...    2. Click 'Download' button of three desired releases
    ...    Verify the page that appears is corresponding to the release clicked
    
    @{row_identifiers}    Create List    Python 3.9.0    Python 3.8.6    Python 3.5.10
    ${button_to_click}    Set Variable    Download
    
    Validate Table Clicked Links    ${row_identifiers}    ${button_to_click}
    