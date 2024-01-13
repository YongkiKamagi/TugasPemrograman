def tampilkan_menu():
    print("Selamat datang di program pendaftaran karyawan")
    print("Menu :")
    print("1. Daftar karyawan")
    print("2. Lihat semua karyawan")
    print("3. Hapus karyawan")
    print("4. Keluar")


def daftar_karyawan(karyawan):
    nama = input("Masukkan nama karyawan : ")
    umur = int(input("Masukkan umur karyawan : "))
    pekerjaan = input("Masukkan pekerjaan karyawan : ")
    karyawan.append([nama, umur, pekerjaan])


def lihat_karyawan(karyawan):
    print("\nSemua Karyawan :")
    for data in karyawan:
        print("Nama : ", data[0])
        print("Umur : ", data[1])
        print("Pekerjaan : ", data[2])
        print("===================================")


def hapus_karyawan(karyawan):
    nama = input("Masukkan nama karyawan yang ingin dihapus : ")
    for i in range(len(karyawan)):
        if karyawan[i][0] == nama:
            karyawan.pop(i)
            print("\nKaryawan berhasil dihapus")
            break
    else:
        print("\nKaryawan tidak ditemukan")


karyawan = []
while True:
    tampilkan_menu()
    pilihan = int(input("Masukkan pilihan anda : "))
    if pilihan == 1:
        daftar_karyawan(karyawan)
    elif pilihan == 2:
        lihat_karyawan(karyawan)
    elif pilihan == 3:
        hapus_karyawan(karyawan)
    elif pilihan == 4:
        break
    else:
        print("\nPilihan tidak valid, silahkan coba lagi")