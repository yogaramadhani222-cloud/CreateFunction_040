def convert(nilai, unit):
    if unit == 'C':
        nilai = (nilai * 9/5) + 32
        return nilai
    elif unit == 'F':
        nilai = (nilai - 32) * 5/9
        return nilai
    else:
        return "unit tidak valid"
nilai = float(input("Masukkan nilai suhu: "))
unit = input("Masukkan unit suhu (C/F): ")
print(convert(nilai, unit))