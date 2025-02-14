def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num)[2:].upper()

def binary_to_hexadecimal(binary_str):
    decimal_num = binary_to_decimal(binary_str)
    hexadecimal_str = decimal_to_hexadecimal(decimal_num)
    return hexadecimal_str

# Пример использования:
binary_number = input("Введите двоичное число: ")
hexadecimal_number = binary_to_hexadecimal(binary_number)
print(f"Шестнадцатеричное представление: {hexadecimal_number}")