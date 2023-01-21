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
def fun_words_count(filename: str):
    """
    fun_words_count
    :param filename:
    :return:
    """
    with open(filename, 'rt') as file:
        text = file.read()
        print(text)
    words_dict = dict()
    text = ("files/London.txt")
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace(":", "").replace("'", "")
    text = text.casefold()
    text = text.lower()
    words = text.split()
    words.sort()
    print(words)
    print(f"Кол-во слов: {len(words)}")
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict
















