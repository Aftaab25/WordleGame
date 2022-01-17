import random

file1 = open('words.txt', 'r',encoding="utf8", errors='ignore')
Lines = file1.readlines()
 
# words[]: This list will store all our 5-letter words for the game
words = []

# Strips the newline character and the spaces (if there are any)
for line in Lines:
  word = line.strip()
  if len(word) == 5 and (word not in words):
    word = word.lower() # Only lower characters are allowed
    words.append(word)

# Removing any character that is not alphabet
for i in range(len(words)):
  for j in words[i]:
    if ord(j) < 97 or ord(j) > 122:
      words[i] = words[i].replace(j, '')

#print(words)
#print(len(words))

# Picking a random word from the list of words
print(words[random.randint(0, len(words)-1)])

# displayed[]: will store all the displayed words to avoid repeatation of 
# words.
displayed = []
