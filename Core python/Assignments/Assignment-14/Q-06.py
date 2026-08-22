# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.
def maximumProduct(a):
    max_product=0
    for i in a:
        for j in a:
            product=i*j
            if(product>max_product):
                max_product=product
                first_number=i
                second_number=j
    print(first_number,second_number,max_product)
a={10,25,5,7}
maximumProduct(a)