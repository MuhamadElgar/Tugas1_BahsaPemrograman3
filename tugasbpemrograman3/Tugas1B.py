def calculate_imt(weight, height):
    imt = weight / (height ** 2)
    return imt

def determine_status(imt):
    if imt < 18.5:
        status = "Underweight (Kurus)"
    elif 18.5 <= imt <= 22.9:
        status = "Normal range (Normal)"
    elif 23 <= imt <= 24.9:
        status = "Overweight (Berlebih)"
    elif 25 <= imt <= 29.9:
        status = "Pre-obese (Pra-obesitas)"
    elif 30 <= imt <= 34.9:
        status = "Obese class 1 (Obesitas kelas 1)"
    elif 35 <= imt <= 39.9:
        status = "Obese class 2 (Obesitas kelas 2)"
    else:
        status = "Obese class 3 (Obesitas kelas 3)"
    return status

def main():
    print("Aplikasi untuk menghitung Indeks Massa Tubuh (IMT)")
    print("==============================================")
    weight = float(input("Masukkan berat badan Anda (kg): "))
    height = float(input("Masukkan tinggi badan Anda (m): "))

    imt = calculate_imt(weight, height)
    status = determine_status(imt)

    print(f"\nIMT Anda adalah {imt:.2f}")
    print(f"Status gizi Anda adalah: {status}")

if __name__ == "__main__":
    main()
