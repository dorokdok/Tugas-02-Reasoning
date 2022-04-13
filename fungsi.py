import numpy as np
import pandas as pd
from typing import List

listFloat = List[float]
Fuzifikasi = List[listFloat]


def FuzifikasiServis (inputan: int) -> listFloat :
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


