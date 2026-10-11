# WAP to print following patterns 
width = 21

print("*" * width)
spaces = 25
for i in range(10):
    print(" " * spaces + "*")
    spaces -= 2

print("*" * width + " *")
