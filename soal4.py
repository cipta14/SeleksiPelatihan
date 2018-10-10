def hitungangka(angka):
    ulang = 100
    jmlangka = 0
    for i in range(ulang+1):
        sli = str(i)
        cekdg1 = sli.startswith(str(angka))
        cekdg2 = sli.endswith(str(angka))
        if  cekdg1 == 1 or cekdg2 == 1 :
            if len(sli) > 1 and cekdg1 == 1 and cekdg2 == 1:
                jmlangka = jmlangka + 1
            jmlangka = jmlangka + 1

    print("Angka : ",str(angka), " Muncul Sebanyak : ", str(jmlangka), " Kali")

hitungangka(3)

