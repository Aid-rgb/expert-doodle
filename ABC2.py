import struct

def calculate_power_ieee754(value, power):
    value_bytes = struct.pack('d', value)
    value_int = int.from_bytes(value_bytes, byteorder='big')

    sign_bit = (value_int >> 63) & 0x1
    exponent_part = ((value_int >> 52) & 0x7FF) - 1023
    fraction_part = 1 + (value_int & 0xFFFFFFFFFFFFF) / (1 << 52)

    result_value = pow(-1 if sign_bit else 1, power) * pow(fraction_part, power) * pow(2, exponent_part * power)

    result_bytes = struct.pack('d', result_value)
    result_int = int.from_bytes(result_bytes, byteorder='big')

    return result_value

input_number = 2.0
exponent_value = 2
output_result = calculate_power_ieee754(input_number, exponent_value)

print(f"Result: {output_result}")

expected_result = input_number ** exponent_value
print(f"Expected Result: {expected_result}")
print(f"Difference: {abs(output_result - expected_result)}")