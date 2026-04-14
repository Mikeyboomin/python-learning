def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    elif n < 1:
        return "Argument must be an integer greater than 0."
    else:
        result = ""
        for number in range(1, n + 1):
            if number == n:
                result += str(number)
            else:
                result += str(number) + " "
        return result
    
print(number_pattern(4))