import random

def scrambled(given):
    n = len(given)
    
    if len(given) <= 3:
        return given
    else:
        given  = list(given)
        
        spl_chars = [',','.','?','!',';','_',':']
        spl_store = dict()
        first = ''
        last = ''
        for i in range(len(given)):
            if given[i] in spl_chars:
                spl_store[i] = given[i] 
            if given[i] not in spl_chars and first == '':
                first_ind = i
                first = given[i]
                #print(f"First :{first} {first_ind}")
        for i in range(len(given)-1,-1,-1):
            if given[i] not in spl_chars and last == '':
                last_ind = i
                last = given[i]
                #print(f"Last :{last} {last_ind}")
        given.remove(first)
        given.remove(last)
        for i in spl_store.keys():
            given.remove(spl_store[i])
            
        random.shuffle(given)
        #print(spl_store)
        
        given.insert(0,first)
        given.insert(len(given),last)
        for i in spl_store.keys():
            given.insert(i,spl_store[i])
        v = ''.join(given)
        return v
        
        
            
    
        
        

given = input("Enter the sentence to be scrambled: ")
final = list()
lib = given.split()
for item in lib:
    final.append(scrambled(item))
print(" ".join(final))