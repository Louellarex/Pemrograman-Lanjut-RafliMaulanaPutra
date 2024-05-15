#TB 1 Pemrograman Lanjut
# Rafli Maulana Putra (41823010058)

#Mendekode Matrix
def dekode_matrix(input_matrix):
    barisan, colums=map(int, input_matrix[0].split())
    #fungsi map() mengembalikan objek peta (yang merupakan iterator) dari hasil setelah menerapkan fungsi yang diberikan ke setiap item dari iterable yang diberikan

    matrix=[]

    for baris in input_matrix[1:]:
        matrix.append(list(baris))

    dekode_text= ''
    for colum in range(colums):
        for baris in range(barisan):
            # Jika karakter bukan alfanumerik, ganti dengan spasi
            if not matrix[baris] [colum].isalnum():
                dekode_text += ' '
            else:
                dekode_text += matrix[baris] [colum]

    return dekode_text

# Matrix script
input_matrix = [
    '7 3',
    'Tsi',
    'h%x',
    'i #',
    'sM ',
    '$a ',
    '#t%',
    'ir!'
]

# Mengoutput hasil
print(dekode_matrix(input_matrix))
