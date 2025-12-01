word1 = input("Въведете първата дума: ").lower()
word2 = input("Въведете втората дума: ").lower()

sorted_word1 = sorted(word1)
sorted_word2 = sorted(word2)
if sorted_word1 == sorted_word2:
    print("Думите са анаграми")