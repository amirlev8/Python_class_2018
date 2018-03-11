# python_class_2018. HW1 Q2. Amir Levi 032551087.

#I'll start by defining a helping function that will tell me if a number is a plaindrome.
def pal_check(check_pal_input):
  """
  check if a number is a palindrome
"""
  a = False
  if check_pal_input==check_pal_input[::-1]:
      a=True
  return a



def check_palindrome():
  """
  Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition. 
   
   Note: It should print out the first number (with a palindrome in its last 4 digits), 
   not all 4 "versions" of it.
"""
  numbers=[]
  for j in range(100000,999999): #run on all 6 figuers numbers
    num1=str(j)[-4::1] 
    check = pal_check(num1) #Check if the last 4 numbers are a palindrome
    if check: #if check is True
      num2=str(j+1)[-5::1]
      check=pal_check(num2) #check if the last 5 numbers are a palindrome
      if check:
        num3=str(j+2)[1:4:1]
        check=pal_check(num3) #check if the middle 3 numbers are a palindrome
        if check:
          num4=str(j+3)
          check=pal_check(num4) #check if the number is a palindrome
          if check:
            numbers.append(j)
  return numbers          
        
    
b=check_palindrome()
print(b)
