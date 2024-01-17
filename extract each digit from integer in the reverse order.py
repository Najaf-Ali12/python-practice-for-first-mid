# Write a Program to extract each digit
#from an integer in the reverse order.
#WITH FOR LOOP
number = input("enter a number")
print("Given number", number)
for i in number:
    # get the last digit
    digit =int(number) % 10
    # remove the last digit and repeat the loop
    number = int(number) // 10
    print(digit,end=" ")



#WITH WHILE LOOP
x=int(input("enter a number"))
print("Given number is",x)
while x>0:
  ang=x%10
  x=x//10
  print(ang,end=" ")

