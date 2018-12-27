nama = 'Indonesia'

if nama.lower().startswith('ind'):
    print 'Nama diawal dengan "ind"'
if 'ne' in nama:
    print 'Nama berisi string "ne"'
if nama.find('done') != -1:
    print 'Nama berisi string "done"'

pembatas = ', '
daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']

print pembatas.join(daftar_belanja)