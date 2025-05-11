a = int(input("Masukkan bilangan bulat positif: "))
def k (a):
    hasil = []
    for i in range (1,a+1):
        if a % i == 0:
            hasil.append(i)
    return hasil #return digunakan untuk mengembalikan nilai dari fungsi
n = len(k(a))
print (f'Faktor dari {a} adalah {k(a)}') #f' digunakan untuk format string
print (f'Jumlah faktor dari {a} adalah {n}')

def cp(n): # fungsi cek prima ini dari chatGPT
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

fpr = [x for x in k(a) if cp(x)]# Menyaring bilangan prima dari daftar- dari chatGPT
# membuat list baru yang berisi elemen dari k(a) yang lolos uji fungsi cp(x)
print (f'Faktor prima dari {a} adalah {fpr}')

def kalf (n): # fungsi untuk mencari faktor prima dari bilangan bulat positif- dari chatGPT
    fk = []
    pb = 2
    while n > 1:
        if n % pb == 0:
            fk.append(pb)
            n = n // pb
        else:
            pb += 1
    return fk

fkpr = ' × '.join(map(str, kalf(a))) #Membuat perkalian dari faktor prima
# Fungsi untuk mencari faktorisasi prima berpangkat
def fkpr_eks(faktor):
    # Menghitung frekuensi setiap faktor prima
    hitung = {}
    for p in faktor:
        if p in hitung:
            hitung[p] += 1
        else:
            hitung[p] = 1
    # Membuat string faktorisasi berpangkat
    return ' × '.join([f"{p}^{e}" if e > 1 else str(p) for p, e in hitung.items()])

# Faktorisasi prima berpangkat
print(f"Faktorisasi prima dari {a} adalah: {fkpr}")
print(f"Faktorisasi prima berpangkat dari {a} adalah: {fkpr_eks(kalf(a))}")
