import math

def hitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

def hitung_volume_bola(jari_jari):
    volume = (4/3) * math.pi * (jari_jari ** 3)
    return volume

def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

def main():
    while True:
        print("\nPilih operasi yang ingin Anda lakukan:")
        print("1. Hitung Luas Segitiga??")
        print("2. Hitung Volume Bola??")
        print("3. Hitung Volume Balok??")
        print("4. Keluar")

        pilihan = input("Masukkan nomor pilihan Anda [ 1,2,3 atau 4?]: ")

        if pilihan == '1':
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = hitung_luas_segitiga(alas, tinggi)
            print("Luas segitiga:", luas)
        elif pilihan == '2':
            jari_jari = float(input("Masukkan jari-jari bola: "))
            volume = hitung_volume_bola(jari_jari)
            print("Volume bola:", volume)
        elif pilihan == '3':
            panjang = float(input("Masukkan panjang balok: "))
            lebar = float(input("Masukkan lebar balok: "))
            tinggi = float(input("Masukkan tinggi balok: "))
            volume = hitung_volume_balok(panjang, lebar, tinggi)
            print("Volume balok:", volume)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
