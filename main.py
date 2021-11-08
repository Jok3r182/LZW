
def intToBinary(list):
    return ''.join(bin(code) for code in list)


def stringToBinary(list):
    return ''.join(bin(ord(char)) for char in list)


def compareBits(withCompression, withoutCompression):
    return len(withoutCompression) - len(withCompression)


def LZWCompression(input):
    dict_size = 256

    # utf-16 chr mes istatydami sk gauname raide, gauname dictionary a:97 tarkim, jog paskui pagal
    # turima value galetume priskirti reiksme

    dictionary = dict((chr(i), i) for i in range(dict_size))
    string = ""
    result = []
    print("Input\tNext\tOutput\tDictionary")
    for char in input:
        phrase = string + char
        # ar fraze yra arba raide
        if phrase in dictionary:
            string = phrase
        else:
            result.append(dictionary[string])
            # sukuriame dictioneryje reiksme su size, nes tokia value neegzistuoja
            dictionary[phrase] = dict_size
            dict_size += 1
            print(string + "\t\t" + char + "\t\t" + string + "\t\t" + phrase)
            string = char
    if string:
        #paskutiniai raidei prideti nes visada pridedavome viena maziau pries tai tarkim kai buvo ma mes idedavome m
        result.append(dictionary[string])
        withCompression = intToBinary(result)
        withoutCompression = stringToBinary(input)
        print("\nWithout Compression = " + withoutCompression)
        print("With Compression = " + withCompression)
        print("Difference = " + str(compareBits(withCompression, withoutCompression)) + " bits\n")

    return result


if __name__ == '__main__':
    print(LZWCompression("Matas Paulius Dregva"))
