#with the help of list
def gcd(m,n) :
    cf =[]

    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i==0) :
            cf.append(i)
    print(cf)
    return print(cf[-1])

def gcd_notlist(m,n) :
    for i in range(1,min(m,n)+1):
        if(m%i)==0 and (n%i)==0:
            crcf = i;
    return print(crcf)

gcd(30,25)
gcd_notlist(30,25)

