IMZALAR = {
    "89504e470d0a1a0a": "PNG",
    "ffd8ff": "JPEG",
    "25504446": "PDF",
    "4d5a": "EXE",
}
dosya_yolu ="test_dosyalari/stant.jpeg"
with open(dosya_yolu, "rb") as f:      
    ilk_baytlar = f.read(8)            

print(ilk_baytlar)
print(ilk_baytlar.hex())

bulunan_tur = "Bilinmiyor"

for imza, tur in IMZALAR.items():
    if ilk_baytlar.hex().startswith(imza):
        bulunan_tur = tur
        break

    print("Gerçek Tür:", bulunan_tur)

