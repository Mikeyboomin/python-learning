def number_triangle(n):
    if not isinstance(n, int):
        return "Argument must be an integer."
    elif n < 1:
        return "Argument must be greater than 0."
    else:
        result = ''
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                result += str(j)

                if j != i:
                    result += " "
            if i != n:
                result += "\n"
        return result
    
print(number_triangle(4))