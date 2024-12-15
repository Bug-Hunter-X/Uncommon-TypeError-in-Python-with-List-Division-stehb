def function_with_uncommon_error(x):
    try:
        result = 1 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

#This works as expected
print(function_with_uncommon_error(2)) #Output: 0.5
print(function_with_uncommon_error(0)) #Output: Division by zero

#This shows an uncommon error that happens when passing a list
print(function_with_uncommon_error([1,2,3])) #Output: TypeError: unsupported operand type(s) for /: 'int' and 'list'