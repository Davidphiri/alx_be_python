# robust_division_calculator.py
def safe_divide(numerator, denominator):
    """Perform safe division, handling errors for division by zero and non-numeric inputs."""
    try:
        # Attempt to convert input to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division
        result = numerator / denominator
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
