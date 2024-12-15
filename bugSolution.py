def improved_function(x):
    try:
        if isinstance(x, (int, float)):
            if x == 0:
                return "Division by zero"
            else:
                return 1 / x
        elif isinstance(x, list):
            return "Error: Input must be a number, not a list"
        else:
            return "Error: Invalid input type"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# This will now gracefully handle list inputs
print(improved_function(2))  # Output: 0.5
print(improved_function(0))  # Output: Division by zero
print(improved_function([1, 2, 3]))  # Output: Error: Input must be a number, not a list