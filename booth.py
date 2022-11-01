def max(x,y):
    if(x>=y):
        return x
    else:
        return y

def toBinary(n):
    return bin(n).replace("0b","0")

def toDecimal(n): # n->string
    return int(n,2)

def twosComplement(num):
    n = toBinary(num)
    b = '1'
    a = n.replace('1','%temp%').replace('0','1').replace('%temp%','0')
    return bin(int(a,2) + int(b,2)).replace('0b','')

def add(a,b):
    return bin(int(a,2) + int(b,2)).replace("0b","")
        
def multiply(Multip,Multiplier):
    M = toBinary(Multip)
    Q = toBinary(Multiplier)
    len1 = len(M) 
    len2 = len(Q) 
    count = max(len1,len2)
    a = '0'
    q = '0'
    for i in range(0,count):
        if Q[-1] == '1' and q == '0':
            a = add(a,twosComplement(Multip))
            print(a)
        elif Q[-1] == '0' and q == '1':
            a = add(a,M)
            print(a)
    

multiply(2,3)
#print(twosComplement(toDecimal('10')))
# print(add('0','11'))
# print(toBinary(2))


        
    
