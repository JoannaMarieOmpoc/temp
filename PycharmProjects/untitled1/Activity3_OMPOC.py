wordlist = list()
temp = list()

while True:
    content = raw_input("Enter words: ")
    if content == 'end':
        break
    word = str(content)
    wordlist.append(word)
print "You have entered the following words: ",wordlist,"\n"


print "The words whose first letter occurs again within the word is: "

for i in range(len(wordlist)):
    for j in range(len(wordlist[i])):
        firstL = wordlist[i][:1]
        nextL = wordlist[i][j+1:j+2]
        if firstL == nextL:
            print wordlist[i]