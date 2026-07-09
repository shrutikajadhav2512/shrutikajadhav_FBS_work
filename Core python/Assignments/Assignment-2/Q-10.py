# WAP to reverse three-digit number
# take threee digit number for reverse
digit=int(input('Enter three digit number:'))
# calculations
digit1=digit%10
num=digit//10
digit2=num%10
num=num//10
digit3=num%10
num=num//10
reverse = digit1 * 100 + digit2 * 10 + digit3
print(f'reverse number is:{reverse} ')


