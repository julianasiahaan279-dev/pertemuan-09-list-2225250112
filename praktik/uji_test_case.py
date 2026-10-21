def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil

print(f"Rata-rata [60, 70, 80] = {rata_rata([60, 70, 80]):.2f}")
print(f"Min / Maks [60, 70, 80] = {min([60, 70, 80])} / {max([60, 70, 80])}")
print(f"Jumlah lulus [60, 70, 80] = {len(nilai_lulus([60, 70, 80]))}")
print(f"Jumlah lulus [59, 60, 61] = {len(nilai_lulus([59, 60, 61]))}")
print(f"Rata-rata [] = {rata_rata([])}")