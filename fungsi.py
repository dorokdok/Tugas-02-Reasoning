import numpy as np
import pandas as pd
from typing import List

listFloat = List[float]
Fuzifikasi = List[listFloat]

#Function Fuzifikasi Servis
def FuzifikasiServis (inputan: float) -> listFloat :
    bagus = float
    tengah = float
    jelek = float
    #Bagus
    #Jika Servis > 85 maka bagus = 1
    if inputan > 85 :
        bagus = 1
    #Jika Servis 60-85 maka servis-60/85-60
    elif inputan > 60 and inputan <= 85 :
        bagus = (inputan-60)/(85-60)
    #Jika servis di bawah 60 maka bagus = 0
    else :
        bagus = 0
    #Menengah
    #Jika servis > 80 atau < 40 maka tengah = 0
    if inputan > 80 or inputan <= 40:
        tengah = 0
    #Jika 45 < servis < 55 maka tengah = 1
    elif inputan > 45 and inputan < 55:
        tengah = 1
    #Jika 55 <= servis <= 80 maka tengah = rumus
    elif inputan >= 55 and inputan <= 80 :
        tengah = (80 - inputan)/(80-55)
    #Jika 40 < servis <= 45 maka tengah = rumus
    elif inputan > 40 and inputan <= 45 :
        tengah = (inputan - 40)/(45-40)
    # jelek    
    #Jika servis > 40 maka jelek = 0
    if inputan > 40:
        jelek = 0
    #Jika servis <= 10 make jelek = 1
    elif inputan > 0 and inputan <= 10:
        jelek = 1
    #Jika 10 < servis <= 45 maka jelek = rumus
    elif inputan > 10 and inputan <= 45:
        jelek = (inputan - 10)/(55-10)
    return [bagus,tengah,jelek]

#Function Fuzifikasi Harga
def FuzifikasiHarga (inputan: float) -> listFloat :
    mahal = float
    tengah = float
    murah = float
    #mahal
    #Jika harga > 8 maka mahal = 1
    if inputan > 8 :
        mahal = 1
    #Jika 6 < harga <= 8 maka mahal = rumus
    elif inputan > 6 and inputan <= 8 :
        mahal = (inputan-6)/(8-6)
    #Jika di bawah 6 maka mahal = 0
    else :
        mahal = 0
    #Menengah
    #Jika harga > 8 atau harga <= 4 maka tengah = 0
    if inputan > 8 or inputan <= 3:
        tengah = 0
    #Jika 4 < harga < 5 maka tengah = 1
    elif inputan > 4 and inputan < 5:
        tengah = 1
    #Jika 5 < harga <= 7 maka tengah = rumus
    elif inputan >= 5 and inputan <= 8 :
        tengah = (8 - inputan)/(8-5)
    #Jika 3 < harga <= 4 maka tengah = rumus
    elif inputan > 3 and inputan <= 4 :
        tengah = (inputan - 3)/(4-3)
    #murah
    #Jika Harga > 4 maka murah = 0   
    if inputan > 4:
        murah = 0
    #Jika harga <= 2 maka murah = 1
    elif inputan > 0 and inputan <= 2:
        murah = 1
    #jika 2 < harga <= 4 maka murah = rumus
    elif inputan > 2 and inputan <= 4:
        murah = (inputan - 2)/(4-2)
    return [mahal,tengah,murah]

#Inference dengan aturan
def inference(servis: Fuzifikasi, harga: Fuzifikasi) -> Fuzifikasi:
    out = Fuzifikasi
    out = []
    pasti = listFloat
    mungkin = listFloat
    tidak = listFloat
    
    for i in range(len(servis)):
        dmp = Fuzifikasi
        dmp = []
        pasti = []
        mungkin = []
        tidak = []
        for j in range(len(servis[i])):
            if servis[i][j] >= 0.3:
                if j == 0 :
                    #Jika bagus dan mahal maka mungkin
                    if harga[i][0] >= 0.3:
                        if servis[i][j] < harga[i][0]:
                            mungkin.append(servis[i][j])
                        else:
                            mungkin.append(harga[i][0])
                    #Jika bagus dan tengah/rata" maka pasti
                    if harga[i][1] >= 0.3:
                        if servis[i][j] < harga[i][1]:
                            pasti.append(servis[i][j])
                        else:
                            pasti.append(harga[i][1])
                    #Jika bagus dan murah maka pasti
                    if harga[i][2] >= 0.3:
                        if servis[i][j] < harga[i][2]:
                            pasti.append(servis[i][j])
                        else:
                            pasti.append(harga[i][2])
                if j == 1:
                    #Jika tengah/rata" dan mahal maka tidak
                    if harga[i][0] >= 0.3:
                        if servis[i][j] <= harga[i][0]:
                            tidak.append(servis[i][j])
                        else:
                            tidak.append(harga[i][0])
                    #Jika tengah dan tengah maka mungkin
                    if harga[i][1] >= 0.3:
                        if servis[i][j] <= harga[i][1]:
                            mungkin.append(servis[i][j])
                        else:
                            mungkin.append(harga[i][1])
                    #Jika tengah dan murah maka mungkin
                    if harga[i][2] >= 0.3:
                        if servis[i][j] <= harga[i][2]:
                            mungkin.append(servis[i][j])
                        else:
                            mungkin.append(harga[i][2])
                if j == 2:
                    #Jika jelek dan mahal/sedang/murah maka tidak
                    if harga[i][0] >= 0.3:
                        if servis[i][j] < harga[i][0]:
                            tidak.append(servis[i][j])
                        else:
                            tidak.append(harga[i][0])
                    if harga[i][1] >= 0.3:
                        if servis[i][j] < harga[i][1]:
                            tidak.append(servis[i][j])
                        else:
                            tidak.append(harga[i][1])
                    if harga[i][2] >= 0.3:
                        if servis[i][j] < harga[i][2]:
                            tidak.append(servis[i][j])
                        else:
                            tidak.append(harga[i][2])
        pasti.sort()
        mungkin.sort()
        tidak.sort()
        #Untuk mencari nilai pasti/mungkin/tidak terendah
        if len(pasti) > 0:
            dmp.append(pasti[0])
        else:
            dmp.append(0)
        if len(mungkin) > 0:
            dmp.append(mungkin[0])
        else:
            dmp.append(0)
        if len(tidak) > 0:
            dmp.append(tidak[0])
        else:
            dmp.append(0)
        out.append(dmp)

    return out

#Defuzzifikasi menggunakan sugeno
#pasti * 100 + mungkin * 50 + murah *30 /pasti+mungkin+tidak
def defuzzy(inputan: listFloat) -> float:
    pembagi = inputan[0]+inputan[1]+inputan[2]
    if pembagi == 0:
        return 0
    else:
        return ((inputan[0]*100+inputan[1]*50+inputan[2]*30)/pembagi)