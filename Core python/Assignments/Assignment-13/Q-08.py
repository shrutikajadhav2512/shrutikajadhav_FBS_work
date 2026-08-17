# Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary
def word_frequency(string):
    freq = {}
    word = ""

    for ch in string:
        if ch != " ":
            word = word + ch
        else:
            if word != "":
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
                word = ""

    if word != "":
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    print(freq)

string = "cricket kho-kho cricket football kho-kho cricket"
word_frequency(string)