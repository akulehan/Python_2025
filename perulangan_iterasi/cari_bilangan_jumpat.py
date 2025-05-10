#Suatu bilangan bulat positif n disebut bilangan JUMPAT jika jumlah n bilangan bulat positif pertama dapat dinyatakan sebagai penjumlahan empat bilangan bulat positif berurutan. Banyaknya bilangan JUMPAT yang kurang dari 2024 adalah ....
n = range (1,2024)
setSn = set() #setSn adalah himpunan untuk menampung Sn
for i in n:
    Sn=int((i*(i+1))/2)
    a=(Sn-6)/4
    if a==int(a):
        setSn.add(Sn) #menyimpan Sn ke dalam himpunan
Jumpat = len (setSn) #menghitung banyaknya anggota setSn
print ('Jumpat : ',Jumpat)

#Bonus Menghitung modulus (hasil bagi)
a = 10
b = 3
hasil_modulus = a % b
print("Sisa hasil bagi:", hasil_modulus)  # Output: 1