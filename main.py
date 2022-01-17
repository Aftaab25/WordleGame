file1 = open('words.txt', 'r',encoding="utf8", errors='ignore')
Lines = file1.readlines()
 
words = []
# Strips the newline character
for line in Lines:
  word = line.strip()
  if len(word) == 5 and (word not in words):
    word = word.lower()
    words.append(word)
for i in range(len(words)):
  for j in words[i]:
    if ord(j) < 97 or ord(j) > 122:
      words[i] = words[i].replace(j, '')
print(words)
print(len(words))
