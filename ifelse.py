# key = input("pass :")

# if (key=="ntahlah") :
#     print ("Anda berhasil masuk")
# else :
#         print ("kata kunci tidak sesuai")

bil = int(input("masukkan angka :"))

if (bil < 0):
    print ("masukkan hanya bilangan positif")

else :
    if (bil % 2)==0 :
        print ("{0} adalah bilangan  genap".format(bil))
    else :
        print ("{0} adalah bilangan  ganjil".format(bil))