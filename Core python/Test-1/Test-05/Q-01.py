# A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.

def lists(amount):
    D = [2000, 500, 200, 100, 50, 20, 10, 5]
    count = 0
    for denomination in D:
        notes=amount//denomination
        count+=notes
        amount%=denomination
    print("Minimum number of notes needed:", count)
amount = int(input("Enter amount: "))
lists(amount)