numbers_list = list(range(2, 11, 2))

reverse_number_list = sorted(numbers_list, reverse=True)

#for number in reverse_number_list:
#   print(number)

squares = []

large_numbers = list(range(1, 1_000_001))

print(min(large_numbers))
print(max(large_numbers))
print(sum(large_numbers))

small_numbers = list(range(1, 6))

print(min(small_numbers))
print(max(small_numbers))
print(sum(small_numbers))

odd_numbers = list(range(1,21,2))

print(f"odd numbers {odd_numbers}")
#print (f"squares\t{squares}")

cube = [value for value in range(0,10,2)]

print(f"cubes\t{cube}")

