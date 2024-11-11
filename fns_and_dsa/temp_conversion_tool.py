# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main user interaction
def main():
    try:
        # Ask the user to input a temperature value and unit
        temp_input = input("Enter a temperature (e.g., 32C or 100F): ").strip()
        
        # Check if the input ends with 'C' or 'F' for Celsius or Fahrenheit
        if temp_input[-1].upper() == 'C':
            # Extract the numeric part of the input and convert it to Celsius
            celsius_value = float(temp_input[:-1])
            fahrenheit_value = convert_to_fahrenheit(celsius_value)
            print(f"{celsius_value}°C is equal to {fahrenheit_value:.2f}°F")
        elif temp_input[-1].upper() == 'F':
            # Extract the numeric part of the input and convert it to Fahrenheit
            fahrenheit_value = float(temp_input[:-1])
            celsius_value = convert_to_celsius(fahrenheit_value)
            print(f"{fahrenheit_value}°F is equal to {celsius_value:.2f}°C")
        else:
            # Raise an error if the temperature unit is not valid
            raise ValueError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        # Handle invalid temperature input (non-numeric or invalid unit)
        print(f"Error: {e}. Please enter a numeric value followed by 'C' or 'F'.")

if __name__ == "__main__":
    main()
