# Створити програму, яка приймає секунди та переводить їх у формат HH:MM:SS
S = int(input("Input seconds : "))
M = S//60
H = M//60
M = M - (H * 60)
S = S - ((M * 60) + (H * 3600))
print(str(H) + "h:" + str(M) + "m:" + str(S) + "s")