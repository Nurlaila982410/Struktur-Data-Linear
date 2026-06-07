#SET = yang tidak beraturan
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} #hasilnya {'orange', 'banana', 'pear', 'apple'} karena set hanya menyimpan elemen yang unik dan tidak berurutan
print("Isi basket: ", basket) #

#mengecek keanggotaan
print('orange' in basket)
print('crabgrass' in basket)

#set dari dua kata (huruf unik)
a = set('abracadabra')
b = set('alacazam')

print("set a:", a)
print("set b:", b)

#operasi set
print(a-b) #huruf di a tapi tidak ada di b
print(a|b) #gabungan a dan b
print(a&b) #irisan (yang sama yang di a sama b)
print(a^b) #selisih simetris (yang beda gitu antara a sama b)
