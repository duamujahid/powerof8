def is_power_of_8(num):
    if num <= 0:
        return False
    return (num & (num - 1)) == 0 and (num & 0x924924924) != 0

num = int(input("Enter a number: "))

if is_power_of_8(num):
    print(num, "is a power of 8.")
else:
    print(num, "is not a power of 8.")
