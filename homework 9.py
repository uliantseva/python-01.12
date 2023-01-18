def censor(filename: str):
    with open(filename, 'rt') as file:
        data = file.read()
        return data
li = ['London', 'is', 'city']
text = censor("files/London.txt")
for i, j in li:
    text = text.replace(i, j)
print(text)



















