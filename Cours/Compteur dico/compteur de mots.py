with open("ndparis.txt", "r", encoding="UTF-8") as paris: phrase = paris.read()
mots = {}
for word in phrase.split():
    word = word.lower().strip()
    if word in mots:mots[word] += 1
    else:mots[word] = 1
print(mots); print(max(mots, key=mots.get),":", mots[max(mots, key=mots.get)])