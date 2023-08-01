
#1 - Write a Python program to calculate the area of a rectangle given its length and width

# length = float(input("Escreva a altura: "))
# width = float(input("Escreva a largura: "))
# area = length * width

# print(f"A area do retângulo é equivalente a {area}")

#2 - Create a program that takes a user's name and age as input and prints a greeting message

# import random

# name = str(input("Escreva o seu nome: ")).capitalize()
# yo = int(input("Escreva a sua idade: "))
# greetings = [
#     "Olá, seja bem-vindo",
#     "Oi, que bom te ver por aqui",
#     "Olá, é um prazer conhecê-lo",
#     "Oi, como vai?",
#     "Olá, espero que seu dia seja ótimo",
#     "Olá, é uma honra tê-lo(a) aqui",
#     "Oi, como posso ajudar?",
#     "Olá, que alegria encontrá-lo(a)",
#     "Oi, seja bem-vindo(a) ao nosso espaço",
#     "Olá, fico feliz em vê-lo(a)"
# ]

# print(f"{random.choice(greetings)} {name}! Você possui {yo} anos.")

#3 - Write a program to check if a number is even or odd+

# number = int(input("Escreva um número: "))
# if number % 2:
#     print("Ímpar!")
# else:
#     print("Par!")

#or --------

# def check_even_odd(number):
#     if number % 2 == 0:
#         print(f"{number} é um número par")
#     else:
#         print(f"{number} é um número ímpar")

# try:
#     user_input = int(input("Escreva um número: "))
#     check_even_odd(user_input)
# except ValueError:
#     print("Número inválido. Por gentileza insira um número válido!")

#4 - Given a list of numbers, find the maximum and minimum values.

# list_numbers = [0,1,2,3,4,5,6,7,8,9,10]
# min = min(list_numbers)
# max = max(list_numbers)

# print(f"Menor número {min}\nMaior número {max}")

#5 - Create a Python function to check if a given string is a palindrome

# def is_palindrome():
    #Remove spaces and convert to lowercase for case-insensitive comparison

#---------------------------- I have to do late 

#6 - Calculate the compound interest for a given principal amount, interest rate, and time period