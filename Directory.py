#directionary
tel = {'jack':4098, 'sape':4139}
#menambah data
tel['guido'] = 4127
print(tel)
#mengakses nilai
print(tel['jack'])
#mengakses key yang tidak ada (AMAN)
print(tel.get('irv')) #hasil : None
#menghapus data
del tel['sape']

#menambah lagi
tel['irv'] = 4127
print(tel)

#mengubah ke list
print(list(tel))
#mengurutkan key
print(sorted(tel))
#mengecek keberadaan key
print('guido' in tel)
print('jack' not in tel)