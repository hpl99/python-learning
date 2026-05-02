# i = input("Enter string you wanto to ")
# print("GOOD AFTERNOON" ,i  )

# name  = input("Enter name of you like the shape of ypuu")
# date = input("Enter the date")
# print(f"Dear <{name}>, \nYou are Selected!\n<{date}>  ")
#comments 
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(letter.replace("<|Name|>","paaji" ).replace("<|Date|>","25-keptemyur-20987"))

#for detection of double string 
yut = "har har haaar r  r"
indx = yut.find("haaar")
cult = yut.replace("  "," ")
print(yut)
print(cult)
print (indx)