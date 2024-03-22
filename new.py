
numbers = [5, 2, 8, 3, 7, 8, 9, 11]
odd_numbers = []
even_numbers = []
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])
    else:
        odd_numbers.append(numbers[i])
    i += 1
print(f"Odd numbers: {odd_numbers}")
print(f"Even numbers: {even_numbers}")