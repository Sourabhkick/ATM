
from num2words import num2words
num = 5601656
print(num2words(num))

num = [5,6,0,1]
num1 = ["hundret","thousent"]
#
# 1000 * 5 = 5000
# 500
# 100 * 6 = 600
# 50
# 10
# 1 * 1 = 1

for i in num:
    print(i,end=" ")

a=int(input("enter the amount :-"))
def amount(a):
  n = [1000, 500, 100, 50, 10, 1]
  x = 0
  for i in range(6):
    q = n[i]
    x += int(a / q)
    a = int(a % q)
  if a > 0:
    x = -1
  return x
print("No Of Notes :-",amount(a))
