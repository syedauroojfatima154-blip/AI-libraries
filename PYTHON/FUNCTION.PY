# phase 2 function
"""
# reverse a number through function
def reverse_number(num):
    reverse = 0
    while num > 0:
        x = num % 10
        reverse = reverse * 10 + x
        num //= 10
    return reverse

print(reverse_number(1234))

# sum of  digit  with funtions 
def sum_of_number(num):
    total=0
    while num>0 :
        x=num% 10
        total+=x
        num//=10
    return total 
num = int(input("enter a number :"))
print("sum_of_digits:",sum_of_number(num))
"""

