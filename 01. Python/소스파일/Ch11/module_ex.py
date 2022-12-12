import fah_converter

print("Enter a celsius value: ")
celsius = float(input())
fahrenheit = fah_converter.covert_c_to_f(celsius)
print("That's", fahrenheit, "degrees Fahrenheit.")
