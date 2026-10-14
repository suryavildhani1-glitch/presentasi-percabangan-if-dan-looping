data_siswa = [
    {"nama": "budi", "nilai": 83},
    {"nama": "anto", "nilai": 90},
    {"nama": "rara", "nilai": 76},
    {"nama": "fira", "nilai": 65}
]

kkm = 75

print("===Data Nilai Siswa===")

for siswa in data_siswa:
    nama = siswa["nama"]
    nilai = siswa["nilai"]

    if nilai >= kkm:
        keterangan = "Lulus"
    else:
        keterangan = "Tidak Lulus"

    print(f"nama: {nama:<4} | nilai: {nilai} | keterangan: {keterangan}")