# Implementasi Algoritma Floyd
def floyd(matriks_tetangga):
    n = len(matriks_tetangga)
    
    # Inisialisasi matriks jarak
    jarak = [baris[:] for baris in matriks_tetangga]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                jarak[i][j] = min(jarak[i][j], jarak[i][k] + jarak[k][j])

    return jarak

# Implementasi Algoritma Warshall
def warshall(matriks_tetangga):
    n = len(matriks_tetangga)

    # Inisialisasi matriks keberadaan jalur langsung
    jalur_langsung = [baris[:] for baris in matriks_tetangga]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                jalur_langsung[i][j] = jalur_langsung[i][j] or (jalur_langsung[i][k] and jalur_langsung[k][j])

    return jalur_langsung

# Fungsi untuk mencetak matriks
def cetak_matriks(matriks, nama):
    print(f"{nama}:")
    for baris in matriks:
        print(baris)

# Fungsi untuk mencetak matriks awal
def cetak_matriks_awal(matriks_tetangga):
    print("\nMatriks Awal:")
    for baris in matriks_tetangga:
        print(baris)

# Contoh penggunaan
matriks_tetangga = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

cetak_matriks_awal(matriks_tetangga)

hasil_floyd = floyd(matriks_tetangga)
hasil_warshall = warshall(matriks_tetangga)

cetak_matriks(hasil_floyd, "\nMatriks Jarak (Floyd)")
cetak_matriks(hasil_warshall, "\nMatriks Jalur Langsung (Warshall)")
