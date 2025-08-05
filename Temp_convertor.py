try:
    temp = float(input("Enter the temperature: "))
    Unit = input("Either Celsius or Fahrenheit (C or F): ").lower()

    if Unit == "c":
        converted = round((9 * temp) / 5 + 32, 1)
        print(f"The temperature in Fahrenheit: {converted}°F")
    elif Unit == "f":
        converted = round((temp - 32) * 5 / 9, 1)
        print(f"The temperature in Celsius: {converted}°C")
    else:
        print(f"'{Unit}' isn't a valid unit (use 'C' or 'F')")
except ValueError:
    print("Enter a valid number for temperature.")