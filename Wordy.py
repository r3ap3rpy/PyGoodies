import re

WORDS = re.compile(r'\w+')

class WordyClass:
    def __init__(self, text):
        self.text = text
        self.words = WORDS.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __str__(self):
        return f"WordyClass(text = {self.text})"

class WordyGen:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word
    def __iter__(self):
        return self

with open('loremipsum.txt') as file:
    text_words = WordyClass(file.read())

print(text_words.words)
print(len(text_words))

genwords = WordyGen(text_words.words)
print(genwords)
for word in genwords:
    print(word)
