from pertemuan2 import pop


def balik_string(teks):
    stack = []

    for char in teks:
        stack.append(char)
    
    hasil = ''

    while stack:
        hasil += stack.pop()
    return hasil

print (balik_string('halo'))
print (balik_string('python'))
print (balik_string('racecar'))