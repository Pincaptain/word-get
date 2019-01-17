from core.util import variables
from core.functions import parser
from core.functions import requests
from core.functions import scraper


def execute(argv):

    """
    Provides the user with the documentation and use cases.
    Starts listening for queries.

    :param argv:
    :return void:
    """

    print(format('{0}'.format(variables.text_welcome)))
    print(format('{0}'.format(variables.text_manual)))
    print(format('{0}'.format(variables.text_options)))
    print('')

    loop()


def result(query):
    response = requests.request(variables.wordnet_base_url + query)
    words = scraper.scrape(response)

    return words


def loop():

    """
    Loops endlessly or until explicitly stopped using specific keywords.
    Each iteration takes a query from the input.
    Each query goes through a validation process.
    Once validated a request is formed based on the query.

    :return void:
    """

    while True:
        query = input('Query: ')

        if query in variables.exit_keywords:
            break

        if not parser.is_valid_query(query):
            print('The query provided is invalid. Please try again!')

            continue

        print('Great! Your request is on its way!')
        print('')

        words = result(query)

        if words is None:
            print('No words found!')
            continue

        for key in words.keys():
            print(key + ': ')
            print('')

            for word in words[key]:
                print('Name: {0}'.format(query))
                print('Similar names: {0}'.format(str(word['names'])[1: len(str(word['names'])) - 1]) if len(word['names']) != 0 else 'Similar names: (No similar names provided)')
                print('Description: {0}'.format(word['description']) if len(word['description']) != 0 else 'Description: (No description provided)')
                print('Examples: {0}'.format(str(word['examples'])[1: len(str(word['examples'])) - 1]) if len(word['examples']) != 0 else 'Examples: (No examples provided)')
                print('')

    print('')
    print('Thanks for supporting this program!')