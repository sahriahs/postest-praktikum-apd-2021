#menu login
sandiuser = ["200", "210"]
sandiadm = []
x = 56
while x <= 110:
    if x < 100:
        y = "0" + str(x)
    else:
        y = str(x)
    sandiadm.append(y)
    x += 1

def login():
    print("""
    ================================================
    SELAMAT DATANG DI PROGRAM KASIR DEPOT KANG UJANG 
    ================================================
     SILAKAN LOGIN DENGAN MENG-INPUT NAMA DAN SANDI       
        *sandi admin merupakan tiga nim terakhir
         **sandi user merupakan tiga nim pertama
    ================================================""")
    coba = "y"
    global username
    global sandi
    while coba == "y":
        username = input("masukkan nama: ")
        sandi = (input("masukkan sandi: "))
        if sandi in sandiadm:
            print("login berhasil")
            print("anda login sebagai admin")
            break
        elif sandi in sandiuser:
            print("login berhasil")
            print("anda login sebagai pengguna")
            break
        else:
            print("sandi yang anda masukkan salah")
            coba = input("masukkan ulang sandi (y/n): ")

# bagian utama
daftar = {
    'Bakso Biasa'     :10000,
    'Bakso Spesial'   :15000,
    'Mie Ayam Biasa'  :10000,
    'Mie Ayam Bakso'  :15000
}
pesan = []
jumlah = []
total = []

def menu():
    print(" ========= Menu DEPOT KANG UJANG =========")
    j = 1
    for i in daftar:
        print(f"\t{j}). {i} : Rp{daftar[i]}") 
        j += 1
    print(" =========================================\n")

def tambah():
    print(" =========== MEMBUAT MENU BARU ===========")
    tambahmenu = input("input nama menu baru: ")
    tambahharga = int(input("tambahkan harga menu baru: ")) 
    daftar.update({tambahmenu : tambahharga})
    print(f""" =========================================
 \t Menu Baru Telah Ditambagkan.
 =========================================""")

def ubah():
    menu()
    pilih = input("pilih menu yang ingin diubah: ")
    if int(pilih) in range(len(daftar) + 1):
        print(" ============= MENGUBAH MENU =============")
        x = int(pilih) - 1
        j = 0
        for i in daftar:
            if x == j:
                del daftar[i]
        j += 1
        tambahmenu = input("input nama menu baru: ")
        tambahharga = int(input("tambahkan harga menu baru: ")) 
        daftar.update({tambahmenu : tambahharga})
        print(f""" =========================================
 \tMenu Berhasil Diubah.
 =========================================""")
    else:
        print("menu salah. harap masukkan ulang")
    
def hapus():
    menu()
    print(" ============= MENGHAPUS MENU =============")
    x = int(input("pilih menu yang ingin dihapus: ")) - 1
    j = 0
    for i in daftar:
        if x == j:
            lama = daftar[i]
            del daftar[i]
    j += 1
    print(f""" =========================================
 \tMenu {lama} Berhasil Dihapus.
 =========================================""")

def tambahpesan():
    menu()
    print(" =========== TAMBAHKAN PESANAN ===========")
    x = int(input("pilih menu: ")) - 1
    y = int(input("berapa banyak: "))
    j = 0
    for i in daftar:
        if x == j:
            pesan.append(i)
            z = y * daftar[i]
            total.append(z)
        j += 1
    jumlah.append(y)
    print(f""" =========================================
 \t Pesanan Telah Ditambagkan.
 =========================================""")

def pesanan():
    if len(pesan) == 0:
        print("Anda belum memesan apapun.")
    else:
        print(" ============= Pesanan Anda ==============")
        for i in range(0, len(pesan)):
            print(f"    {i + 1}. {jumlah[i]} porsi {pesan[i]} Rp{total[i]}")
        print(" =========================================")

def ubahpesan():
    pesanan()
    if len(pesan) != 0:
        print(" ============= MENGUBAH MENU =============")
        a = int(input("pilih pesanan yang ingin diubah: ")) - 1
        pesanan_lama = pesan[a]
        jumlah_lama = jumlah[a]
        total_lama = total[a]
        menu()
        x = int(input("pilih pesanan baru: ")) - 1
        y = int(input("berapa banyak: "))
        j = 0
        for i in daftar:
            if x == j:
                pesan.append(i)
                z = y * daftar[i]
                total.append(z)
                pesanan_baru = i
                jumlah.append(y)
                pesan[a] = pesanan_baru
                jumlah[a] = y
                total[a] = z
            j += 1
        print(f""" =========================================
  pesanan Anda '{jumlah_lama} porsi {pesanan_lama} Rp{total_lama}'
        telah diubah menjadi '{y} porsi {pesanan_baru} Rp{z}'
 =========================================""")
    else:
        selamatdatang()

def hapuspesan():
    pesanan()
    print(" ============= HAPUS PESANAN ==============")
    x = int(input("pilih pesanan yang ingin dihapus: ")) - 1
    print(f""" =========================================
 pesanan Anda '{jumlah[x]} porsi {pesan[x]} Rp{total[x]}' telah dihapus.
 =========================================""")
    del jumlah[x], pesan[x], total[x]
    

def diskon():
        global diskon
        day = input("hari pembelian: ")
        diskon = 0
        if day == "jumat" or day == "senin":
            print(" ============ DISKON SPESIAL =============")
            if sum(total) >= 300000:
                diskon = int((25/100) * sum(total))
                if diskon > 100000:
                    diskon = 100000
                print("===== diskon 25% s.d. Rp100.000 =====")
            elif sum(total) >= 150000 and sum(total) < 300000:
                diskon = int((10/100) * sum(total))
                print("============= diskon 10% =============")
            elif sum(total) >= 80000 and sum(total) < 150000:
                diskon = int((5/100) * sum(total))
                print("============= diskon 5% =============")
            else:
                print("Anda tidak mendapatkan diskon.")
        else:
            print("Anda tidak mendapatkan diskon.")
        print(f""" =========================================
    Anda mendapatkan diskon Rp{diskon}
 =========================================""")

def bayar():
    global harga
    if sum(total) != 0:
        print(f"\nTotal tagihan = Rp{sum(total)}")
        lanjut = input("lanjutkan transaksi (y/n): ")
        if lanjut == "y":
            diskon()
            harga = sum(total) - diskon
            print(f"Total harus dibayar = Rp{harga}")
            uang = int(input("Uang Tunai Pembeli: Rp"))
            while uang < harga:
                print("Uang Tunai Kurang. Harap Masukkan Ulang")
                uang = int(input("Uang Tunai Pembeli: Rp"))
            kembali = uang - harga
            print(f"""
    ================================================
    ================== STRUK BELI ==================
    ================================================
    Nama          : {username}
    Beli          :""")
            for i in range(0, len(pesan)):
                print(f"                    {i + 1}. {jumlah[i]} porsi {pesan[i]} Rp{total[i]}")

            print(f"""    Total         : Rp{sum(total)}
    Diskon        : - Rp{diskon}
    Total Tagihan : Rp{harga}
    Uang          : Rp{uang}
    Kembali       : Rp{kembali}
    ================================================
            terima kasih atas kunjungan Anda
    ================================================
        """)
        elif lanjut == "n":
            selamatdatang()
    else:
        print("belum ada pesanan.")
        selamatdatang()

def selamatdatang():
    while True:
        if sandi in sandiadm:
            print("""
    [1] Tampilkan Menu
    [2] Tambahkan Menu
    [3] Ubah Menu
    [4] Hapus Menu
    [5] Keluar
    """)
            pilih = (input("masukkan pilihan: "))
            if pilih == "1":
                menu()
            elif pilih == "2":
                tambah()
            elif pilih == "3":
                ubah()
            elif pilih == "4":
                hapus()
            elif pilih == "5":
                break
            else:
                print("menu salah. harap masukkan ulang")
        elif sandi in sandiuser:
            print("""
    [1] Tampilkan Menu
    [2] Tambahkan Pesanan
    [3] Tampilkan Pesanan Saya
    [4] Ubah Pesanan
    [5] Hapus Pesanan
    [6] Bayar Pesanan
    [7] Keluar
    """)
            pilih = (input("pilih menu: "))
            if pilih == "1":
                menu()
                print(""" =========== PENAWARAN SPESIAL ===========
 DISKON S.D 25% PADA HARI SENIN DAN JUMAT  
       *syarat dan ketentuan berlaku
 =========================================""")
            elif pilih == "2":
                tambahpesan()
            elif pilih == "3":
                pesanan()
            elif pilih == "4":
                ubahpesan()
            elif pilih == "5":
                hapuspesan()
            elif pilih == "6":
                bayar()
                break
            elif pilih == "7":
                break
            else:
                print("menu salah. harap masukkan ulang")

#jalannya program
next = "y"
while next == "y":
    login()
    selamatdatang()
    next = input("user selanjutnya? (y/n): ")
    if next == "y":
        del pesan[0:], jumlah[0:], total[0:]
