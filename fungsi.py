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
    #Jika servis > 85 atau < 30 maka tengah = 0
    if inputan > 85 or inputan < 30:
        tengah = 0
    #Jika 50 <= servis <= 60 maka tengah = 1
    elif inputan >= 50 and inputan <= 60:
        tengah = 1
    #Jika 60 < servis <= 85 maka tengah = rumus
    elif inputan > 60 and inputan <= 85 :
        tengah = (85 - inputan)/(85-60)
    #Jika 30 <= servis < 50 maka tengah = rumus
    elif inputan >= 30 and inputan < 50 :
        tengah = (inputan - 30)/(50-30)
    # jelek    
    #Jika servis >= 50 maka jelek = 0
    if inputan >= 50:
        jelek = 0
    #Jika servis < 30 make jelek = 1
    elif inputan > 0 and inputan < 30:
        jelek = 1
    #Jika 30 <= servis < 50 maka jelek = rumus
    elif inputan >= 30 and inputan < 50:
        jelek = (50 - inputan)/(50-30)
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
    #Jika harga > 8 atau harga <= 3 maka tengah = 0
    if inputan > 8 or inputan <= 3:
        tengah = 0
    #Jika 5 <= harga < 6 maka tengah = 1
    elif inputan >= 5 and inputan < 6:
        tengah = 1
    #Jika 6 <= harga <= 8 maka tengah = rumus
    elif inputan >= 6 and inputan <= 8 :
        tengah = (8 - inputan)/(8-6)
    #Jika 3 < harga <= 5 maka tengah = rumus
    elif inputan > 3 and inputan < 5 :
        tengah = (inputan - 3)/(5-3)
    #murah
    #Jika Harga > 5 maka murah = 0   
    if inputan >= 5:
        murah = 0
    #Jika harga <= 3 maka murah = 1
    elif inputan > 0 and inputan <= 3:
        murah = 1
    #jika 3 < harga <= 5 maka murah = rumus
    elif inputan > 3 and inputan <= 5:
        murah = (5 - inputan)/(5-3)
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
#pasti * 100 + mungkin * 50 + tidak *30 /pasti+mungkin+tidak
def defuzzy(inputan: listFloat) -> float:
    pembagi = inputan[0]+inputan[1]+inputan[2]
    if pembagi == 0:
        return 0
    else:
        return ((inputan[0]*100+inputan[1]*50+inputan[2]*30)/pembagi)