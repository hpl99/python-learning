import pyjokes
import os
directory= 'C:/Users/edgeo/helo'
contents = os.listdir(directory)
for i in contents:
    print(i)
print("Twinkle twinkle little star ")
jokes = pyjokes.get_joke()
print(jokes)
# type casting
x  = "3120"
a = type(x)
print(a)
#converting type
print(float(x))
# input 

i = int(input("ENTER MNUM"))
J = int(input("enter numd5rg")) # if wec dont add int or something then it concatenates them cosidering them as string 

print(i+J)