def safe_divide(numerator, denominator):
    """Performs division while handling division by zero and non-numeric inputs."""
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        # Handle case where inputs cannot be converted to floats
        return "Error: Both numerator and denominator must be numeric values."
    
    try:
        # Perform the division and return the result
        result = numerator / denominator
        return f"Result: {result:.2f}"
    except ZeroDivisionError:
        # Handle division by zero error
        return "Error: Division by zero is not allowed."