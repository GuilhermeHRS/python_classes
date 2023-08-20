def celsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

# input_user = float(input("Escreva a temperatura em C°: "))
# fahrenheit_value = celsius_to_fahrenheit(input_user)
# print(f"C°{input_user} equivale a F°{round(fahrenheit_value, 2)}")

temperaturas_fahrenheit = []

while True:
    try:
        input_str = input("Escreva a temperatura em °C (ou digite 'exit' para sair): ")
        if input_str.lower() == 'exit':
            break
        temperatura_celsius = float(input_str)
        fahrenheit = celsiusToFahrenheit(temperatura_celsius)
        temperaturas_fahrenheit.append(fahrenheit)
    except ValueError:
        print("Por favor, insira um número válido ou 'exit' para sair.")

print("Temperaturas em Fahrenheit inseridas:", temperaturas_fahrenheit)
