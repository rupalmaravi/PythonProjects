# From a given array , create 2 arrays with even and odd number
# Get sum of all odd and even  numbers from array
lucky_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_number = []
even_number = []
odd_number_sum = 0
even_number_sum = 0
for n in lucky_numbers:
    if n % 2 != 0:
        odd_number.append(n)
        odd_number_sum += n
    else:
        even_number.append(n)
        even_number_sum += n

print("Odd numbers from the array - ", odd_number)
print("Even Numbers from the array - ", even_number)
print("Sum of all odd numbers - ", odd_number_sum)
print("Sum of all odd numbers - ", even_number_sum)
