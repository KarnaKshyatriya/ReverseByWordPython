variableString=input('Hey user give me a string to reverse::  ')
ls=variableString.split(' ')

for i in ls[::-1]:
    print(i,end=' ')

print()
#print(variableString)
input('Please press enter to exit the console')