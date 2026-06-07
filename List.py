#LIST = kumpulan data yang bisa diubah
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'] #list bisa berisi data yang sama

print(fruits.count('apple')) #count = menghitung jumlah kemunculan suatu data dalam list
print(fruits.count('tangerine')) #hasilnya 0 karena tangerine tidak ada dalam list

print(fruits.index('banana')) #hasilnya 3 karena index pertama dari banana adalah 3
print(fruits.index('banana', 4)) #hasilnya 6 karena index pertama dari banana setelah index 4 adalah 6

fruits.reverse() #reverse = membalik urutan list
print(fruits) #hasilnya ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append('grape') #append = menambahkan elemen di akhir list
print(fruits) #hasilnya ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort() #sort = mengurutkan list secara alfabetis
print(fruits) #hasilnya ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

print(fruits.pop()) #pop = menghapus elemen terakhir dari list dan mengembalikan nilai yang dihapus
print(fruits) #hasilnya ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']