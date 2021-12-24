import random

def scrambled_words (string_seq):
    punctutation = (",",".",";","!","?")
    count = 0
    new_word = []
    new_scrambled_word=""

    words_list=[words for words in string_seq.split()]
    words_scrambled_list=[]
    for word in words_list:
        
        if len(word)<= 3:
            words_scrambled_list.append(word)
        elif word[-1] in (punctutation):
            word1 = word[1:-2]
            
            word1 = random.sample(word1,len(word1))
            word1.insert(0,word[0])
            word1.append(word[-2])
            word1.append(word[-1])
            for i in word1:
                new_scrambled_word+=i 
            
            words_scrambled_list.append(new_scrambled_word)
            new_scrambled_word=""

        else:
            word1 = word[1:-1]
            word1 = random.sample(word1,len(word1))
            word1.insert(0,word[0])
            word1.append(word[-1])
            new_word = new_word +word1
            for i in word1:
                new_scrambled_word += i
            words_scrambled_list.append(new_scrambled_word)
            new_scrambled_word=""
    return words_scrambled_list

string_seq = input("Enter the Sentence to get Scramble Sentence:")
result=scrambled_words(string_seq)
final_result = ''
for word in result:
    final_result+= word + " "
print(final_result)