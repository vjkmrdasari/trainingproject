def generate_anagrams(word):
    anagram_list = []
    def backtrack(path,remaining):
        if not remaining:
            anagram_list.append(path)
            return
        for i in range(len(remaining)):
            backtrack(path+remaining[i],remaining[:i]+remaining[i+1:])

    backtrack("",word)
    print(len(anagram_list))
    return anagram_list
word = 'abc'
print(generate_anagrams(word))
