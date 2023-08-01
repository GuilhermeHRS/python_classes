"""
Q 1: Write a Python program to print "Hello, World!"
Q 2: Calculate the sum of two numbers entered by the user.
Q 3: Convert temperature from Celsius to Fahrenheit.
"""
#1
print("Hello, World!")

#2
a = int(input("Escreva um número de 0 a 9: "))
b = int(input("Escreva outro número número de 0 a 9: "))
soma = a + b
print(f"A soma de {a} com {b} = {soma}")

#3
celcius = float(input("Escreva a temperatura em C°: "))
fahrenheit = (celcius * 1.8) + 32

print(f"C°{celcius} equivale a F°{round(fahrenheit, 2)}")



