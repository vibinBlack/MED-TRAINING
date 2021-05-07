
def is_Bigstr2(bigString,smallString,startIdx): 

    leftBigIdx = startIdx 

    rightBigIdx = startIdx + len(smallString) - 1

    leftSmallIdx = 0

    rightSmallIdx = len(smallString) - 1

  

    while (leftBigIdx <= rightBigIdx):         #iterate until leftBigIdx variable reaches <= rightBigIdx 

        if (bigString[leftBigIdx] != smallString[leftSmallIdx] or 

            bigString[rightBigIdx] != smallString[rightSmallIdx]): 

            return False

  

        leftBigIdx += 1

        rightBigIdx -= 1

        leftSmallIdx += 1

        rightSmallIdx -= 1

    return True


def is_Bigstr1(bigString, smallString): 

    for i in range(len(bigString)):                  # iterating in the bigstring  

        if (i + len(smallString) > len(bigString)):     #  condition when smallString is not available after 'i'th position

            break                                    

        if (is_Bigstr2(bigString, smallString, i)): 

            return True

    return False



def multi_str(bigString, smallStrings): 

    solution = []                                   #  storing list for boolean entries

    for smallString in smallStrings: 

         solution.append(is_Bigstr1(bigString, smallString)) 

    return solution




def test_01():
    str1 = "this is a big string"
    substr = ["this", "not", "a", "small", "string", "kappa"] 
    assert [True, False, True, False, True, False] == multi_str(str1, substr) 


#print(multi_str(str1,str2)); 
def test_02():
    str1 ="optival medplus training"
    str2=["medplus","customfur","training","medplus"]
    assert [True, False, True, True]  == multi_str(str1,str2)


    
