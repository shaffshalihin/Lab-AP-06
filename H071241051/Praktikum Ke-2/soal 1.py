sisi_1=int(input('Masukan Sisi = '))
sisi_2=int(input('Masukan Sisi = '))
sisi_3=int(input('Masukan Sisi = '))
if sisi_1 + sisi_2 > sisi_3 and sisi_1+sisi_3>sisi_2 and sisi_2+sisi_3>sisi_1 :
    if sisi_1==sisi_2 or sisi_2==sisi_3 or sisi_3==sisi_1 :
        print('Adalah segitiga sama kaki')
    elif sisi_1==sisi_2==sisi_3 :
        print('Adalah segitiga sama sisi') 
    elif sisi_3!=sisi_1!=sisi_2 :
        print('Adalah segitiga sebarang')
else:
   print('Tidak dapat membentuk segitiga yang valid')
