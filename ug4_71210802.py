import json

with open('mahasiswa.json', 'r+') as datafile:
    data = []

    mhs = int(input("Masukan jumlah mahasiswa baru : "))

    for i in range(0, mhs):
       
        name = input("Masukan nama Anda : ")
        a = []
        b = {}
        jml_hobi = int(input("Masukan Jumlah hobi : "))
        a_hobi = []
        for j in range(1, jml_hobi+1):
            hobi = input("Masukan Hobi ke-{index} : ".format(index=j))
            a_hobi.append(hobi)

        prestasi = input("Masukan Prestasi Anda : ")

        a.append({"BioData":{"Hobi":a_hobi,"Prestasi":prestasi}})
        data[name] = a

        print("=== Data berhasil ditambahkan ===")
        print()

#tambahkan data ke json
with open('mahasiswa.json', 'w') as datafile:
    json.dump(data, datafile)