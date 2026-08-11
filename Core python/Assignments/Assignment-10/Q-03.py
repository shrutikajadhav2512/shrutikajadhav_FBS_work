# Write a program to find the second largest element in the list.
numbers = [100,50,39,700,459,500]

largest = numbers[0]
second = numbers[1]

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    if i > second and i != largest:
        second = i

print("Second largest:", second)