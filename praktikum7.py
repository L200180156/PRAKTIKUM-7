##Praktikum 7
##Kegitan 2
password = 'aulia'
a = str(input('Masukkan Password: '))
for x in range (2):
    if a == password:
        print ('Anda berhasil login')
    elif a != password:
        b = str(input('Maaf, anda salah memasukkan password. Masukkan Password: '))
else:
    print('anda telah memasukkan password 3 kali. akses anda ditolak')
##Kegitan 3
a= str(input('masukkan nama anda: '))
b= float(input('sekarang pukul: '))
if 00.00 <=b<= 11.59:
    print ('selamat pagi', a)
elif 12.00 <=b<= 14.59:
    print ('selamat siang', a)
elif 15.00<=b<=18.59 :
    print ('selamat sore', a)
elif 19.00 <=b<= 23.59:
    print ('selamat malam', a)
