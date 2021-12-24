def ones_compliment(binary_number):
    string_res=""
    for i in range(len(binary_number)):
        if binary_number[i] == "0":
            ones_num = 1
            string_res+=str(ones_num)

        else:
            ones_num = 0 
            string_res+= str(ones_num)

    return string_res 


def twos_compliment(binary_number):
    for i in range(len(binary_number)-1,-1,-1):
        if binary_number[i]=='1':
            m = i 
            break 
    ones_comp = ones_compliment(binary_number[:m])

    return ones_comp+binary_number[m:]
        

number = input("Enter the Binary Number :")
result_ones=ones_compliment(number)
print(result_ones)
result_twos = twos_compliment(number)
print(result_twos)
