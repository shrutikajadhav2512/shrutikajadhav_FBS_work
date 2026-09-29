# Find all of the words in a string that are less than 5 letters (take
# input from user)
s = input("Enter a string: ")
words = [word for word in s.split() if len(word) < 5]
print(words)
