a = int(input('Enter Value Of A : '))
b = int(input('Enter Value Of B : '))
c = int(input('Enter Value Of C : '))

if(a>b):
    if(b>c):
        print('A is Largest Number.')
elif(b>c):
    print('B is Largest Number.')
else:
    print('C Is Largest Number.')