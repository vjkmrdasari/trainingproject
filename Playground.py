def is_valid_parentheses(s):
    stack = []
    mapping = {']':'[' , '}':'{' , ')':'('}

    for char in s:
        if char in mapping:
            top = stack.pop()
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack

print(is_valid_parentheses("{[]}"))
#this was done in github
