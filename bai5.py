# cau a
n = int(input("Nhap so n : "))
k = int(input("nhap so k  "))
A = []
for i in range(n):
    x = int(input("nhap so nguyen duong"))
    if x > 0:
        A.append(x)
    if  x <=0:
        print("loi do " + str(x) +" khong phai la so nguyen duong")
        exit()
print("Day vua nhap :")
for i in range(len(A)):
    print(A[i], end="\n")
#cau b
#thuat toan sap xep noi bot 
def noibot(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
noibot(A)
print("Sau khi sap xep thi day co thu tu la : ")
for i in range(len(A)):
    print(A[i], end = " ")
