nilai_akhir=int(input('nilai akhir = '))
persetase_kehadiran=int(input('persentase kehadiran = '))
tugas_tambahan=(input('tugas tambahan = '))
if nilai_akhir < 60 and persetase_kehadiran < 75 :
    print('Tidak lulus')
elif 85<=nilai_akhir<=100 :
    print ('Lulus dengan predikat A')
elif 70<=nilai_akhir<=84 :
    print ('Lulus dengan predikat B')
elif 60<=nilai_akhir<=69 :
    print ('Lulus dengan predikat C')
elif nilai_akhir <= 60 and tugas_tambahan >= 70 :
    print ('Lulus dengan predikat C')
