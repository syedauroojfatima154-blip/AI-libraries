# PHASE 1  core python 
"""
  # airthmatic operations 
num1 = float(input("Enter the first number = "))
num2 = float(input("Enter the second number = "))
sum =  num1 + num2
print("final answer :",sum)

# reverse a number (12345)
num = float(input(" Enter the  number ="))
reverse = 0
while num > 0:
     x=num % 10 
     reverse = reverse*10+ x
     num = num//10
     print("REVERSE:",reverse)


#Count Digits & Sum of Digits
num =(float(input("Enter a NUMBER =")))
count=0
total=0
while num > 0:
    x=num %10
    total=x
    count=+1
    num = num//10
    print("total digits:", count)
    print(" sum: ",total)

# strong passwrod checker 
password = input("Enter your password")
has_digit = False
has_upper = False

if len(password)>=8:
    for ch in password :
     if ch.isdigit():
         has_digit = True
     if ch.isupper():
        has_upper = True
    if has_digit and has_upper:
       print("Strong Password")
    else:
       print("Weak Password")
else:
   print("weak Password")
   
# palindrome checker 
num = int(input("Enter a number :"))
orginal_num = 12321
reverse = 0
while num > 0:
    x= num%10
    reverse = reverse *10 + x
    num = num // 10
    if orginal_num == reverse:
     print("palindrome")
else:
    print("Not a palindrome")
    """
    



    

 

