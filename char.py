word = input('enter a word or phrase: ')
char = input('enter the character you want to find: ')
i = 0
count = 0

while i < len(word):
    if word[i] == char:
        count = count + 1
    i = i + 1

print("number of times", char, "has come up in this word/phrase are/is: ", count )