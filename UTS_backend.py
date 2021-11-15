skincare = ["Lacoco", "Npure", "Cosrx"]
lacoco = ["Dark Spot essence", "Watermelon Glow Mask", "Eye Serum", "Bakuchiol Essence"]
npure = ["Npure Face Toner", "Npure Clay Mask", "Npure Sunscreen", "Npure Cica Clear Pad"]
cosrx = ["AHA/BHA Toner", "Low pH Cleanser", "Centella Blemish Cream", "Advanced snail Cream"]
keranjang = []

while True:
    print("========================================")
    print("=            COSMETIC HOUSE            =")
    print("=               SKINCARE               =")
    print("========================================")
    print("========================================")
    print("=              1. Lacoco               =")
    print("=              2. Npure                =")
    print("=              3. Cosrx                =")
    print("----------------------------------------")
    skincare = input("Silahkan pilih [1-3] :")
    print(" ")

    if skincare == "1":
        print("========================================")
        print("    Anda memilih angka 1 yaitu Lacoco   ")
        print("           Daftar Produk Lacoco         ")
        print("========================================")
        while True:
            for a in range(0, len(lacoco)):
                print(f'{a + 1}. {lacoco[a]}')
            print("----------------------------------------")
            p_lacoco = int(input("Masukkan produk yang akan dibeli [1-4]: "))
            print(" ")
            if p_lacoco == 1:
                keranjang.append(lacoco[0])
            elif p_lacoco == 2:
                keranjang.append(lacoco[1])
            elif p_lacoco == 3:
                keranjang.append(lacoco[2])
            elif p_lacoco == 4:
                keranjang.append(lacoco[3])
            else:
                print("========================================")
                print("=        Produk Tidak Tersedia         =")
                print("= Silahkan pilih produk yang tersedia  =")
                print("========================================")
                continue
            print('============ list keranjang ============')
            for b in range(0, len(keranjang)):
                print(f'{b +1} {keranjang[b]}')
            break
    elif skincare == "2":
        print("========================================")
        print("    Anda memilih angka 2 yaitu Npure    ")
        print("           Daftar Produk Npure          ")
        print("========================================")
        while True:
            for a in range(0, len(npure)):
                print(f'{a + 1}. {npure[a]}')
            print("----------------------------------------")
            p_npure = int(input("Masukkan produk yang akan dibeli [1-4]: "))
            print(" ")
            if p_npure == 1:
                keranjang.append(npure[0])
            elif p_npure == 2:
                keranjang.append(npure[1])
            elif p_npure == 3:
                keranjang.append(npure[2])
            elif p_npure == 4:
                keranjang.append(npure[3])
            else:
                print("========================================")
                print("=        Produk Tidak Tersedia         =")
                print("= Silahkan pilih produk yang tersedia  =")
                print("========================================")
                continue
            print('============ list keranjang ============')
            for b in range(0, len(keranjang)):
                print(f'{b +1} {keranjang[b]}')
            break
    elif skincare == "3":
        print("========================================")
        print("    Anda memilih angka 3 yaitu Cosrx    ")
        print("           Daftar Produk Cosrx          ")
        print("========================================")
        while True:
            for a in range(0, len(cosrx)):
                print(f'{a + 1}. {cosrx[a]}')
            print("----------------------------------------")
            p_cosrx = int(input("Masukkan produk yang akan dibeli [1-4]: "))
            print(" ")
            if p_cosrx == 1:
                keranjang.append(cosrx[0])
            elif p_cosrx == 2:
                keranjang.append(cosrx[1])
            elif p_cosrx == 3:
                keranjang.append(cosrx[2])
            elif p_cosrx == 4:
                keranjang.append(cosrx[3])
            else:
                print("========================================")
                print("=        Produk Tidak Tersedia         =")
                print("= Silahkan pilih produk yang tersedia  =")
                print("========================================")
                continue
            print('============ list keranjang ============')
            for b in range(0, len(keranjang)):
                print(f'{b +1} {keranjang[b]}')
            break
    else:
        print(" ")
        print("               ==========               ")
        print("         Produk Tidak ditemukan         ")
        print("  Silahkan pilih produk yang tersedia   ")
        print("               ==========               ")
        print(" ")
        continue

    print(" ")
    print("----------------------------------------")
    tanya = input("Ada tambahan lagi ? [Y/N]")
    if tanya == "y" or tanya == "Y":
        continue
    else:
        print(" ")
        print(" ")
        print("               ==========               ")
        print("Terimakasih Telah Berbelanja ditoko Kami")
        print("             Happy Shopping             ")
        print("               ==========               ")
        break
