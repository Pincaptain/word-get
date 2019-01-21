import json
import dicttoxml
import csv
import pandas


def export_to_json(dic, query):

    """
    Exports the passed dictionary to a json file.
    Returns a boolean result based on the success of the operation.

    :param dic:
    :param query:
    :return bool:
    """

    dic['query'] = query
    json_string = json.dumps(dic)

    try:
        with open('output.json', 'w') as file:
            file.write(json_string)

    except (IOError, OSError):
        return False

    return True


def export_to_xml(dic, query):

    """
    Exports the passed dictionary to a xml file.
    Returns a boolean result based on the success of the operation.

    :param dic:
    :param query:
    :return bool:
    """

    dic['query'] = query
    xml_dic = dicttoxml.dicttoxml(dic)

    try:
        with open('output.xml', 'w') as file:
            file.write(xml_dic.decode())

    except (IOError, OSError):
        return False

    return True


def transform_dic(dic, query):

    """
    Transforms the dictionary to a csv/excel ready dictionary.

    :param dic:
    :param query:
    :return:
    """

    new_dic = {
        'query': [],
        'type': [],
        'names': [],
        'description': [],
        'examples': []
    }

    for key in dic.keys():
        words = dic[key]

        for word in words:
            new_dic['query'].append(query)
            new_dic['type'].append(key)
            new_dic['names'].append(str(word['names'])[1: len(str(word['names'])) - 1])
            new_dic['description'].append(word['description'])
            new_dic['examples'].append(str(word['examples'])[1: len(str(word['examples'])) - 1])

    return new_dic


def export_to_csv(dic, query):

    """
    Exports the passed dictionary to a xml file.
    Returns a boolean result based on the success of the operation.

    :param dic:
    :param query:
    :return bool:
    """

    csv_dic = transform_dic(dic, query)

    try:
        with open('output.csv', 'w') as file:
            w = csv.writer(file, csv_dic)

            w.writerow(csv_dic.keys())

            keys = list(csv_dic.keys())
            single_instance = csv_dic[keys[0]]

            for i in range(len(single_instance)):
                row = []

                for key in keys:
                    row.append(csv_dic[key][i])

                w.writerow(row)

    except (IOError, OSError):
        return False

    return True
