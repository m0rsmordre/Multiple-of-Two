def bul(nb):
    nb = int(nb)
    p = len(bin(nb))-2
    
    return min((2**(p-1),2**p),key=lambda i: abs(nb-i))

print(bul(768)) #closest multiple of 2 = 512
print(bul(769)) #closest multiple of 2 = 1024
