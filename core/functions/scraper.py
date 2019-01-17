from core.functions import parser

from bs4 import BeautifulSoup


def scrape(response):

    """
    Scrapes the response content into a different resulting dictionary.
    The new dictionary contains categories as keys (nouns, verbs...) and a list of words attached to each one.

    :param response:
    :return:
    """

    if response['code'] != 200:
        return None

    soup = BeautifulSoup(response['content'], 'html.parser')
    result = {}

    for tag in soup.find_all('h3'):
        result[tag.string] = []

    uls = soup.find_all('ul')
    keys = list(result.keys())

    # Iterate over each unordered list
    for i in range(len(uls)):
        # Store the matching word category (Noun, Verb...)
        key = keys[i]

        # Iterate over each list items inside the list
        for li in uls[i].find_all('li'):
            word = {
                'description': parser.get_word_desc(li.text),
                'examples': parser.get_word_examples(li.text)
            }
            word_contents = []

            for a in li.find_all('a'):
                word_contents.append(a.string.strip())

            word['type'] = word_contents[1]
            word['names'] = []

            for j in range(2, len(word_contents)):
                word['names'].append(word_contents[j])

            result[key].append(word)

    return result
