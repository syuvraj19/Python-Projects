def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def miles_to_kilometers(miles):
    return miles * 1.60934

def kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

def main():
    while True:
        print("Unit Converter")
        print("1. Temperature")
        print("2. Length")
        print("3. Weight")
        print("4. Exit")
        choice = input("Choose a conversion type: ")

        if choice == '1':
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            temp_choice = input("Choose a temperature conversion: ")
            if temp_choice == '1':
                celsius = float(input("Enter temperature in Celsius: "))
                print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
            elif temp_choice == '2':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")
            else:
                print("Invalid choice.")

        elif choice == '2':
            print("1. Miles to Kilometers")
            print("2. Kilometers to Miles")
            length_choice = input("Choose a length conversion: ")
            if length_choice == '1':
                miles = float(input("Enter length in miles: "))
                print(f"{miles} miles is {miles_to_kilometers(miles)} kilometers")
            elif length_choice == '2':
                kilometers = float(input("Enter length in kilometers: "))
                print(f"{kilometers} kilometers is {kilometers_to_miles(kilometers)} miles")
            else:
                print("Invalid choice.")

        elif choice == '3':
            print("1. Pounds to Kilograms")
            print("2. Kilograms to Pounds")
            weight_choice = input("Choose a weight conversion: ")
            if weight_choice == '1':
                pounds = float(input("Enter weight in pounds: "))
                print(f"{pounds} pounds is {pounds_to_kilograms(pounds)} kilograms")
            elif weight_choice == '2':
                kilograms = float(input("Enter weight in kilograms: "))
                print(f"{kilograms} kilograms is {kilograms_to_pounds(kilograms)} pounds")
            else:
                print("Invalid choice.")

        elif choice == '4':
            print("Exiting the converter.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
