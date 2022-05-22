alphabet = ["a", "b", "c", "d", "e","f","g","h","i","j","k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z", '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '{', ']', '}', '{', ':', ';', '<', '>', ',', '.', '?', '/', '`', '~', ' ']
cipherd = '$rs#j&svvjlojsxjmszro@'#.replace(" ", "")
ctext = []
st = list(cipherd)

i = 0
cipher = 10
s1 = 0
while i < len(cipherd):
    if st[i] not in alphabet:
        ctext.append(st[st[i]])
        i += 1
        continue
    o = alphabet.index(st[i])    
    if o - cipher > 0:    
        ctext.append(alphabet[o - cipher])
    else:
        s1 = o - cipher + len(alphabet)
        ctext.append(alphabet[s1])
    i += 1


ctext = ''.join(ctext)
print(ctext)