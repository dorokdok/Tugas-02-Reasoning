import fungsi as f

#Inisialisasi variable
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

print(fuzifikasiSrvc,"\n\n", fuzifikasiPrc)

#Inference 
inferenceds = f.inference(fuzifikasiSrvc,fuzifikasiPrc)

#Defuzzifikasi
for i in range(len(inferenceds)):
    dmp = f.defuzzy(inferenceds[i])
    defuzzy.append(dmp)

#Mengubah kembali dari list menjadi excel dengan mengambil 10 data terbaik
dataIDdmp = [x for _, x in sorted(zip(defuzzy, dataID),reverse= True)]
dataServisdmp = []
dataHargadmp = []
dataDefuzzy = []

for i in range(10):
    dmpID = dataIDdmp[i]
    j = 0
    while dmpID != dataID[j]:
        j+= 1
    dataServisdmp.append(dataServis[j])
    dataHargadmp.append(dataHarga[j])
    dataDefuzzy.append(defuzzy[j])

df = f.pd.DataFrame({'id': dataIDdmp[0:10], 'servis': dataServisdmp[0:10], 'harga': dataHargadmp[0:10], 'fuzzy score': dataDefuzzy[0:10]})
df.to_excel('peringkat.xlsx', sheet_name='tes', index=False)




