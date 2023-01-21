# 1
def censor(filename: str, list_words):

    """
    list_words = ['London', 'Parliament', 'city']
    filename: "files/London.txt"
    :param filename:
    :param list_words:
    :return:
    """

    with open(filename, 'rt') as file:
        text = file.read()
        print(text)
        for word in list_words:
            text = text.replace(word, '*' * len(word))
    with open("files/London 3.txt", "wt") as file:
        file.write(text)
censor("files/London.txt", ['London', 'Parliament', 'city'])

# 2
def fun_words(filename: str):
    """
    filename: "files/London.txt"
    :param filename:
    :return:
    """
    with open(filename, 'rt') as file:
        text = file.read()
        vocabulary = file.read()
        return vocabulary
        result = len(text.split())
        print(result)
















