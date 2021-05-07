
def is_Bigstr2(bigString,smallString,startIdx): 

    leftBigIdx = startIdx 

    rightBigIdx = startIdx + len(smallString) - 1

    leftSmallIdx = 0

    rightSmallIdx = len(smallString) - 1

  

    while (leftBigIdx <= rightBigIdx): 

        if (bigString[leftBigIdx] != smallString[leftSmallIdx] or 

            bigString[rightBigIdx] != smallString[rightSmallIdx]): 

            return False

  

        leftBigIdx += 1

        rightBigIdx -= 1

        leftSmallIdx += 1

        rightSmallIdx -= 1

    return True


def is_Bigstr1(bigString, smallString): 

    for i in range(len(bigString)):   

        if (i + len(smallString) > len(bigString)): 

            break

        if (is_Bigstr2(bigString, smallString, i)): 

            return True

    return False



def multi_str(bigString, smallStrings): 

    solution = []

    for smallString in smallStrings: 

         solution.append(is_Bigstr1(bigString, smallString)) 

    return solution


str1 = "this is a big string"
substr = ["this", "not", "a", "small", "string", "kappa"] 

assert [True, False, True, False, True, False] == multi_str(str1, substr) 

str1 ="optival medplus training"
str2=["medplus","customfur","training","medplus"]

#print(multi_str(str1,str2)); 

assert [True, False, True, True]  == multi_str(str1,str2)


    
