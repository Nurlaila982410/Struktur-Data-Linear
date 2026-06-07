#TUPLE = kumpulan data yang tidak bisa diubah
t = 12345, 54321, 'hello!' #tuple bisa dibuat tanpa tanda kurung, tapi biasanya kita menggunakan tanda kurung untuk membuatnya lebih jelas
t[0] #hasilnya 12345 karena index pertama dari tuple adalah 0
print (t) #hasilnya (12345, 54321, 'hello!') karena tuple ditampilkan dengan tanda kurung

#tuples my be nested
u = t, (1, 2, 3, 4, 5) #hasilnya ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5)) karena tuple t dan tuple (1, 2, 3, 4, 5) digabungkan menjadi satu tuple yang lebih besar
print(u) #hasilnya ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5)) karena tuple t dan tuple (1, 2, 3, 4, 5) digabungkan menjadi satu tuple yang lebih besar

#tuples are immutable:
#t[0] = 88888
#but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1]) #hasilnya ([1, 2, 3], [3, 2, 1]) karena tuple v berisi dua list yang bisa diubah
print(v) #hasilnya ([1, 2, 3], [3, 2, 1]) karena tuple v berisi dua list yang bisa diubah