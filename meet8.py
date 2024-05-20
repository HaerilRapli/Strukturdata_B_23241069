# perbandingan lanjutan 
MasukanUser = (input("masukan bilangan kurang dari 3 atau lebih dari 9:"))

# -----cek kurang dari 3
kurDar =(MasukanUser < 3)
print("kurang dari 3 =", kurDar)

# -----cek kurang dari 9
lebDar =(MasukanUser > 9)
print("lebih dari 9 =", lebDar)

betul = kurDar and lebDar
print ("pengecekan final :", betul)

# ---------4 ++++++++++++14-------
MasukanUser = float(input("masukan bilangan antara 4 dan 14 :"))
hasil = (4 < MasukanUser < 14)
print(hasil)

#----5++++++++9---------12++++++++++30------------prs