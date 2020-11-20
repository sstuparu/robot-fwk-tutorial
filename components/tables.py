from selenium.webdriver.common.by import By
from components.authenticate import Authenticate
import datetime
from pages.base_page import BasePage

class Tables(Authenticate):
    main_page_obj = BasePage()
    
    
    def scrape_webpage_for_table(self, header_needed, as_selenium_objects=False):
        """This method extracts desired table from a page

        Parameters:
            header_needed (list or str): list of header cells or a string representing a cell from the header
            as_selenium_objects (bool): specifies if table contents are returned as selenium objects
        Return:
             table_dict: a dictionary with keys 'header' and 'content'
        """
        tables = self.driver.find_elements(By.XPATH, '//div[./ol]')
        headers = [table.find_element(By.CLASS_NAME, 'list-row-headings') for table in tables]
        contents = [table.find_element(By.TAG_NAME, 'ol') for table in tables]
        table_dict = dict()
        index = ''

        for i in range(len(headers)):
            header_contents = [cell.text for cell in headers[i].find_elements(By.TAG_NAME, 'span')]

            if header_needed == header_contents or header_needed in header_contents:
                index = i
                break
            else:
                continue

        if index == '':
            raise ValueError('No header found or header introduced is incorrect')
        elif as_selenium_objects:
            table_dict['header'] = headers[index]
            table_dict['content'] = contents[index]

            return table_dict
        else:
            table_dict['header'] = [cell.text for cell in headers[index].find_elements(By.TAG_NAME, 'span')]
            table_dict['content'] = [[cell.text for cell in row.find_elements(By.TAG_NAME, 'span') if cell.text != '']
                                     for row in contents[index].find_elements(By.TAG_NAME, 'li')]

            return table_dict

    def click_table_cell(self, header_needed, cell_to_identify_row, cell_to_click):
        """
        Method that finds a desired python release and clicks on 'Download' link for that specific release

        Parameters:
            header_needed (str or list): list of header cells or a string representing a cell from the header
            cell_to_identify_row (str): a string containing the desired python release
            cell_to_click (str): a string containing the cell one wants to click
        """
        table = self.scrape_webpage_for_table(header_needed=header_needed, as_selenium_objects=True)
        table_rows = table['content'].find_elements(By.TAG_NAME, 'li')
        desired_row = None

        for row in table_rows:
            if cell_to_identify_row in row.text:
                desired_row = row

        if not desired_row or cell_to_click not in desired_row.text:
            raise ValueError("Introduced values are not in the table or are spelled incorrectly")
        else:
            desired_row.find_element(By.PARTIAL_LINK_TEXT, cell_to_click).click()
            
    def convert_date_custom(self, input_date, format_string):
        return datetime.datetime.strptime(input_date, format_string)
    
    def validate_correspondece_between_tables_releases(self, table1, table2):
        correspondence_dict = dict()
        
        for row_table1 in table1['content']:
            for row_table2 in table2['content']:
                if row_table1[0] in row_table2[0]:
                    correspondence_dict[row_table1[0]] = correspondence_dict.get(row_table1[0], []) + [row_table2[0]]
                else:
                    continue

        for release in table1['content']:
            assert correspondence_dict.get(release[0]), \
                f"Release {release[0]} not found in dictionary"
    
    def validate_table_clicked_links(self, row_identifiers, button_to_click):
        for release in row_identifiers:
            self.main_page_obj.select_base_page_tab_and_click_subtab('downloads', 'All releases')
            self.click_table_cell('Release version', release, button_to_click)

            current_page_title = Authenticate().driver.find_element(By.CLASS_NAME, 'page-title').text

            assert release == current_page_title, \
                f"Current page title is {current_page_title} not {release} as expected"
