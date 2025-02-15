def decimal_to_binary(n):
    return bin(n)[2:]  # Removes the '0b' prefix

# Example usage
decimal_number = int(input("Enter a decimal number: "))
binary_representation = decimal_to_binary(decimal_number)
print(f"Binary representation: {binary_representation}")