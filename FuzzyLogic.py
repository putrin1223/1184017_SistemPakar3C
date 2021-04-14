import csv

#  1. LINGUISTIC
#
#     Income      |      LOW(L)      BELOW AVERAGE(B)       AVERAGE(A)      HIGH(H)
#     Debt        |      FEW(F)      NORMAL(N)       MUCH(M)
#     ------------
#     Acceptance  |      YES        MAYBE       NO

#  2. MEMBERSHIP FUNCTION
#     Ada pada laporan

#  3. FUZZIFICATION

#  INCOME SCORE CALCULATION
def lowIncome(x):  # For low income
    if x <= 0.3:
        return 1
    elif x >= 0.8:
        return 0
    else:
        return (0.8 - x) / (0.8 - 0.3)


def baIncome(x):  # For below average income
    if 0.6 <= x <= 1:
        return 1
    elif 0.4 < x < 0.6:
        return (x - 0.4) / (0.6 - 0.4)
    elif 1 < x < 1.2:
        return (1.2 - x) / (1.2 - 1)
    else:
        return 0


def avIncome(x):  # For average income
    if 1.0 <= x <= 1.4:
        return 1
    elif 0.8 < x < 1.0:
        return (x - 0.8) / (1.0 - 0.8)
    elif 1.4 < x < 1.6:
        return (1.6 - x) / (1.6 - 1.4)
    else:
        return 0


def highIncome(x):  # For high income
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


# DEBT SCORE CALCULATION
def fewDebt(y):  # Few debts
    if y <= 30:
        return 1
    elif y >= 50:
        return 0
    else:
        return (50 - y) / (50 - 30)


def normalDebt(y):  # Normal debts
    if 50 <= y <= 70:
        return 1
    elif 30 < y < 50:
        return (y - 30) / (50 - 30)
    elif 70 < y < 80:
        return (80 - y) / (80 - 70)
    else:
        return 0


def muchDebt(y):  # Much debts
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


# 4. RULE

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


# 5. INFERENCE
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


#  6.DEFUZZIFICATION
def sugenoDefuz(yes, no, maybe):                            # Constant values are set to 87, 70, and 52
    return ((yes * 87) + (maybe * 70) + (no * 52)) / (yes + maybe + no)


#  7. MAIN PROGRAM
income = []                                                 # Initialize the 'income' array
debt = []                                                   # Initialize the 'debt' array
bltScore = []                                               # Initialize the 'bltScore' array
bltFinal = []                                               # Initialize the 'bltFinal' array

with open('DataTugas2.csv', mode='r') as csv_input:         # Input from DataTugas2.csv file
    bltData = csv.reader(csv_input)
    next(bltData)                                           # Skip the first row
    for row in bltData:
        income.append(float(row[1]))                        # Insert second column to 'income' array
        debt.append(float(row[2]))                          # Insert third column to 'debt' array

for i in range(len(income)):                                # Looping for every person
    L, B, A, H = incomeValue(income[i])                     # Calculate the score for income categories
    F, N, M = debtValue(debt[i])                            # Calculate the score for debt categories
    yes, maybe, no = inference(L, B, A, H, F, N, M)         # Calculate the score for acceptance categories
    score = sugenoDefuz(yes, no, maybe)                     # Calculate the final score
    bltScore.append([score, (i + 1)])                       # Insert the final scores to array
bltScore.sort(reverse=True)                                 # Sort the scores array

for i in range(0, 20):                                      # Loop for 20 datas
    bltFinal.append(bltScore[i][1])                         # Insert the accepted person's numbers to array

with open('TebakanTugas2.csv', mode="w") as csv_output:     # Output to *.csv file
    bltOut = csv.writer(csv_output, lineterminator='\n')
    for data in bltFinal:                                   # Looping for every data in 'bltFinal' array
        bltOut.writerow([data])                             # Write data to *.csv file

print(income)
print(debt)
print(bltScore)
print(bltFinal)
