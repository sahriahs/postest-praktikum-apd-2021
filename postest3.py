print("================ KONVERSI MATA UANG IDR ================ \n")

print("daftar mata uang yang dapat dikonversi: ")
Daftar = ["1. IDR - USD", "2. IDR - SGD", "3. IDR - EUR", "4. IDR - JYP", "5. Keluar dari program."]
for i in Daftar:
    print(i)
print("")

berhenti = False
while not berhenti:
    pilih_daftar = input("pilih daftar (1, 2, 3, 4, atau 5 untuk keluar dari program): ")
    if pilih_daftar == "1":
        IDR = int(input("masukkan nilai IDR:"))
        USD = float(IDR * 0.000071)
        print(f"{IDR} IDR = {USD} USD\n")

    elif pilih_daftar == "2":
        IDR = int(input("masukkan nilai IDR:"))
        SGD = float(IDR * 0.000095)
        print(f"{IDR} IDR = {SGD} SGD\n")

    elif pilih_daftar == "3":
        IDR = int(input("masukkan nilai IDR:"))
        EUR = float(IDR * 0.000061)
        print(f"{IDR} IDR = {EUR} EUR\n")

    elif pilih_daftar == "4":
        IDR = int(input("masukkan nilai IDR:"))
        JYP = float(IDR * 0.0080)
        print(f"{IDR} IDR = {JYP} JYP\n")

    elif pilih_daftar == "5":
        print("Anda keluar dari program.")
        berhenti = True

    else:
        print("Tolong perhatikan lagi daftar pilihan yang kamu masukan ya\n\r")

print("\n========================================================")