def safe_divide(numerator, denominator):
    """Safely divide two values with error handling."""
    try:
        # Convert to float
        num = float(numerator)
        den = float(denominator)

        # Attempt division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
