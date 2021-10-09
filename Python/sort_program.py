import time
def ascending_sort(n):
    a = []
    print('Enter numbers one by one:\n')
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        for j in range(1,n-i):
            if a[j-1]>a[j]:
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp
    print('The sorted list is   ',a)

def descending_sort(n):
    d = []
    print('Enter numbers one by one:\n')
    for i in range(n):
        d.append(int(input()))
    for i in range(n):
        for j in range(1,n-i):
            if d[j-1]<d[j]:
                temp = d[j-1]
                d[j-1] = d[j]
                d[j] = temp
    print('The sorted list is   ',a)
print(time.asctime(time.localtime()))
s = int(input('Press 0 for ascending order and 1 for descending order:\n'))
n = int(input('Enter the size of list:\n'))
if s == 0:
    ascending_sort(n)
else:
    descending_sort(n)