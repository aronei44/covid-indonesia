import requests
r = requests.get('https://api.kawalcorona.com/indonesia/provinsi', auth=('user', 'pass'))
raw = r.json()
print("Data Kasus Covid 19 Indonesia")
print("\nDibuat Oleh : Arwani")
print("\nAPI : kawalcorona\n")
for r in raw:
	data = r['attributes']
	print("Kode Provinsi  =",data['Kode_Provi'])
	print(" Provinsi  	= ", data["Provinsi"])
	print("  Kasus Positif   = ", data["Kasus_Posi"])
	print("  Kasus Sembuh    = ", data["Kasus_Semb"])
	print("  Kasus Meninggal = ", data["Kasus_Meni"])
	print("===========================\n")
	