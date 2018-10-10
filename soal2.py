jmlbilangan = int(input("Masukkan Jumlah Bilangan : "))

nilai1 = 0
nilai2 = 1
jml = 0

# check if the number of terms is valid
if jmlbilangan <= 0:
   print ("Masukkan Bilangan Positif")
elif jmlbilangan == 1:
   print("Urutan Fibonacci Dengan Jml bilangan ",jmlbilangan,":")
   print(nilai1)
else:
   print("Urutan Fibonacci Dengan Jml Bilangan ",jmlbilangan,":")
   while jml < jmlbilangan:
       print(nilai1,end=' , ')
       hasil = nilai1 + nilai2
       nilai1 = nilai2
       nilai2 = hasil
       jml += 1