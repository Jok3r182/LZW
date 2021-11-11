def intToBinary(result):
    return ''.join(bin(code) for code in result)


def stringToBinary(result):
    return ''.join(bin(ord(char)) for char in result)


def compareBits(with_compression, without_compression):
    return len(without_compression) - len(with_compression)


def LZWCompression(user_input):
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    temp_dictionary = ""
    result = []
    print("Input\tNext\tOutput\tDictionary")
    for char in user_input:
        phrase = temp_dictionary + char
        if phrase in dictionary:
            temp_dictionary = phrase
        else:
            result.append(dictionary[temp_dictionary])
            dictionary[phrase] = dict_size
            dict_size += 1
            print(temp_dictionary + "\t\t" + char + "\t\t" + temp_dictionary + "\t\t" + phrase)
            temp_dictionary = char

    if temp_dictionary:
        result.append(dictionary[temp_dictionary])
        withCompression = intToBinary(result)
        withoutCompression = stringToBinary(user_input)
        print("\nWithout Compression = " + withoutCompression)
        print("With Compression = " + withCompression)
        print("Difference = " + str(compareBits(withCompression, withoutCompression)) + " bits\n")

    return result


if __name__ == '__main__':
    print(LZWCompression("Matas Paulius Dregva"))
