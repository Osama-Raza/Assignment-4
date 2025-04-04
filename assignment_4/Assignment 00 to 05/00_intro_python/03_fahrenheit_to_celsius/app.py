fahrenheit  = float (input('Enter a temperature in fahrenheit: '))
print(f'Temperature: {fahrenheit}F')

celsius = (fahrenheit - 32) * 5.0/9.0
print(f'Temperature:{celsius: .2f}C')