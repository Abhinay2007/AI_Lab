def calculate_parity_bits(data_bits):
    r = 0
    while (2 ** r) < (data_bits + r + 1):
        r += 1
    return r


def generate_hamming(data):
    data_bits = len(data)
    parity_bits = calculate_parity_bits(data_bits)
    total_bits = data_bits + parity_bits

    # 1-indexed array
    code = [0] * (total_bits + 1)

    # Place data bits
    data_index = 0
    for position in range(1, total_bits + 1):
        # Positions that are not powers of 2 contain data
        if position & (position - 1):
            code[position] = data[data_index]
            data_index += 1

    # Calculate parity bits
    for p in range(parity_bits):
        position = 2 ** p
        parity = 0

        for i in range(1, total_bits + 1):
            if i & position:
                parity ^= code[i]

        code[position] = parity

    return code


def detect_error(code):
    total_bits = len(code) - 1
    error_position = 0

    parity_bits = calculate_parity_bits(total_bits)

    for p in range(parity_bits):
        position = 2 ** p
        parity = 0

        for i in range(1, total_bits + 1):
            if i & position:
                parity ^= code[i]

        if parity:
            error_position += position

    return error_position


# ---------------- MAIN PROGRAM ----------------

print("HAMMING CODE - ASCII ERROR DETECTION AND CORRECTION")

bits = int(input("Enter ASCII size (7 or 8): "))

if bits not in [7, 8]:
    print("Invalid choice. Enter 7 or 8.")
    exit()

character = input("Enter an ASCII character: ")

if len(character) != 1:
    print("Please enter exactly one character.")
    exit()

ascii_value = ord(character)

# Check ASCII range
if bits == 7 and ascii_value > 127:
    print("Character cannot be represented using 7-bit ASCII.")
    exit()

if bits == 8 and ascii_value > 255:
    print("Character cannot be represented using 8 bits.")
    exit()

# Convert ASCII value to binary
binary = format(ascii_value, f"0{bits}b")

print("\nASCII value:", ascii_value)
print("Data bits:  ", binary)

# Convert binary string to list of integers
data = [int(bit) for bit in binary]

# Generate Hamming code
code = generate_hamming(data)

print("Hamming code:",
      ''.join(str(code[i]) for i in range(len(code) - 1, 0, -1)))

# Introduce an error
error_position = int(
    input(f"\nEnter bit position to corrupt (1-{len(code)-1}, 0 for no error): ")
)

if error_position < 0 or error_position >= len(code):
    print("Invalid position.")
    exit()

if error_position != 0:
    code[error_position] ^= 1

    print("Corrupted code:",
          ''.join(str(code[i]) for i in range(len(code) - 1, 0, -1)))

# Detect error
detected_position = detect_error(code)

if detected_position == 0:
    print("\nNo error detected.")
else:
    print("\nError detected at bit position:", detected_position)

    # Correct the error
    code[detected_position] ^= 1

    print("Corrected Hamming code:",
          ''.join(str(code[i]) for i in range(len(code) - 1, 0, -1)))

print("\nProgram completed.")