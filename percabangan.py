# percabangan

jumlah_botol_susu = 173
jumlah_telur = 589
print(f"jumlah botol susu", {jumlah_botol_susu}, "btl")
print(f"jumlah telur", {jumlah_telur}, "btr")
if jumlah_botol_susu > 0 :
    print("Budi mengecek harganya, dan ternyata cukup")
    if jumlah_telur > 0 :
        print("Budi membeli 1 botol susu")
        print("Budi membeli 6 butir telur")
    else:
        print("Budi membeli 1 botol susu dan tidak membeli telur")


else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Budi menyerahkan belanjaannya pada Ibu")