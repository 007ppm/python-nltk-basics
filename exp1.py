from nltk.tokenize import sent_tokenize, word_tokenize
eg="hello ppm, how are u buddy ? how's todays weather? Im so bored."
print(sent_tokenize(eg)) 
print(word_tokenize(eg))

print("\n\n\n\ TO VIEW IN A PROPER LIST : \n\n")

for i in word_tokenize(eg):
    print(i)
