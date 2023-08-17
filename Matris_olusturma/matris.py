import numpy as np

matris1 = np.random.randint(0, 255, size=(3, 3))
matris2 = np.random.randint(0, 255, size=(3, 3))

for i in range(3):
    for j in range(3):
        matris1[i][j] = np.random.randint(0, 256)
        matris2[i][j] = np.random.randint(0, 256)
print("Matris 1:")
print(matris1)
print("\nMatris 2:")
print(matris2)
toplam = np.zeros((3, 3), dtype=int)
cikarma = np.zeros((3, 3), dtype=int)
carpma = np.zeros((3, 3), dtype=int)
for i in range(3):
    for j in range(3): #döngü oluşturduk 
        toplam[i][j] = matris1[i][j] + matris2[i][j]
        if toplam[i][j] > 256:
            toplam[i][j] = 255 #toplamayı yaptırdık 
        cikarma[i][j] = matris1[i][j] - matris2[i][j]
        if cikarma[i][j] < 0:
            cikarma[i][j] = 0 #çıkarmayı yaptırdık.
        carpma[i][j] = matris1[i][j] * matris2[i][j]
        if carpma[i][j] > 256:
            carpma[i][j] = 255 #çarpmayı yaptırdık
print("\nToplama Matrisi:")
print(toplam)
print("\nÇıkarma Matrisi:")
print(cikarma)
print("\nÇarpma Matrisi:")
print(carpma)
