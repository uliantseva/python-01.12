def censor(filename: str):
    with open(filename, 'rt') as file:
        data = file.read()
        return data
li = ['London', 'Parliament', 'city']
text = censor("files/London.txt")
text = text.replace("London", "*" * len("London"))
text = text.replace("Parliament", "*" * len("Parliament"))
text = text.replace("city", "*" * len("city"))
with open("files/London.txt", "wt") as file:
    file.write(text)
print(text)


















