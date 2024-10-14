from prettytable import PrettyTable
admin ={"Admin": "adm123"}
user ={"User": "user123"}

data_pengunjung = [
    [1,"Mus","Kunjungan Biasa"],
    [2,"Riza","Peminjaman Buku"],
    [3,"Topik","Peminjaman Komputer"]
]

def login() :
        print("----------------------------------")
        print("==============Login===============")
        print("----------------------------------")
        Username = str(input("Masukan Username anda: "))
        Password = str(input("Masukan Password anda: "))
        
        if Username in admin and admin[Username] == Password:
            return "admin"
        elif Username in user and user[Username] == Password:
            return Username
        else:
            return None

def menu_Pengunjung(Username):
    while True:
        print(f"*** Menu {Username} ***")
        print("1. Berkunjung")
        print("2. Akitivitas")
        print("3. Keluar")

        pilihan = input("Pilih Menu (1-3): ")

        if pilihan == "1":
            Berkunjung(Username)
        elif pilihan == "2":
            Aktivitas(Username)
        elif pilihan == "3":
            print("Terimakasih Sudah Berkunjung Ke Perpustakaan")
            break
        else:
            print("Pilihan Tidak Ada. Silakan coba lagi.")

def Berkunjung(Username):
    print("----------------------------------------")
    print("+++++ Silahkan Tambahkan Data Anda +++++")
    print("----------------------------------------")
    Nomor = input("Masukan Nomor Anda :  ")
    Nama = input("Masukan Nama Anda : ")
    Aktivitas = input("Masukan Aktivitas Yang Mau Anda Lakukan : ")
    data_pengunjung.append([Nomor, Nama, Aktivitas])
    print("Terimakasih Sudah Daftar, Selamat Datang di Perpustakan")

def Aktivitas(Username):
    lihat_data()

def Keluar(Username):
    print("+++++ Terimakasih Sudah Datang +++++")

def menu_Admin(Username):
    while True:
        print(f"\n*** Menu {Username} ***")
        print("1. Tambah Data Pengunjung")
        print("2. Perbarui Data Pengunjung")
        print("3. Lihat Data Pengunjung")
        print("4. Hapus Data Pengunjung")
        print("5. Keluar")

        pilihan = input("Pilih Menu (1-5): ")

        if pilihan == "1": 
            tambah_data()
        elif pilihan == "2": 
            perbarui_data()
        elif pilihan == "3":
            lihat_data()
        elif pilihan == "4": 
            hapus_data()
        elif pilihan == "5": 
            print("Sampai Jumpa")
            break
        else:
            print("Pilihan Tidak Ada. Silakan coba lagi.")

def tambah_data():
    Nomor = input("Masukkan Nomor Aktivitas : ")
    Nama = input("Masukan Nama Pengunjung : ")
    Aktivitas = input("Masukan Aktivitas : ")
    data_pengunjung.append([Nomor, Nama, Aktivitas])
    print("Nama Telah Di Daftarkan")

def perbarui_data():
    update = str(input("Masukkan Nama Pengunjung Yang Mau Diubah : "))
    for i in range(len(data_pengunjung)): 
        if data_pengunjung[i][1] == update:
            nama_baru = input("Masukkan Nama Pengunjung Yang Baru : ")
            aktivitas_baru = input("Masukkan Aktivitas : ")
            data_pengunjung[i][1] = nama_baru
            data_pengunjung[i][2] = aktivitas_baru
            lihat_data()
            print("Berhasil Mengubah Data.")
            break
    else:
        print("Nama tidak ditemukan, Masukkan data yang benar.")  

def lihat_data():
    table = PrettyTable()
    table.field_names = ["Nomor", "Nama", "Aktivitas"]
    for item in data_pengunjung:
        table.add_row(item)
    print(table)

def hapus_data():
    hapus = input("Masukkan Nama Yang Ingin Dihapus: ")
    for i, siswa in enumerate(data_pengunjung):
        if siswa[1] == hapus:  
            del data_pengunjung[i]
            print(f"Data Pengunjung {hapus} Berhasil Dihapus.")
            lihat_data()

def main():
    print("\n----------------------------------------------------------")
    print("++++++ Selamat Datang Di Perpustakaan ++++++")
    print("----------------------------------------------------------")

    while True:
        user_type = login()
        if user_type == "admin":
            print("Yeay Login Berhasil")
            print("Selamat Datang Admin")
            menu_Admin(user_type) 
        elif user_type:
            print(f"Yeay Login Berhasil: {user_type}!")
            print("Halo Pengunjung")
            menu_Pengunjung(user_type)
        else:
            print("Data Tidak Ada. Silakan coba lagi.")

        ngulang = input("Apakah Anda ingin Lanjut? (iya/tidak): ")
        if ngulang.lower() != 'iya':
            print("Terima kasih telah Datang, Sampai jumpa!")
            break

main()






