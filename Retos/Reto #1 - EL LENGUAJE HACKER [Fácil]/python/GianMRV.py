char = {
    "A": "4",
    "B": "I3",
    "C": "[",
    "D": ")",
    "E": "3",
    "F": "|=",
    "G": "&",
    "H": "#",
    "I": "1",
    "J": ",_|",
    "K": ">|",
    "L": "1",
    "M": "/\\/\\",
    "N": "^/",
    "O": "0",
    "P": "|*",
    "Q": "(_,)",
    "R": "I2",
    "S": "5",
    "T": "7",
    "U": "(_)",
    "V": "\/",
    "W": "\/\/",
    "X": "><",
    "Y": "j",
    "Z": "2",
  }

word = 'Yo soy Iron Man'
word_listed = list(word)
encrypted = ''

for i in (word_listed):
    if i == ' ':
        encrypted += i
        continue
    encrypted += char[i.upper()]

print('From:','\'', word, '\'', 'to:', '\'', encrypted, '\'')