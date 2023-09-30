
# functions to convert numbers to binary, decimal or hex
# used in conjuntion with NumberConverter.py front-end script


hexTable = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

# convert Decimal to Binary
# takes an int and an empty list
def decToBinary(dNum, bRunningTotal):
    quotient, rem = divmod(dNum, 2)
    #print(quotient, rem)

    if rem == 0:
        bRunningTotal.insert(0, '0')
    elif rem > 0:
        bRunningTotal.insert(0, '1')
    #print('running total = ' + ''.join(bRunningTotal))

    if quotient == 0:
        #print(''.join(bRunningTotal))
        return str(''.join(bRunningTotal))
    else:
        return decToBinary(quotient, bRunningTotal)



# convert Binary to Decimal 
# takes an int and an empty list
def binaryToDec(bNum, dRunningTotal):
    bNum = list(str(bNum))

    # handle non binary entry
    for i in bNum:
        if i != '1' and i != '0':
            return 'please enter a binary number' #None

    bNum.reverse()
    for i, v in enumerate(bNum):
        # print(i, v, end=' ')
        # print(int(v)*2**i)
        dRunningTotal.append(int(v)*2**i)
    x = sum(dRunningTotal)
    return x



# convert Decimal to Hexadecimal
# takes an int and an empty list
def decToHex(dNum, hRunningTotal):
    quotient, rem = divmod(dNum, 16)
    if quotient == 0:
        hRunningTotal.append(rem)
        print(f'{hRunningTotal}')

        hRunningTotal.reverse()
        output = []
        for i in hRunningTotal:
            if i not in hexTable:
                output.append(i)
            else:
                output.append(hexTable[i])
        print(output)
        return ''.join(str(x) for x in output)
    else:
        hRunningTotal.append(rem)
        print(hRunningTotal)
        return decToHex(quotient, hRunningTotal)
    


# convert Hexadecimal to Decimal 
# takes a string and an empty list
def hexToDec(hNum, runningTotal):
    digits = list(hNum) # break down the hex value
    exp = [] # to hold the descending exponent values
    for i in range(len(digits)):
        exp.append(i)
    exp.reverse()

    # print(f'digits {digits}')
    # print(f'exp {exp}')

    for i in range(len(exp)):
        if digits[i] in hexTable.values():
            conv = [k for k, v in hexTable.items() if v == digits[i]]
            runningTotal.append(conv[0]*16**exp[i])
        else:
            #print(int(digits[i]))
            runningTotal.append(int(digits[i])*16**exp[i])
    
    print(runningTotal)
    total=sum(runningTotal)
    return total



# convert Hexadecimal to Binary
# takes a string and an empty list
# makes use of hexToDec() & decToBinary() 
def hexToBinary(hNum, runningTotal):
    h2d = hexToDec(hNum, runningTotal)
    runningTotal = []
    d2b = decToBinary(h2d, runningTotal)
    return d2b



# convert Binary to Hexadecimal
# takes an int and an empty list
# makes use of binaryToDec() & decToHex() 
def binToHex(bNum, runningTotal):
    b2d = binaryToDec(bNum, runningTotal)
    runningTotal = []
    d2h = decToHex(b2d, runningTotal)
    return d2h






