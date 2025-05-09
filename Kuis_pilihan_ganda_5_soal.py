print('Hallo, nama kamu siapa? Ketikkan ya!')
nama=input("Nama :")
print('Terimakasih. Salam Kenal',nama,'!')
print('Aku punya teka-teki untukmu? Apakah kamu bersedia menjawab?')
kesediaan=input('Jawabanmu: ')
if kesediaan=='Ya' or kesediaan=='ya' or kesediaan=='YA' or kesediaan=='Y' or kesediaan=='y' or kesediaan=='mau':
   print('Bagus, Ayo kita mulai bermain')
else:
   print('Baiklah lain kali kita bermain')
benar = 0
salah = 0
print('Siapakah Presiden pertama Indonesia?'
      '\n'
      'A. Soekarno'
      '\n'
      'B. Soeharto'
      '\n'
      'C. Joko Widodo'
      '\n'
      'D. Prabowo'
      '\n'
      'Jawab dengan mengetik A, B, C, atau D ya!')
jawaban1=input('Jawabanmu: ')
if jawaban1=='A'or jawaban1=='a':
   print('Jawabanmu Benar')
   benar += 1
else:
   print('Maaf, jawabanmu masih salah! Coba lagi')
   salah += 1 
print('Pertanyaan selanjutnya:')
print('Apa lambang negara Indonesia?'
      '\n'
      'A. Merpati'
      '\n'
      'B. Garuda'
      '\n'
      'C. Elang'
      '\n'
      'D. Rajawali')
jawaban2 = input('Jawabanmu: ')
if jawaban2 == 'B' or jawaban2 == 'b':
   print('Jawabanmu Benar')
   benar += 1
else:
   print('Maaf, jawabanmu masih salah! Coba lagi')
   salah += 1
print('Pertanyaan selanjutnya:')
print('Apa ibu kota negara Indonesia?'
      '\n'
      'A. Surabaya'
      '\n'
      'B. Bandung'
      '\n'
      'C. Jakarta'
      '\n'
      'D. Yogyakarta')
jawaban3 = input('Jawabanmu: ')
if jawaban3 == 'C' or jawaban3 == 'c':
   print('Jawabanmu Benar')
   benar += 1
else:
   print('Maaf, jawabanmu masih salah! Coba lagi')
   salah += 1

print('Pertanyaan selanjutnya:')
print('Siapakah pahlawan yang dikenal dengan julukan "Bapak Pendidikan"?'
      '\n'
      'A. Ki Hajar Dewantara'
      '\n'
      'B. RA Kartini'
      '\n'
      'C. Soekarno'
      '\n'
      'D. Moh. Hatta')
jawaban4 = input('Jawabanmu: ')
if jawaban4 == 'A' or jawaban4 == 'a':
   print('Jawabanmu Benar')
   benar += 1
else:
   print('Maaf, jawabanmu masih salah! Coba lagi')
   salah += 1

print('Pertanyaan terakhir:')
print('Apa dasar negara Indonesia?'
      '\n'
      'A. UUD 1945'
      '\n'
      'B. Pancasila'
      '\n'
      'C. Bhineka Tunggal Ika'
      '\n'
      'D. Proklamasi')
jawaban5 = input('Jawabanmu: ')
if jawaban5 == 'B' or jawaban5 == 'b':
   print('Jawabanmu Benar')
   benar += 1
else:
   print('Maaf, jawabanmu masih salah! Coba lagi')
   salah += 1
print('Permainan sudah selesai, terimakasih sudah bermain!')
print('Kamu menjawab',benar,'pertanyaan dengan benar')
print('Kamu menjawab',salah,'pertanyaan dengan salah')
print('Skor kamu adalah ',benar*20)
print('Terima kasih, ',nama, '! Sampai jumpa lagi!')

