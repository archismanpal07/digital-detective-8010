"""Convert a positive decimal integer to binary and hexadecimal."""

raw_value = input("Enter a positive decimal integer: ")

try:
    number = int(raw_value)
except ValueError:
    raise SystemExit("Please enter a whole number.")

if number <= 0:
    raise SystemExit("Please enter a positive integer greater than zero.")

binary_value = bin(number)[2:]
hexadecimal_value = hex(number)[2:].upper()

print(f"Decimal: {number}")
print(f"Binary: {binary_value}")
print(f"Hexadecimal: {hexadecimal_value}")
