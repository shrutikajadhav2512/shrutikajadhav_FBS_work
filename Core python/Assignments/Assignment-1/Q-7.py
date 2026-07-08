# program to find the roots of a quadratic equation.
# Input coefficient a,b,c.
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

# Calculations
d = b**2 - 4*a*c
root1 = (-b + d) / (2*a)
root2 = (-b - d) / (2*a)

# Display results
print("first root is:", root1)
print("second root is:", root2)