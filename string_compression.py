def string_compression(string):
    result = []
    count = 1
    output = ""
    for char in range(1,len(string)):
        if string[char] == string[char-1]:
            count += 1

        else:
            result.append(string[char-1])
            result.append(str(count))
            count = 1
    result.append(string[-1])
    result.append(count)
    for ch in result:
        output += str(ch)


    return output
print(string_compression("aaabcbbbdccce"))