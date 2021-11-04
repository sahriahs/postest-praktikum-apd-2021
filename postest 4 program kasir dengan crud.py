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

#CRUD create = menambah, read = tampil, update = mengubah, delete = menghapus
makanan = ["Bakso Biasa   ", "Bakso Spesial ", "Mie Ayam Biasa", "Mie Ayam Bakso"]
hargamakanan = [10000, 15000, 10000, 15000]
stok = makanan + ["Mie Pangsit   ", "Bakso Mercon  ", "Bakso Urat    ", "Pangsit Krispy"]
pesan = []
jumlah = []
total = []
rerata = []

def menu():
    print(" ========= Menu DEPOT KANG UJANG =========")
    for i in range(0, len(makanan)):
        print(f"        {i + 1}. {makanan[i]}  Rp{hargamakanan[i]}")
        
def tambah():
    print(" ===== Stok Baru Di DEPOT KANG UJANG =====")
    for i in range(0, len(stok)):
        print(f"    {i + 1}. {stok[i]}")
    tambah = stok[int(input("pilih menu baru: ")) - 1]
    harga = int(input("masukkan harga menu baru: "))
    makanan.append(tambah)
    hargamakanan.append(harga)
    print("menu baru telah di tambahkan")

def ubah():
    menu()
    x = int(input("pilih menu yang ingin diubah: ")) - 1
    menu_lama = makanan[x]
    menu_baru = input("menu baru: ")
    makanan[x] = menu_baru
    harga_lama = hargamakanan[x]
    harga_baru = int(input("harga baru: "))
    print(f"{menu_lama} Rp{harga_lama} telah diubah menjadi {menu_baru} Rp{harga_baru}")

def hapus():
    menu()
    x = int(input("pilih menu yang ingin dihapus: ")) - 1
    hapus = makanan[x]
    del makanan[x], hargamakanan[x]
    print(f"{hapus} telah dihapus")

def tambahpesan():
    menu()
    x = int(input("pilih menu: ")) - 1
    order = makanan[x]
    pesan.append(order)
    y = int(input("berapa banyak: "))
    jumlah.append(y)
    z = y * hargamakanan[x]
    total.append(z)

def pesanan():
    if len(pesan) == 0:
        print("Anda belum memesan apapun.")
    else:
        print("============= Pesanan Anda ==============")
        for i in range(0, len(pesan)):
            print(f"    {i + 1}. {jumlah[i]} porsi {pesan[i]} Rp{total[i]}")

def ubahpesan():
    pesanan()
    if len(pesan) != 0:
        x = int(input("pilih pesanan yang ingin diubah: ")) - 1
        pesanan_lama = pesan[x]
        jumlah_lama = jumlah[x]
        total_lama = total[x]
        menu()
        pilih = int(input("pilih pesanan baru: ")) - 1
        pesanan_baru = makanan[pilih]
        pesan[x] = pesanan_baru
        y = int(input("berapa banyak: "))
        jumlah[x] = y
        z = y * hargamakanan[pilih]
        total[x] = z
        print(f"""  pesanan Anda '{jumlah_lama} porsi {pesanan_lama} Rp{total_lama}'
        telah diubah menjadi '{y} porsi {pesanan_baru} Rp{z}'""")
    else:
        selamatdatang()

def hapuspesan():
    pesanan()
    x = int(input("pilih pesanan yang ingin dihapus: ")) - 1
    print(f"pesanan Anda '{jumlah[x]} porsi {pesan[x]} Rp{total[x]}' telah dihapus")
    del jumlah[x], pesan[x], total[x]

def diskon():
        global diskon
        day = input("hari pembelian: ")
        diskon = 0
        if day == "jumat" or day == "senin":
            if sum(total) >= 300000:
                diskon = int((25/100) * sum(total))
                if diskon > 100000:
                    diskon = 100000
                print("===== diskon 25% s.d. Rp100.000 =====")
            elif sum(total) >= 150000 and sum(total) < 300000:
                diskon = int((10/100) * sum(total))
                print("Anda mendapatkan diskon 10%")
            elif sum(total) >= 80000 and sum(total) < 150000:
                diskon = int((5/100) * sum(total))
                print("Anda mendapatkan diskon 5%")
            else:
                print("Anda tidak mendapatkan diskon.")
        else:
            print("Anda tidak mendapatkan diskon.")
        print(f"Anda mendapatkan diskon Rp{diskon}")

def bayar():
    global harga
    if sum(total) != 0:
        print(f"\nTotal tagihan = Rp{sum(total)}")
        lanjut = input("lanjutkan transaksi (y/n): ")
        if lanjut == "y":
            diskon()
            harga = sum(total) - diskon
            rerata.append(harga)
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
            elif pilih == "6":
                break
            else:
                print("menu salah. harap masukkan ulang")
                selamatdatang()
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
                selamatdatang()

#jalannya program
next = "y"
while next == "y":
    login()
    selamatdatang()
    next = input("user selanjutnya? (y/n): ")
    if next =="y":
        del pesan[0:], jumlah[0:], total[0:]