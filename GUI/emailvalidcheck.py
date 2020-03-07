import re
txt=input("Enter Mail Id Here: ")
x=re.findall("@+",txt)
if (x):
    print("Valid Mail")
else:
    print("invalid")
	    
