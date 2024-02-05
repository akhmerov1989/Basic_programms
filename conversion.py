kilometers = float(input("Enter the distance in km: "))
# Conversion factor: 1 km = 0.621371 miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor

print(f"{kilometers} kilometers is equal to {miles} miles")


celsius = float(input("Enter temperature in Celsius: "))

# Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
