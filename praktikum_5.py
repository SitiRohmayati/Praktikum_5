daftar = {}
while True:
    print("")
    r = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari (K)eluar] : ")
    if r.lower()== 'k' :
        print("Terima Kasih")
        break
        
    elif r.lower()=='l' :
        print("Daftar Nilai")
        print("======================================================================")
        print(" | No |   Nama    |    NIM     |  Tugas   | UTS  |  UAS  |  Akhir    |")
        print("======================================================================")
        i=0
        for x in daftar.items() :
            i+=1
            print(" | {6:2} |{0:11s}|{1:12}|{2:10d}|{3:6d}|{4:7d}|{5:11.2f}|"\
                  .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        print("======================================================================")
    elif r.lower()=='t' :
        print("Tambah Data")
        nama       = input    ("Nama        : ")
        nim        = input    ("NIM         : ")
        nilaitugas = int(input("Nilai Tugas : "))
        nilaiuts   = int(input("Nilai UTS   : "))
        nilaiuas   = int(input("Nilai UAS   : "))
        akhir      = ((nilaitugas)*30/100 + (nilaiuts)*35/100 + (nilaiuas)*35/100)
        daftar[nama] = nim, nilaitugas, nilaiuts, nilaiuas, akhir
    elif r.lower ()== 'u':
        print("Ubah Data")
        nama = input ("Masukan Nama : ")
        if nama in daftar.keys():
            nim        = input    ("NIM         :")
            nilaitugas = int(input("Nilai Tugas : "))
            nilaiuts   = int(input("Nilai UTS   : "))
            nilaiuas   = int(input("Nilai UAS   : "))
            daftar[nama] = nim, nilaitugas, nilaiuts, nilaiuas, akhir
        else :
            print("daftar {0} tidak ada".format(nama))
    elif r.lower()=='h':
        print("Hapus Kontak")
        nama = input("Nama : ")
        if nama in daftar.keys():
            del daftar[nama]
        else:
            print("daftar {0} tidak ada".format(nama))
        
    elif r.lower()=='c':
        print("Cari Daftar")
        nama= input("Nama : ")
        if nama in daftar.keys():
            print("================================================")
            print("|  Nama  |   NIM   | Tugas | UTS | UAS | Akhir |")
            print("================================================")
            print("| {0:8s}|{1:9}|{2:7d}|{3:5d}|{4:5d}|{5:7.2f}|"\
                  .format(nama, nim, nilaitugas, nilaiuts, nilaiuas, akhir))
            print("================================================")
        else :
            print("daftar {0} tidak ada".format(nama))
    else :
        print("Daftar Nilai")
        print("======================================================================")
        print(" | No |   Nama    |    NIM     |  Tugas   | UTS  |  UAS  |  Akhir    |")
        print("======================================================================")
        print(" |                      TIDAK ADA DATA                               |")
        print("======================================================================")
        
