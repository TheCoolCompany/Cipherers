alphabet = ["a", "b", "c", "d", "e","f","g","h","i","j","k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z", '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '{', ']', '}', '{', ':', ';', '<', '>', ',', '.', '?', '/', '`', '~', ' ']
text = "this will be in cipher"#.replace(" ", "")
ctext = []
st = list(text)
o = 1
i = 0
cipher = 10
while i < len(text):
    if st[i] not in alphabet:
        ctext.append(st[i])
        i += 1
        continue
    o = alphabet.index(st[i])
    if o + cipher <= len(alphabet):     
        ctext.append(alphabet[o + cipher])
        i += 1
    else:
        ctext.append(alphabet[o + cipher - len(alphabet)])
        i += 1
        


ctext = ''.join(ctext)
print(ctext)
    

