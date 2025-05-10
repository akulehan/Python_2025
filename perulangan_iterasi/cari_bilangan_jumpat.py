#Suatu bilangan bulat positif n disebut bilangan JUMPAT jika jumlah n bilangan bulat positif pertama dapat dinyatakan sebagai penjumlahan empat bilangan bulat positif berurutan. Banyaknya bilangan JUMPAT yang kurang dari 2024 adalah ....
#pencarian bilangan jumpat
print ('\n')
n = 1
a = 1
u = 100
setSn = set() #setSn adalah himpunan untuk menampung Sn
setJu = set() #juga himpunan untuk menampung Ju
while n < u:
    Sn=int((n*(n+1))/2)
    setSn.add(Sn)
    n+=1
    print(Sn, end=' ')
print ('-----------------------------------')
while a < u:
    Ju=4*a+6
    setJu.add(Ju)
    a+=1
    print(Ju, end=' ')
print ('\n')
Jumpat = setSn & setJu #irisan 2 himpunan
print ('Jumpat : ',Jumpat)
print ('\n')
print ('--------------------xxxxxxxxxxx-----------------------')

#pengulangan untuk mencari bilangan jumpat 1- 2024
print ('\n')
n = 1
a = 1
u = 2024
setSn = set()
setJu = set()
while n < u:
    Sn=int((n*(n+1))/2)
    setSn.add(Sn)
    n+=1
while a < u:
    Ju=4*a+6
    setJu.add(Ju)
    a+=1
Jumpat = setSn & setJu 
jlhjumpat = len(Jumpat)
print ('Jumlah bilangan jumpat 1-2024 : ', jlhjumpat)