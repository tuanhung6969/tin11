# cau a
n = int(input("Nhap so n : "))
A = []
for i in range(n):
    x = int(input("nhap so nguyen duong "))
    if x > 0:
        A.append(x)
    if  x <=0:
        print("loi do " + str(x) +" khong phai la so nguyen duong")
        exit()
print("Day vua nhap :")
for i in range(len(A)):
    print(A[i], end = " "),
#cau b 
print("           ")
B= []
for n in A:
    for i in range(2, n):
        if n % i == 0:
    #      print("Số {0} không phải số nguyên tố".format(n))
            break
    else:
        B.append(n)
print("so luong cac so nguyen to trong day la " + str(len(B)))