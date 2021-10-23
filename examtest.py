a=int(input("masukkan batas bawah :"))
b=int(input("masukkan batas atas :"))

for x in range(a,b):
    for y in range(a,b):
        for y in range(1,x):
            print("*",end=" ")
        print("")

a=100
b=50

if (a==b):
    m=a*3
else :
    if (a%b==0):
        m=a*5
    else :
        m=a*7

print(m)

data=[('bejo',77),('rudi',58),('maya',99,)]
nilai=[]

for x in data :
    nilai.append(x[1])
print(sorted(nilai))

for z in range(10,-2,2):
    print(z,end=" ")