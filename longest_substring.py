def longest_unique_substring(s):
  char_set = set()
  start = 0
  max_len = 0
  max_substring = ""

  for end in range (len(s)):
    while s[end] in char_set:
      char_set.remove(s[start])
      start += 1
    char_set.add(s[end])

    if end - start + 1 >max_len:
      max_len = end - start + 1
      max_substring = s[start:end+1]
  return max_len,max_substring

s = "abcabcbb"
length, substring = longest_unique_substring(s)
print("Length:", length)
print("Substring:", substring)