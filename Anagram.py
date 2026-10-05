word1 = input("Enter word1: ")
word2 = input("Enter word2: ")

if sorted(word1) == sorted(word2):
    print("The words are Anagrams")
else:
    print("The words are not Anagrams")
