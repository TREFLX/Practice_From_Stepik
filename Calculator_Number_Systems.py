actual_number = int(input("Введите число:"))

def convert(actual_number):
    bin_num = bin(actual_number)  # 0b1111111
    oct_num = oct(actual_number)  # 0o177
    hex_num = hex(actual_number)  # 0x7f

    print(bin_num[2:])  # 1111111
    print(oct_num[2:])  # 177
    print(hex_num[2:].upper())

convert(actual_number)