# Python Program to Detect if Two Strings are Anagrams
def anagram():
    counta=0
    countb=0
    for ch in a:
        for i in a:
            if(ch==i):
                counta+=1
        for j in b:
            if(ch==j):
                countb+=1
    if(counta==countb):
        print("Anagram")
    else:
        print("Not anagram")
a="listen"
b="silent"
anagram()
