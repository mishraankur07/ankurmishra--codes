
#string concatenation
from builtins import input, int, print


str1 = "ankur"
str2 = "mishra"
print(str1 +str2)

str = "hello i aam ankur"
str = str.capitalize()
print(str)

str = "hello i aam ankur"
str = str.replace("r","rmishra")
print(str)

str = "hello i aam ankur"
str = str.find("ankur")
print(str)

age = 21
if(age>=18) :
    print("you are eligible to vote")
    


marks = int(input("enter the marks"))
if(marks >= 90) :
     print("gradeA") 
elif(marks >= 80 and marks < 90):
    print("gradeB")
elif(marks >= 70 and marks < 80):
     print("gradeC")
else:
     print("gradeD")



num = int(input("eeenter the njumber"))
if(num%2 == 0):
     print("even number")
else:   
     print("odd number")
