""" edge cases: a non-integer value is provided in the first or as part of the second argument
the number of items provided in the second argument does not match N-1
there are duplicate values in the second argument"""


import sys
argumentList = sys.argv           #getting command line argument from the console
number=sys.argv[2].split()        #converting the string into list of individual numbers
if (not argumentList[1].isdigit()):   #check if first argument is non-integer
   print("a non-integer value is provided")
elif any((not i.isdigit()) for i in number):   #check if part of second argument is non-integer
   print("The Second argument contains a non integer value")
elif len(number)!=int(argumentList[1])-1:       #check if second argument not match with n-1
   print("the number of items provided in the second argument does not match N-1")
elif len(number) != len(set(number)): #check if second argument contains duplicates
   print("there are duplicate values in the second argument")
else:
   n=int(argumentList[1])
   number=list(map(int,number))
   print("The missing number is:",end='')       #printing the missing value using loop
   for missing_num in range(1,n+1):
       if missing_num in number:
           continue
       else:
           print(missing_num)
            
#python missing.py 1 "1 2 3 5" give the arg[2] in string