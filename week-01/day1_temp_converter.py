celcius = float(input("Enter temperature in Celsius: "))

def convert():
    result = round((celcius * 1.8) + 32, 2)
    print("Value in Fahrenheit is: " + str(result))

convert()