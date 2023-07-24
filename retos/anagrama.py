def anagrama(word1,word2):
    if word1 == word2:
        return False
    return sorted(word1.lower()) == sorted(word2.lower())

result = anagrama("gota","gato")   
print(result) 

#sorted ordena el string de mandera alfabetica
