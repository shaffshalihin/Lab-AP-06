awal_a=int(input("Masukan populasi awal serangga A = "))
awal_b=int(input("Masukan populasi awal serangga B = "))
hari=int(input("Masukan jumlah hari = "))
a=awal_a
b=awal_b
for i in range(1,hari+1):
    if i%2!=0:
        a+=int(a*0.3)  
        b+=int(b*0.5)     
    elif i%2==0:  
        a-=int(a*0.2)  
        b-=int(b*0.4)        
    if i%5==0:  
        a-=int(a*0.1)
        b-=int(b*0.1)
        print("Predator memakan 10% populasi")
    print(f"Hari ke-{i}: populasi A = {a}, populasi B = {b}")
