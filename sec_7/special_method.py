class Word(object):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'WORD!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()


w = Word('test')
# print(w)
# print(len(w))
# print(len(w.text))
w2 = Word('test')

print(w + w2)
print(w == w2)

print(id(w))
print(id(w2))
