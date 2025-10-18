def print_fibo(n):
    output_list = []
    if n == 0:
        return None
    elif n == 1:
        return 1
    elif n>1:
        a, b = 0, 1
        for _ in range(n):
            output_list.append(a)
            a, b = b, a+b
    return output_list

print(print_fibo(10))


