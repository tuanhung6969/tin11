# cau a
n = int(input("Nhap so n : "))
A = []
for i in range(n):
    x = int(input("nhap so nguyen duong"))
    if x > 0:
        A.append(x)
    if  x <=0:
        print("loi do " + str(x) +" khong phai la so nguyen duong ")
        exit()
print("Day vua nhap :")
for i in range(len(A)):
    print(A[i], end = " "),
# cau b
B = []
for i in A:
    if i%2==0:
        B.append(i)
c=0
k = len(B)
print("         ")
print("Co " + str(k) + " so chan trong day" )
for i in B:
    c = c+i
print("tong cac so chan trong day la " + str(c))