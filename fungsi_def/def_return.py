print ('\n')
print('Kita akan bantu menghitung sisa bagi')
def pembagian (bilangan,pembagi):
    hasilbagibulat = bilangan // pembagi #tanda // adalah pembagian bulat
    sisapembagian = bilangan - (hasilbagibulat*pembagi)
    return sisapembagian
bilangan = int(input('Masukkan bilangan yang akan dibagi: '))
pembagi = int(input('Masukkan bilangan pembagi: '))
print ('Modulus atau sisa bagi :' ,pembagian (bilangan,pembagi))
print ('Dapat juga ditulis: ', bilangan, ' = ' , pembagian (bilangan,pembagi),'( mod', pembagi ,')')
print ('\n')