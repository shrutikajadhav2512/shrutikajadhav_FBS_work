# Write a Python program to find the longest common prefix of all
# strings. Use the Python set.
def prefix(words):
    answer = ""
    a = words.pop()
    b = words.pop()
    c = words.pop()
    for i in range(5):
        if(a[i] == b[i] == c[i]):
            answer += a[i]
        else:
            break

    print(answer)
words = {"flower", "flow", "flight"}
prefix(words)