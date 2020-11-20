
from components.tables import Tables
from pages.available_releases import AvailableReleasesPage
from pages.base_page import BasePage
from pages.first_result import FirstSearchResultPage
from pages.search_results import SearchResultsPage


class ApiLibrary(Tables, 
                 AvailableReleasesPage, 
                 BasePage, 
                 FirstSearchResultPage, 
                 SearchResultsPage):
    pass