import os
from time import sleep
admin = ['Andre', 'Irfan']
user = ['Faiz', 'Noval']
alluser = admin + user
buku = ["Sastra", "IPA", "Agama", "Sosial"]
backupbuku = ["Sastra", "IPA", "Agama", "Sosial"]
antreanuser=[]
antreanbuku=[]

terpinjamuser=[]
terpinjambuku=[]


def login_function():
   who = input('Login as : ')
   if who in admin:
      sleep(0.5)
      os.system('cls')
      admin_function(who)
   elif who in user:
      sleep(0.5)
      os.system('cls')
      user_function(who)
   else:
      sleep(0.5)
      os.system('cls')
      print('You dont have permission')
      sleep(0.5)
      os.system('cls')
      login_function()

def admin_function(who):
    choose = ""
    while choose != "7":
        print(terpinjamuser)
        print(terpinjambuku)
        print("Menu Administrator")
        print("1. Input buku yang akan dipinjam")
        print("2. Pinjam buku")
        print("3. Kembalikan buku")
        print("4. Buku Tersedia")
        print("5. Antrean Peminjaman")
        print("6. Logout")
        print("7. Exit")
        choose = input("Masukkan pilihan : ")
        os.system('cls')
        if choose == "1":
            pinjaminput = input("Nama Buku : ")
            userpinjam = input("Nama Peminjam: ")
            if pinjaminput in buku and userpinjam in alluser and userpinjam in antreanuser and pinjaminput in antreanbuku:
                del buku[buku.index(pinjaminput)]
                del alluser[alluser.index(
                    userpinjam)]  # Hapus alluser berdasarkan index agar ketika seorang user masih berstatus meminjam, tidak dapat melakukan peminjaman lagi.
                del antreanuser[antreanuser.index(userpinjam)]
                del antreanbuku[antreanbuku.index(pinjaminput)]
                print("Berhasil!")
                sleep(1)
                os.system('cls')

            else:
                print("Gagal!")
                sleep(1)
                os.system('cls')

        elif choose == "2":
            requestpinjam = input("Masukkan Nama Buku : ")
            if requestpinjam in buku and who not in antreanuser and requestpinjam not in antreanbuku:
                antreanbuku.append(requestpinjam)
                antreanuser.append(who)
                terpinjamuser.append(who)
                terpinjambuku.append(requestpinjam)
                print("Request Anda Segera Diproses Admin, Harap Tunggu!")
                sleep(1)
                os.system('cls')

            else:
                print("Buku Sedang Tidak Tersedia/Sedang Dalam Peminjaman!")
                sleep(1)
                os.system('cls')

        elif choose == "3":
            requestkembalikan = input("Masukkan Buku yang Ingin Dikembalikan : ")
            if requestkembalikan in backupbuku and requestkembalikan not in buku and who in terpinjamuser and terpinjamuser.index(
                    who) == terpinjambuku.index(requestkembalikan):
                buku.append(requestkembalikan)
                alluser.append(who)
                del terpinjamuser[terpinjamuser.index(who)]
                del terpinjambuku[terpinjambuku.index(requestkembalikan)]
                print("Buku berhasil dikembalikan!")
                sleep(1)
                os.system('cls')

            else:
                print("Input Salah!")
                sleep(1)
                os.system('cls')

        elif choose == "4":
            print(buku)

        elif choose == "5":
            if bool(antreanbuku) == 0 and len(antreanuser) == 0:
                print("Antrean Tidak Ada!")
                sleep(1)
                os.system('cls')

            else:
                print(f"Nama: {antreanuser} Buku:{antreanbuku}")

        elif choose == "6":
            print("Logout, Berhasil!")
            sleep(1)
            os.system('cls')
            login_function()
            break
        elif choose == "7":
            print("Exit Berhasil!")
            sleep(1)
            os.system('cls')

        else:
            print("Pilihan Tidak Ada!")
            sleep(1)
            os.system('cls')

def user_function(who):
    choose = ""
    while choose != "5":
        print("Menu User")
        print("1. Pinjam buku")
        print("2. Kembalikan buku")
        print("3. Buku Tersedia")
        print("4. Logout")
        print("5. Exit")
        choose = input("Masukkan pilihan : ")
        os.system('cls')
        if choose == "1":
            requestpinjam = input("Masukkan Nama Buku : ")
            if requestpinjam in buku:
                antreanbuku.append(requestpinjam)
                antreanuser.append(who)
                terpinjamuser.append(who)
                terpinjambuku.append(requestpinjam)
                print("Request Anda Segera Diproses Admin, Harap Tunggu!")
                sleep(1)
                os.system('cls')

            else:
                print("Buku Sedang Tidak Tersedia/Sedang Dalam Peminjaman!")
                sleep(1)
                os.system('cls')

        elif choose == "2":
            requestkembalikan = input("Masukkan Buku yang Ingin Dikembalikan : ")
            if requestkembalikan in backupbuku and requestkembalikan not in buku and who in terpinjamuser and terpinjamuser.index(
                    who) == terpinjambuku.index(requestkembalikan):
                buku.append(requestkembalikan)
                alluser.append(who)
                del terpinjamuser[terpinjamuser.index(who)]
                del terpinjambuku[terpinjambuku.index(requestkembalikan)]
                print("Buku berhasil dikembalikan!")
                sleep(1)
                os.system('cls')

            else:
                print("Input Salah!")
                sleep(1)
                os.system('cls')

        elif choose == "3":
            print(buku)

        elif choose == "4":
            print("Logout, Berhasil!")
            sleep(1)
            os.system('cls')
            login_function()
            break
        elif choose == "5":
            print("Exit Berhasil!")
            sleep(1)
            os.system('cls')
        else:
            print("Pilihan Tidak Ada!")
            sleep(1)
            os.system('cls')


login_function()
