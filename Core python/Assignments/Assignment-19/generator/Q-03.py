# Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.
def number(start,end,step):
    for i in range(start,end,step):
        while i <= end:
                yield(i)
        
start=int(input("Enter starting value:"))
end=int(input("Enter ending value:"))
step=int(input("Enter value for step:"))
number(start,end,step)