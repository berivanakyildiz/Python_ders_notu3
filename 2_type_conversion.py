
x = input("1.Sayi:")
y = input("2.Sayi:")

toplam = int(x) + int(y) 
print(toplam)
#---------------------------------

x = 5
x = float(x) # int değişkenini floata çevirdik
print(x)
print(type(x)) # veri tipini yazdırdık
#--------------------------------



pi = 3.14
yariCapi = input("Yari Çap:")
yariCapi = float(yariCapi)
alan = pi*yariCapi*yariCapi
cevre = 2*pi*yariCapi

print("Alan: " + str(alan) + " Çevre:" + str(cevre))
