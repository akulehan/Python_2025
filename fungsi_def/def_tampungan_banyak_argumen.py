#contoh
print ('\n')
def salampagi (*VarArgs):
    print ('Halo')
    print('Selamat pagi ', end = ' ')
    for Arg in VarArgs:
        print (Arg, end = ' ')
salampagi('Joni','Eka','Rama')
print ('\n') #untuk menambah spasi
#ini bikin sendiri
def ponakanku (*ganteng):
    print ('Halo bocah ganteng')
    print ('Ayok makan bareng')
    for ant in ganteng:
        print (ant)
ponakanku ('Wawan', 'Wansah', 'Ihsan', 'Salman', 'Syamil', 'Rohmat')
print ('\n')
def muridku (*pintar):
    print ('Halo murid pintar')
    print ('Ayok belajar bareng', end = ' ') #, end = ' ' agar dipanggil di baris sama
    for tar in pintar:
        print (tar, end = ' ')
muridku ('Ridho', 'Aman', 'Syapik')
print ('\n')