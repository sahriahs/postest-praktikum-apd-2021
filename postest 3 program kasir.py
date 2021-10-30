print("""
----------------------------------------------
---------- MENU DI DEPOT KANG UJANG ----------
----------------------------------------------
    MAKANAN: 1. Bakso Biasa        Rp10.000
             2. Bakso Spesial      Rp15.000
             3. Mie Ayam Biasa     Rp10.000
             4. Mie Ayam Bakso     Rp15.000

    MINUMAN: 1. Teh Es/Teh Panas   Rp3.000
             2. Es Jeruk           Rp5.000
            
------------- PENAWARAN SPESIAL --------------
   DISKON S.D 25% PADA HARI SENIN DAN JUMAT  
        *syarat dan ketentuan berlaku
----------------------------------------------""")

pembeli = input("Masukkan nama Pembeli: ") 

nomor = int(input("Masukan Pilihan Makanan: "))
porsi = int(input("Berapa Porsi: "))
    
if nomor == 1:
    total1 = porsi * 10000
    print (f"{porsi} porsi Bakso Biasa = Rp{total1}")
    jenis1=("Bakso Biasa")

elif nomor == 2:
    total1 = porsi * 15000
    print (f"{porsi} porsi Bakso Spesial = Rp{total1}")
    jenis1 = ("Bakso Spesial")
    
elif nomor == 3:
    total1 = porsi * 10000
    print (f"{porsi} porsi Mie Ayam Biasa = Rp{total1}")
    jenis1 = ("Mie Ayam Biasa")

elif nomor == 4:
    total1 = porsi * 15000
    print (f"{porsi} porsi Mie Ayam Bakso = Rp{total1}")
    jenis1 = ("Mie Ayam Bakso")

else:
    while True:
        print("Pilihan tidak ada, silahkan masukan lagi")
        nomor = int(input("Masukan Pilihan Makanan: "))
        porsi = int(input("Berapa Porsi: "))
            
        if nomor == 1:
            total1 = porsi * 10000
            print (f"{porsi} porsi Bakso Biasa = Rp{total1}")
            jenis1=("Bakso Biasa")

        elif nomor == 2:
            total1 = porsi * 15000
            print (f"{porsi} porsi Bakso Spesial = Rp{total1}")
            jenis1 = ("Bakso Spesial")
            
        elif nomor == 3:
            total1 = porsi * 10000
            print (f"{porsi} porsi Mie Ayam Biasa = Rp{total1}")
            jenis1 = ("Mie Ayam Biasa")

        elif nomor == 4:
            total1 = porsi * 15000
            print (f"{porsi} porsi Mie Ayam Bakso = Rp{total1}")
            jenis1 = ("Mie Ayam Bakso")

        break

nomor = int(input("Masukan Pilihan Minuman: "))
gelas = int(input("Berapa Gelas: "))
if nomor == 1:
    total2 = gelas * 3000
    print (f"{gelas} Es Teh = Rp{total2}")
    jenis2 = ("Gelas Es Teh")

elif nomor == 2:
    total2 = gelas * 5000
    print (f"{gelas} Gelas Es Jeruk = Rp{total2}")
    jenis2 = ("Es Jeruk")

else:
    while True:
        print("Pilihan tidak ada, silahkan masukan lagi")
        nomor = int(input("Masukan Pilihan Minuman: "))
        gelas = int(input("Berapa Gelas: "))
        if nomor == 1:
            total2 = gelas * 3000
            print (f"{gelas} Es Teh = Rp{total2}")
            jenis2 = (" Gelas Es Teh")

        elif nomor == 2:
            total2 = gelas * 5000
            print (f"{gelas} Gelas Es Jeruk = Rp{total2}")
            jenis2 = ("Es Jeruk")
        break

totalsemua = total1 + total2
print(f"total semua = Rp{totalsemua}")
listhari = ["senin", "SENIN", "jumat", "JUMAT"]
def diskon():
    global diskon
    hari = input("hari pembelian: ")
    diskon = 0
    if hari in listhari:
        if totalsemua >= 300000:
            diskon = int((25/100) * totalsemua)
            if diskon > 100000:
                diskon = 100000
            print("Anda mendapatkan diskon 25% s.d. Rp100.000")

        elif totalsemua >= 150000 and totalsemua < 300000:
            diskon = int((10/100) * totalsemua)
            print("Anda mendapatkan diskon 10%")

        elif totalsemua >= 80000 and totalsemua < 150000:
            diskon = int((5/100) * totalsemua)
            print("Anda mendapatkan diskon 5%")

        else:
            print("Anda tidak mendapatkan diskon.")

    else:
        print("Anda tidak mendapatkan diskon.")
    print(f"diskon yang Anda dapat = Rp{diskon}")

diskon()

totaltagihan = totalsemua - diskon
print(f"\nTotal harus Dibayar: Rp{totaltagihan}")
uang = int(input("Uang Tunai Pembeli: Rp"))
kembalian = int(uang - totaltagihan)
print(f"Kembalian: Rp{kembalian}")

print(f"""
---------------------------------------------
------------ S T R U K   B E L I ------------
---------------------------------------------
Nama          : {pembeli}
Beli          : {porsi} porsi {jenis1} - Rp{total1}
                {gelas} {jenis2} - Rp{total2}
Total         : Rp{totalsemua}
Diskon        : - Rp{diskon}
Total Tagihan : Rp{totaltagihan}
Uang          : Rp{uang}
Kembalian     : Rp{kembalian}
---------------------------------------------
 Terima kasih telah beli di DEPOT KANG UJANG 
---------------------------------------------""")
