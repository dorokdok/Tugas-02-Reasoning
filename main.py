import fungsi as f

dataServis = f.listFloat
dataHarga = f.listFloat

fuzifikasiSrvc = f.Fuzifikasi
fuzifikasiSrvc = []

data = f.pd.read_excel(r'bengkel.xlsx')
print(data)

dataServis = data['servis'].tolist()
dataHarga = data['harga'].tolist()

for i in range(len(dataServis)):
    fuzifikasiSrvc.append(f.FuzifikasiServis(dataServis[i]))

print(fuzifikasiSrvc)

