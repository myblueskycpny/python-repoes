import os
from time import sleep
user = ["Faiz", "Irfan", "Oki"]
new_car = ["Ferarri", "Lamborghitu", "Tesla"]
used_car = ["Mitsubishi", "Jazz", "CRV"]
backup_used_car = ["Mitsubishi", "Jazz", "CRV"]
sold_car = []
penyewa = []
rented = []


def login_function():
    who = input("Masukkan Identitas: ")
    if who in user:
        sleep(0.5)
        os.system('cls')
        user_function(who)
    else:
        print("Gagal!")
        


def user_function(who):
    while True:
        print("Hai, " + who)
        priv = input("Masuk sebagai(pembeli/penyewa)?: ")
        if priv == "pembeli" or priv == "penyewa":
            if priv == "pembeli":
                sleep(0.5)
                os.system('cls')
                pembeli_function()
                break
            elif priv == "penyewa":
                sleep(0.5)
                os.system('cls')
                penyewa_function(who)
                break
        else:
            sleep(0.5)
            os.system('cls')
            print("error input!")


def pembeli_function():
    choose = ""
    while choose != "4":
        print("Menu: ")
        print("1. katalog mobil baru")
        print("2. beli mobil")
        print("3. logout")
        print("4. keluar")
        choose = input("masukkan pilihan: ")
        if choose == "1":
            sleep(0.5)
            os.system('cls')
            for x in new_car:
                print("-" + x)
        elif choose == "2":
            buycar = input("masukkan nama mobil yang ingin anda beli: ")
            if buycar in new_car:
                if buycar in sold_car:
                    print("mobil telah terjual!")
                else:
                    confirm = input("anda yakin? (y/n): ")
                    if confirm == "y":
                        del new_car[new_car.index(buycar)]
                        sold_car.append(buycar)
                        sleep(0.5)
                        os.system('cls')
                        print("terima kasih telah berbelanja!")
                    elif confirm == "n":
                        sleep(0.5)
                        os.system('cls')
                        print("we appreciate that, see you later!")
                    else:
                        print("input error!")
                        sleep(0.5)
                        os.system('cls')
                        pembeli_function()
                        break
            else:
                print("error input!")
                sleep(0.5)
                os.system('cls')
                pembeli_function()
                break
        elif choose == "3":
            sleep(0.5)
            os.system('cls')
            print("logout berhasil!")
            login_function()
            break
        elif choose == "4":
            print("berhasil, sampai jumpa!")
        else:
            sleep(0.5)
            os.system('cls')
            print("input error!")


def penyewa_function(who):
    choose = ""
    while choose != "5":
        print("Menu: ")
        print("1. katalog mobil sewa")
        print("2. sewa mobil")
        print("3. kembalikan")
        print("4. logout")
        print("5. keluar")
        choose = input("masukkan pilihan: ")
        if choose == "1":
            sleep(0.5)
            os.system('cls')
            for x in used_car:
                print("-" + x)
        elif choose == "2":
            rentcar = input("masukkan nama mobil yang ingin disewa: ")
            if rentcar in used_car:
                confirm = input("anda yakin? (y/n): ")
                if confirm == "y":
                    del used_car[used_car.index(rentcar)]
                    penyewa.append(who)
                    rented.append(rentcar)
                    sleep(0.5)
                    os.system('cls')
                    print("terima kasih telah menyewa!")
                elif confirm == "n":
                    sleep(0.5)
                    os.system('cls')
                    print("we appreciate that, see you later!")
                else:
                    sleep(0.5)
                    os.system('cls')
                    print("input error!")
                    penyewa_function()
                    break                  
        elif choose == "3":
            return_car = input("masukkan nama mobil yang ingin dikembalikan: ")
            if return_car in backup_used_car and return_car not in used_car and who in penyewa and penyewa.index(
                    who) == rented.index(return_car):
                used_car.append(return_car)
                del penyewa[penyewa.index(who)]
                sleep(0.5)
                os.system('cls')
                print("mobil berhasil dikembalikan!")
            else:
                sleep(0.5)
                os.system('cls')
                print("error")
                penyewa_function()
                break
        elif choose == "4":
            print("logout berhasil!")
            login_function()
            break
        elif choose == "5":
            print("berhasil, sampai jumpa!")
        else:
            print("input error!")


login_function()
