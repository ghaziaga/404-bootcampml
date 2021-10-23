pemain = input("Haii, selamat datang di permainan, masukkan nama :")
print ("Oke "+pemain+" silahkan pikirkan angka dari 1-10 dan sistem akan menebaknya dalam 4 langkah")

jawaban=input("Jawab pertanyaan dengan y atau n \n Apakah angka tersebut lebih dari 5 ?\n ")

if (jawaban=="y"):
  jawaban=input("Apakah angka tersebut 8 atau lebih dari 8 ?\n ")
  if (jawaban=="y"):
    jawaban=input("Apakah angka tersebut habis dibagi 2 ?")
    if (jawaban=="y"):
      jawaban=input("Apakah angka tersebut 8 ?")
      if (jawaban=="y"):
        print("Berhasil Tertebak angka anda adalah 8")
      else :
        print("Angka anda adalah 10")
    else :
      print ("Angka tersebut adalah 9")

  else :
    jawaban=input("Apakah angka tersebut habis dibagi 2 ?")
    if (jawaban=="y"):
      print ("Angka Tersebut adalah 6")
    else :
      print ("Angka tersebut adalah 7")

else :
  jawaban=input("Apakah angka tersebut besar dari 3 ?")
  if(jawaban=="y"):
    jawaban=input("Apakah angka tersebut habis dibagi 2 ?")
    if (jawaban=="y"):
      print("Angka tersebut adalah 4")
    else :
      jawaban=input("Apakah angka tersebut 5 ?")
      if (jawaban=="y"):
        print("Berhasil tertebak angka tersebut adalah 5")
      else :
        print ("Angka tersebut adalah 3")
  else :
    jawaban=input("Apakah angka tersebut habis dibagi 2 ?")
    if (jawaban=="y"):
      print("Angka tersebut adalah 2")
    else :
      print("Angka tesebut adalah 1")

