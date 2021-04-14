import csv
def lowIncome(x):  # Untuk berpenghasilan rendah
    if x <= 0.3:
        return 1
    elif x >= 0.8:
        return 0
    else:
        return (0.8 - x) / (0.8 - 0.3)


def baIncome(x):  # Untuk pendapatan di bawah rata-rata
    if 0.6 <= x <= 1:
        return 1
    elif 0.4 < x < 0.6:
        return (x - 0.4) / (0.6 - 0.4)
    elif 1 < x < 1.2:
        return (1.2 - x) / (1.2 - 1)
    else:
        return 0


def avIncome(x):  # Untuk pendapatan rata-rata
    if 1.0 <= x <= 1.4:
        return 1
    elif 0.8 < x < 1.0:
        return (x - 0.8) / (1.0 - 0.8)
    elif 1.4 < x < 1.6:
        return (1.6 - x) / (1.6 - 1.4)
    else:
        return 0


def highIncome(x):  # Untuk berpenghasilan tinggi
    if x >= 1.7:
        return 1
    elif x <= 1.2:
        return 0
    else:
        return (x - 1.2) / (1.7 - 1.2)


def incomeValue(x):
    L = lowIncome(x)
    B = baIncome(x)
    A = avIncome(x)
    H = highIncome(x)
    return L, B, A, H


# PERHITUNGAN SKOR HUTANG
def fewDebt(y):  # Few debts
    if y <= 30:
        return 1
    elif y >= 50:
        return 0
    else:
        return (50 - y) / (50 - 30)


def normalDebt(y):  # Hutang normal
    if 50 <= y <= 70:
        return 1
    elif 30 < y < 50:
        return (y - 30) / (50 - 30)
    elif 70 < y < 80:
        return (80 - y) / (80 - 70)
    else:
        return 0


def muchDebt(y):  # Banyak hutang
    if y >= 80:
        return 1
    elif y <= 60:
        return 0
    else:
        return (y - 60) / (80 - 60)


def debtValue(y):
    F = fewDebt(y)
    N = normalDebt(y)
    M = muchDebt(y)
    return F, N, M


# 4.ATURAN

# INCOME            DEBTS           ACCEPTANCE
# L                 F               MAYBE
# L                 N               YES
# L                 M               YES
# B                 F               MAYBE
# B                 N               MAYBE
# B                 M               YES
# A                 F               NO
# A                 N               MAYBE
# A                 M               MAYBE
# H                 F               NO
# H                 N               NO
# H                 M               MAYBE


# 5. KESIMPULAN

def inference(L, B, A, H, F, N, M):
    R = [[min(L, F), 'M'], [min(B, F), 'M'], [min(A, F), 'N'], [min(H, F), 'N'], [min(L, N), 'Y'], [min(B, N), 'M'],
         [min(A, N), 'M'], [min(H, N), 'N'], [min(L, M), 'Y'], [min(B, M), 'Y'], [min(A, M), 'M'], [min(H, M), 'M']]
    maybe = []
    no = []
    yes = []
    for i in range(len(R)):
        if R[i][1] == 'M':
            maybe.append(R[i][0])
        elif R[i][1] == 'N':
            no.append(R[i][0])
        elif R[i][1] == 'Y':
            yes.append(R[i][0])
    return max(yes), max(maybe), max(no)


#  6.DEFUZIFIKASI
def sugenoDefuz(yes, no, maybe):                            # Constant values are set to 87, 70, and 52
    return ((yes * 87) + (maybe * 70) + (no * 52)) / (yes + maybe + no)


#  7. PROGRAM UTAMA
income = []                                                 # Inisialisasi array 'income'
debt = []                                                   # Imenginisialisasi array 'hutang'
bltScore = []                                               # Inisialisasi array 'bltScore'
bltFinal = []                                               # Inisialisasi array 'bltFinal'

with open('DataTugas2.csv', mode='r') as csv_input:         # Masukan dari file DataTugas2.csv
    bltData = csv.reader(csv_input)
    next(bltData)                                           # Lewati baris pertama
    for row in bltData:
        income.append(float(row[1]))                        # Masukkan kolom kedua ke larik 'pendapatan'
        debt.append(float(row[2]))                          # Masukkan kolom ketiga ke array 'hutang'

for i in range(len(income)):                                # Pendauran untuk setiap orang
    L, B, A, H = incomeValue(income[i])                     # Hitung skor untuk kategori pendapatan 
    F, N, M = debtValue(debt[i])                            # Hitung skor untuk kategori hutang
    yes, maybe, no = inference(L, B, A, H, F, N, M)         # Hitung skor untuk kategori penerimaan
    score = sugenoDefuz(yes, no, maybe)                     # Hitung skor akhir
    bltScore.append([score, (i + 1)])                       # Masukkan skor akhir ke larik
bltScore.sort(reverse=True)                                 # Urutkan larik skor

for i in range(0, 20):                                      # Ulangi untuk 20 data
    bltFinal.append(bltScore[i][1])                         # Masukkan nomor orang yang diterima ke larik

with open('TebakanTugas2.csv', mode="w") as csv_output:     # Output ke file * .csv
    bltOut = csv.writer(csv_output, lineterminator='\n')
    for data in bltFinal:                                   # Perulangan untuk setiap data dalam larik 'bltFinal'
        bltOut.writerow([data])                             # Tulis data ke file * .csv

print(income)
print(debt)
print(bltScore)
print(bltFinal)
