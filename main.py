import fungsi as f

dataServis = f.listFloat
dataHarga = f.listFloat

fuzifikasiSrvc = f.Fuzifikasi
inferenceds=f.Fuzifikasi
fuzifikasiPrc = f.Fuzifikasi
defuzzy = f.listFloat
defuzzy = []
fuzifikasiPrc = []
fuzifikasiSrvc = []

#Mengubah data dari excel menjadi list
data = f.pd.read_excel(r'bengkel.xlsx')
dataID = data['id'].tolist()
dataServis = data['servis'].tolist()
dataHarga = data['harga'].tolist()

#Fuzzifikasi data servis
for i in range(len(dataServis)):
    fuzifikasiSrvc.append(f.FuzifikasiServis(dataServis[i]))

#Fuzzifikasi data harga
for i in range(len(dataHarga)):
    fuzifikasiPrc.append(f.FuzifikasiHarga(dataHarga[i]))

#Inference 
inferenceds = f.inference(fuzifikasiSrvc,fuzifikasiPrc)

#Defuzzifikasi
for i in range(len(inferenceds)):
    dmp = f.defuzzy(inferenceds[i])
    defuzzy.append(dmp)

#Mengubah kembali dari list menjadi excel dengan mengambil 10 data terbaik
dataID = [x for _, x in sorted(zip(defuzzy, dataID),reverse= True)]
dataServis = [x for _, x in sorted(zip(defuzzy, dataServis),reverse= True)]
dataHarga = [x for _, x in sorted(zip(defuzzy, dataHarga),reverse= True)]
defuzzy.sort(reverse= True)
df = f.pd.DataFrame({'id': dataID[0:10], 'servis': dataServis[0:10], 'harga': dataHarga[0:10], 'fuzzy score': defuzzy[0:10]})
df.to_excel('tes.xlsx', sheet_name='tes', index=False)




