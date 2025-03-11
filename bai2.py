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
#cau b
print("            ")
B =[]
for i in A:
    if i%3==0:
        if i%5==0:
            B.append(i)
print("so luong cac so chia het cho 3 va 5 la : " +str(len(B)))
print(B)