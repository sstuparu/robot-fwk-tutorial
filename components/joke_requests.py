import requests


class JokeRequests:
    base_url1 = r'https://official-joke-api.appspot.com'
    base_url2 = r'https://official-joke-api.appspot.com/jokes'
    
    one_rand_joke_url1 = base_url1 + '/random_joke'
    one_rand_joke_url2 = base_url2 + '/random'
    ten_rand_jokes_url1 = base_url1 + '/random_ten'
    ten_rand_jokes_url2 = base_url2 + '/ten'
    one_programming_joke_url1 = base_url2 + '/programming/random'
    ten_programming_jokes_url2 = base_url2 + '/programming/ten'
    
    def get_jokes_from_url(self, URL):
        """Get jokes from the desired URl
        
        Parameters:
            URL (str): The URL where jokes can be found
        
        Returns:
            content (list): a list of dictionaries containing information about each joke
        """
        response = requests.get(URL)
        content = response.json()
        
        if type(content) == list:
            return content
        else:
            return [content]
    
    def get_jokes_by_type(self, type_of_joke='general', number='random'):
        """Get a number of joke of specific type
        
        Parameters:
            type_of_joke (str): The desired joke type
            number (str): The number of jokes returned
            
        Returns:
            A list of dictionaries containing information about each joke
        """
        desired_url = f"{self.base_url2}/{type_of_joke}/{number}"
        
        return self.get_jokes_from_url(desired_url)

    def verify_type_of_joke(self, joke_list, expected_type='general'):
        """Verifies that a list of jokes are of a specific type and throws an error otherwise
        
        Parameters:
            joke_list (list): A list of dictionaries containing information about each joke
            expected_type (str): The expected type of jokes to be found in 'joke_list'
        """
        for index, joke in enumerate(joke_list, start=1):
            assert joke['type'] == expected_type, \
                f"Failed! Joke no. {index} is type {joke['type']} not {expected_type}."
    
    def display_jokes(self, jokes, by_id=False):
        "Displays the setup and punchline of each joke as well as their no. of order"
        for index, joke in enumerate(jokes, start=1):
            self.print_joke(joke, index)()
    
    def display_jokes_by_id(self, jokes, odd_id=True):
        """Displays the jokes that have an odd id or an even id
        
        Parameters:
            jokes (list): List of dictionaries containing information about each joke
            odd_id (bool): True if one wants to display jokes that have an odd id and False if even id jokes are to be displayed
        """ 
        for index, joke in enumerate(jokes, start=1):
            if odd_id and joke['id'] % 2 != 0: 
                self.print_joke(joke, index)
            elif not odd_id and joke['id'] % 2 == 0:
                self.print_joke(joke, index)
              
    def print_joke(self, joke, index):
        print(f"Joke no. {index}:\n{joke['setup'].strip()}\n{joke['punchline'].strip()}\n")
        