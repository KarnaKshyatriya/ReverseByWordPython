def rev(word):
    return word[::-1]

def revfunction(ls):
    for i in ls:
        print(rev(i),end=' ')

myInput=input('Please enter a string to reverse by word')

ls=myInput.split(' ')
revfunction(ls)
print()
input('Please press enter to exit from the console')