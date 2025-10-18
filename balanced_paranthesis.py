def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}  # closing → opening

    for char in s:
        if char in mapping:  # closing bracket
            top = stack.pop() 
            if mapping[char] != top:  # mismatch
                return False
        else:  # opening bracket
            stack.append(char)

    return not stack  # stack must be empty
print(is_valid_parentheses("{[(])}"))