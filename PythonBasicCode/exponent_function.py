def raise_to_power(base_num, power_num):
    result = 1
    for num in range(power_num):
        result = result * base_num
    return result

print(raise_to_power(2,5))