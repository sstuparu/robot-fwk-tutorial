import requests


class JokeRequests:
    one_rand_joke_url1 = r'https://official-joke-api.appspot.com/random_joke'
    one_rand_joke_url2 = r'https://official-joke-api.appspot.com/jokes/random'
    ten_rand_jokes_url1 = r'https://official-joke-api.appspot.com/random_ten'
    ten_rand_jokes_url2 = r'https://official-joke-api.appspot.com/jokes/ten'
    one_programming_joke_url1 = r'https://official-joke-api.appspot.com/jokes/programming/random'
    ten_programming_jokes_url2 = r'https://official-joke-api.appspot.com/jokes/programming/ten'
    base_url = r'https://official-joke-api.appspot.com/jokes'
    
    def get_jokes_from_url(self, URL):
        response = requests.get(URL)
        content = response.json()
        
        if type(content) == list:
            return content
        else:
            return [content]
    
    def get_jokes_by_type(self, type_of_joke='general', number='random'):
        desired_url = f"{self.base_url}/{type_of_joke}/{number}"
        response = requests.get(desired_url)
        content = response.json()
        
        if type(content) == list:
            return content
        else:
            return [content]

    def verify_type_of_joke(self, joke_list, expected_type='general'):
        for index, joke in enumerate(joke_list, start=1):
            assert joke['type'] == expected_type, \
                f"Failed! Joke no. {index} is type {joke['type']} not {expected_type}."
    
    def display_jokes(self, jokes):
        for index, joke in enumerate(jokes, start=1):
            print(f"Joke no. {index}:\n{joke['setup'].strip()}\n{joke['punchline'].strip()}\n")
    
    def display_jokes_by_id(self, jokes, odd_id=True):
        for joke in jokes:
            if odd_id and joke['id'] % 2 != 0: 
                print(f"Joke no. {joke['id']}:\n{joke['setup'].strip()}\n{joke['punchline'].strip()}\n")
            elif not odd_id and joke['id'] % 2 == 0:
                print(f"Joke no. {joke['id']}:\n{joke['setup'].strip()}\n{joke['punchline'].strip()}\n")
              
            
    
a = JokeRequests()
# b = a.get_jokes_from_url(JokeRequests.one_programming_joke_url1)
c = a.get_jokes_by_type('programming', 'ten')
a.display_jokes_by_id(c, False)