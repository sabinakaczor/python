def nwd(l1,l2):
    a = min(l1,l2)
    b= max(l1,l2) % a
    while a!=0 and b!=0:
        temp = min(a,b)
        temp2 = max(a,b) % temp
        a = temp
        b = temp2
    if a==0:
        return b
    else:
        return a

print nwd(6,9) # 3

def nww(a,b):
    return a*b/nwd(a,b)

print nww(5,20) #20