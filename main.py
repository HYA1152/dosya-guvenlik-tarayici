dosya_yolu ="main.py"
with open(dosya_yolu, "rb") as f:      
    ilk_baytlar = f.read(8)            
    
print(ilk_baytlar)
print(ilk_baytlar.hex())
