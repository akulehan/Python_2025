print ('\n')
print('Kita akan bantu menghitung sisa bagi')
bilangan = int(input('Masukkan bilangan yang akan dibagi: '))
pembagi = int(input('Masukkan bilangan pembagi: '))
def pembagian (bilangan,pembagi):
    hasilbagi = bilangan/pembagi
    hasilbagibulat =int(hasilbagi)
    sisapembagian = bilangan - (hasilbagibulat*pembagi)
    return sisapembagian
print ('Modulus atau sisa bagi :' ,pembagian (bilangan,pembagi))
print ('Dapat juga ditulis: ', pembagian (bilangan,pembagi),'( mod', pembagi ,')')
print ('\n')