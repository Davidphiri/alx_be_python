# Global conversion factors (constants) for the temperature conversion
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9    # Factor to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5    # Factor to convert Celsius to Fahrenheit
FAHRENHEIT_OFFSET = 32                  # Fahrenheit offset (from Celsius to Fahrenheit)
CELSIUS_OFFSET = 0                     # Celsius offset (from Fahrenheit to Celsius)

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Use the global conversion factor for Fahrenheit to Celsius
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Use the global conversion factor for Celsius to Fahrenheit
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

# User interaction
def main():
    try:
        # Ask the user for the temperature value
        temp = float(input("Enter the temperature to convert: "))

        # Ask the user whether the input temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Convert and display the result based on the user's choice
        if unit == "F":
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        elif unit == "C":
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Handle non-numeric input
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
