# functions to convert numbers to binary or decimal
# used in conjuntion with NumberConverter.py front-end script


def decToBinary(dNum, bRunningTotal):
    quotient, rem = divmod(dNum, 2)
    #print(quotient, rem)

    if rem == 0:
        bRunningTotal.insert(0, '0')
    elif rem > 0:
        bRunningTotal.insert(0, '1')
    print('running total = ' + ''.join(bRunningTotal))

    if quotient == 0:
        print('binary conversion:')
        print(''.join(bRunningTotal))
        return str(''.join(bRunningTotal))
    else:
        return decToBinary(quotient, bRunningTotal)



def binaryToDec(bNum, dRunningTotal):
    # handle non binary entry
    for i in bNum:
        if i != '1' and i != '0':
            return None

    bNum.reverse()
    for i, v in enumerate(bNum):
        print(i, v, end=' ')
        print(int(v)*2**i)
        dRunningTotal.append(int(v)*2**i)
    x = sum(dRunningTotal)
    print('decimal conversion:\n' + str(x))
    return x

