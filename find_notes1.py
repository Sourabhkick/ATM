# y=int(input("enter Amount :-"))
# x=[1000,500,200,100,50,10,5,1]
# total=y
# i=0
# while y>0:
#     if y>x[i]:
#         count=y//x[i]
#         print(count,"notes of",x[i])
#     y=y%x[i]
#     i+=1
# print("total is ",total)



import requests
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
print(r.content)