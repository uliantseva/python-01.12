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

        for word in list_words:
            text = text.replace(word, '*' * len(word))
        print(text)
    with open("files/London 3.txt", "wt") as file:
        file.write(text)
censor("files/London.txt", ['London', 'Parliament', 'city'])

# 2
def words_count(filename):
    """
    words_count
    :param filename: "files/London.txt"
    :return:
    """
    with open(filename, 'rt') as file:
        text = file.read()
    word_count = {}

    for word in text.split():
        word = word.lower().strip('\n').replace(",", "").replace(".", "").replace(":", "").replace("'", "").replace("\n", " ")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(words_count("files/London.txt"))
















