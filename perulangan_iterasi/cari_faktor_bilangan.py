a = int(input("Masukkan bilangan bulat positif: "))
def k (a):
    hasil = []
    for i in range (1,a+1):
        if a % i == 0:
            hasil.append(i)
    return hasil
n = len(k(a))
print (f'Faktor dari {a} adalah {k(a)}') #f' digunakan untuk format string
print (f'Jumlah faktor dari {a} adalah {n}')