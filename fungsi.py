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
    if inputan > 85 :
        bagus = 1
    elif inputan > 60 :
        bagus = (inputan-60)/(100-60)
    else :
        bagus = 0
    #Menengah
    if inputan > 80 or inputan <= 40:
        tengah = 0
    elif inputan > 45 and inputan < 55:
        tengah = 1
    elif inputan > 55 and inputan <= 80 :
        tengah = (80 - inputan)/(80-55)
    elif inputan > 40 and inputan <= 45 :
        tengah = (inputan - 40)/(45-40)
    # jelek    
    if inputan > 40:
        jelek = 0
    elif inputan > 0 and inputan <= 10:
        jelek = 1
    elif inputan > 10 and inputan <= 40:
        jelek = (inputan - 10)/(40-10)
    return [bagus,tengah,jelek]

#Function Fuzifikasi Harga
def FuzifikasiHarga (inputan: float) -> listFloat :
    mahal = float
    tengah = float
    murah = float
    #mahal
    if inputan > 8 :
        mahal = 1
    elif inputan > 6 :
        mahal = (inputan-6)/(10-6)
    else :
        mahal = 0
    #Menengah
    if inputan > 8 or inputan <= 4:
        tengah = 0
    elif inputan > 4 and inputan < 5:
        tengah = 1
    elif inputan >= 5 and inputan <= 8 :
        tengah = (8 - inputan)/(8-5)
    elif inputan > 4 and inputan <= 4 :
        tengah = (inputan - 4)/(4-4)
    #murah   
    if inputan > 4:
        murah = 0
    elif inputan > 0 and inputan <= 2:
        murah = 1
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
            if servis[i][j] >= 0.5:
                if j == 0 :
                    if harga[i][0] >= 0.5:
                        if servis[i][j] < harga[i][0]:
                            mungkin.append(servis[i][j])
                        else:
                            mungkin.append(harga[i][0])
                    if harga[i][1] >= 0.5:
                        if servis[i][j] < harga[i][1]:
                            mungkin.append(servis[i][j])
                        else:
                            mungkin.append(harga[i][1])
                    if harga[i][2] >= 0.5:
                        if servis[i][j] < harga[i][2]:
                            pasti.append(servis[i][j])
                        else:
                            pasti.append(harga[i][2])
                if j == 1:
                    if harga[i][0] >= 0.5:
                        if servis[i][j] <= harga[i][0]:
                            tidak.append(servis[i][j])
                        else:
                            tidak.append(harga[i][0])
                    if harga[i][1] >= 0.5:
                        if servis[i][j] <= harga[i][1]:
                            mungkin.append(servis[i][j])
                        else:
                            mungkin.append(harga[i][1])
                    if harga[i][2] >= 0.5:
                        if servis[i][j] <= harga[i][2]:
                            mungkin.append(servis[i][j])
                        else:
                            mungkin.append(harga[i][2])
                if j == 2:
                    if harga[i][0] >= 0.5:
                        if servis[i][j] < harga[i][0]:
                            tidak.append(servis[i][j])
                        else:
                            tidak.append(harga[i][0])
                    if harga[i][1] >= 0.5:
                        if servis[i][j] < harga[i][1]:
                            tidak.append(servis[i][j])
                        else:
                            tidak.append(harga[i][1])
                    if harga[i][2] >= 0.5:
                        if servis[i][j] < harga[i][2]:
                            tidak.append(servis[i][j])
                        else:
                            tidak.append(harga[i][2])
        pasti.sort()
        mungkin.sort()
        tidak.sort()
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

#Defuzzifikasi
def defuzzy(inputan: listFloat) -> float:
    pembagi = inputan[0]+inputan[1]+inputan[2]
    if pembagi == 0:
        return 0
    else:
        return ((inputan[0]*100+inputan[1]*50+inputan[2]*30)/pembagi)