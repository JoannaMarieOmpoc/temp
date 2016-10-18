
word = list()
wordList = list()

def isPalindrome(thisword):
    count = 0
    inverse = thisword[::-1]
    if thisword == inverse:
        print("\nTrue")
        wordList.append(thisword)
    else:
        wordList.remove(thisword)
        for i in range(len(thisword)):
            count = count + 1
        print ("\nFalse")
        print("Total number of letters of non palindrome word: ", count)


while True:
    while True:
        letters = raw_input("Enter each letters of the word: ")
        if letters == 'end':
            break
        content = str(letters.lower())
        word.append(content)

    isPalindrome(word)
    print "\n", wordList

    again = raw_input("Enter another word?<1-yes, 0-no>: ")
    if again == '0':
        break

