word = input("please enter a string")
word2 = ""
word3 = ""
for character in word :
    if character.islower():
        word2 += character
    elif character.isupper():
        word3 += character

print(word2 + word3)