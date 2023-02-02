import json
import csv
def censor(filename: str, list_words):
    """
    list_words = ['London', 'Parliament', 'capital']
    filename:
    :param filename:
    :param list_words:
    :return:
    """
    with open(filename, 'rt') as file:
        text = file.read()
    for word in list_words:
        text = text.replace(word, '*' * len(word))
    with open("files/London 3.txt", "wt") as file:
        file.write(text)
    print(text)
censor("files/London.txt", ['London', 'Parliament', 'capital'])
def dict_words_count(filename: str):
    """
    dict_words_count
    :param filename: "files/London.txt"
    :return:
    """
    with open(filename, 'rt') as file:
        text = file.read()
    stat_dict_words = {}
    for word in text.split():
        word = word.lower().strip('\n').replace(",", "").replace(".", "").replace(":", "").replace("'", "").replace(
            "\n", " ")
        if word in stat_dict_words:
            stat_dict_words[word] += 1
        else:
            stat_dict_words[word] = 1
    with open("files/London.stat.json", 'w') as file:
        json.dump(stat_dict_words, file,  indent=4)
    return stat_dict_words
def from_dict_to_list(my_dict: dict) -> list:
    """
    from_dict_to_list
    :param my_dict:
    :return:
    """
    result = []
    for word, count in my_dict.items():
        result.append({'word': word, 'count': count})
    print(result)
    with open("files/London.stat.csv", 'wt') as file:
        writer = csv.writer(file, delimiter='\n')
        writer.writerow(result)
    return result
my_di = dict_words_count("files/London.txt")
print('-----------------')
print(my_di)
print('-----------------')
from_dict_to_list(my_di)





