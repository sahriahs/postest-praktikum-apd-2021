#2. Buatlah Program sederhana dengan inputan biodata, dengan :
#-Variable inputan minimal 5 
#    a.Nama
#    b.NIM
#    c.dan seterusnya
#-Menggunakan tipe data STR,INT,FLOAT(Wajb)
#-Output dibuat sekreatif mungkin
#-Ditekaankan untuk menggunakan List
#   *Modul 4

print("========= PROGRAM SEDERHANA INPUTAN BIODATA =========\n")

biodata = []
#biodata mahawiswa
nama = str(input("masukkan nama: "))
biodata.append(nama)

NIM = int(input("masukkan NIM: "))
biodata.append(NIM)

prodi = str(input("masukkan program studi: "))
biodata.append(prodi)

angkatan = int(input("masukkan angkatan: "))
biodata.append(angkatan)

perguruan_tinggi = str(input("masukkan nama perguruan tinggi: "))
biodata.append(perguruan_tinggi)

tinggi_badan = float(input("masukkan tinggi badan: "))
biodata.append(tinggi_badan)

berat_badan = float(input("masukkan berat badan: "))
biodata.append(berat_badan)

print(f"""\nBIODATA MAHASISWA;
    Nama             : {biodata[0]}
    NIM              : {biodata[1]}
    Program Studi    : {biodata[2]}
    Angkatan         : {biodata[3]}
    Perguruan Tinggi : {biodata[4]}
    Tinggi Badan     : {biodata[5]} meter
    Berat Badan      : {biodata[6]} kg
    """)

print("=====================================================")