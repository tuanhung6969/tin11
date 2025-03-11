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
print("      ")
#cau b 
def abc(A,k):
    for i in range(len(A)):
        if A[i] == k:
            m = i
            return m
    return -100
if abc(A,k) == -100:
    print("khong tim thay")
if abc(A,k) != -100:
    print("k o vi tri thu" + str(abc(A,k)))