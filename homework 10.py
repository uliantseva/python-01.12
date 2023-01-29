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
    print(text)
    with open("files/London 3.txt", "wt") as file:
        file.write(text)

censor("files/London.txt", ['London', 'Parliament', 'capital'])

def censor_json(filename: str):
    """
    filename:
    :param filename
    :return:
    """
    with open(filename, 'rt') as file:
        text = file.read()
    word_count = {}
    for word in text.split():
        word = word.lower().strip('\n').replace(",", "").replace(".", "").replace(":", "").replace("'", "").replace(
                "\n", " ")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count)
    with open("files/London.stat.json", 'w') as file:
        json.dump(word_count, file)
censor_json("files/London.txt")

def censor_csv(filename: str):
    """
    filename:
    :param filename
    :return:
    """
    with open(filename, 'rt') as file:
        text = file.read()
    stat = {}
    word_count = {}
    for word in text.split():
        word = word.lower().strip('\n').replace(",", "").replace(".", "").replace(":", "").replace("'", "").replace(
            "\n", " ")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count)


    with open("files/London.stat.csv", 'wt') as file:
        writer = csv.writer(file)
        writer.writerow(word_count)
        for word, count in stat.items():
            writer.writerow([word, count])

censor_csv("files/London.txt")



