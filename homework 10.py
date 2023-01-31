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
censor("files/London.txt", ['London', 'Parliament', 'capital'])
def dict_words_count(filename: str):
    """
    dict_words_count
    :param filename: "files/London.txt"
    :return:
    """
    #stat = {"filename": filename, "words": [], "word_count": {}}
    with open(filename, 'rt') as file:
        text = file.read()
    dict_words = {}
    for word in text.split():
        word = word.lower().strip('\n').replace(",", "").replace(".", "").replace(":", "").replace("'", "").replace(
            "\n", " ")
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    #print(dict_words)
    with open("files/London.stat.json", 'w') as file:
        json.dump(dict_words, file)
    return dict_words
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
    return result
my_di = dict_words_count("files/London.txt")
#print('-----------------')
print(my_di)
print('-----------------')
from_dict_to_list(my_di)

def censor_csv_stat(filename: str,stat,  my_di):
    """
    filename:
    my_di
    :param
    :return:
    """
    #stat = {"filename": filename, "words": [], "word_count": {}}
    with open("files/London.stat.csv", 'wt') as file:
        writer = csv.writer(file)
        writer.writerow(my_di)
        for word, count in stat.items():
            writer.writerow([word, count])
    return word, count