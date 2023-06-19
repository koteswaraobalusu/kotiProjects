'''Q.1 Write a function SmallLargeSum(array) which accepts the array as an argument or parameter, that performs the addition of the second largest element from the even location with the second largest element from an odd location?

Rules:'''
'''lst=[10,20,25,70,90]
lst.sort(reverse=True)
print(lst)
a=[]
b=[]
def largesmallsum(arr):
    for i in lst:
        if lst.index(i)%2==0:
            a.append(i)
        else:
            b.append(i)
    print(arr+a[-1])
    print(arr+b[0])
largesmallsum(2)'''

'''prime_numbers = [11, 3, 7, 5, 2]


prime_numbers.sort()

print(prime_numbers)'''
'''def password(p):
    if len(p)>=4:
        return 1
    x=re.find('[0-9]',p)
    if x==None:
        return 1
    else:
        return 0
    y=re.find('[A-Z]',p[0])
    if y==None:
        return 1
    else:
        return 0
    for i in p:
        if i!=' ' or '/':
            return 1
        else:
            return 0
    z=re,find('[0-9]',p[0])
    if z==None:
        return 1
    else:
        return 0
print(password('dtring1234'))'''
a=input('enter a string:')
print(''.join(format(ord(i),'02b') for i in a))
        


