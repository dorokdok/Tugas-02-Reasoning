import fungsi as f

dataServis = f.listFloat
dataHarga = f.listFloat

fuzifikasiSrvc = f.Fuzifikasi
fuzifikasiSrvc = []
fuzifikasiPrc = f.Fuzifikasi
fuzifikasiPrc = []

rules=f.Fuzifikasi

data = f.pd.read_excel(r'bengkel.xlsx')
print(data, "\n")

dataServis = data['servis'].tolist()
dataHarga = data['harga'].tolist()

for i in range(len(dataServis)):
    fuzifikasiSrvc.append(f.FuzifikasiServis(dataServis[i]))

print(fuzifikasiSrvc, "\n")

for i in range(len(dataHarga)):
    fuzifikasiPrc.append(f.FuzifikasiHarga(dataHarga[i]))

print(fuzifikasiPrc,"\n")

rules = f.inteference(fuzifikasiSrvc,fuzifikasiPrc)

print(rules, "\nAAAA")

