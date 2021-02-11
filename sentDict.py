


sFile = open("sentences.txt", "r")

sentences = {}
key = 0
for sent in sFile: 
    sentences[key] = sent
    key += 1


