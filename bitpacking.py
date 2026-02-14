def pack_bits(num1, num2):
    print(f"\n\nOriginal bits: {num1:08b}")
    num1 = num1 << 4 # Shift the bits by 4 positions
    print(f"Shifted bits: {num1:08b}")
    print(f"Num2 bits: {num2:08b}")
    num1 = num1 | num2
    print(f"packed bits: {num1:08b}")
    return num1.item()