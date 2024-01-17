#Exercise 15: Write a function called exponent(base, exp)
#that returns an int value of base raises to the power of exp.
#done by my logic
def exponent(base,expos):
  return base**expo
expo=int(input("enter the exponent"))
base=int(input("enter the base"))
t=exponent(base,expo)
print(base,"raises to the power of ",expo,":",t)




#done by pynative.com
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)
