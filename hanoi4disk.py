def hanoi(r1,r2,r3,r4):

    
    n1 =[r4,r3,r2,r1]
    n2= []
    n3 =[]
    # n = [n1,n2,n3]
    # temp = 1
    # while n3 !=[r4,r3,r2,r1]:
        
    for i in range(1,16):
        
        if i % 2 == 0:
            if r1 in n1:
                a = min(n2+n3)
                if a in n2:
                    n2.remove(a)
                    n3.append(a)
                else:
                    n3.remove(a)
                    n2.append(a)
            
            if r1 in n2:
                a = min(n1+n3)
                if a in n1:
                    n1.remove(a)
                    n3.append(a)
                else:
                    n3.remove(a)
                    n1.append(a)

            if r1 in n3:
                a = min(n1+n2)
                if a in n1:
                    n1.remove(a)
                    n2.append(a)
                else:
                    n2.remove(a)
                    n1.append(a)
            
        else:
            if r1 in n1:
                n1.remove(r1)
                n2.append(r1)

            elif r1 in n2:
                n2.remove(r1)
                n3.append(r1)

            elif r1 in n3:
                n3.remove(r1)
                n1.append(r1)

    return n3



print(hanoi(1,2,3,4))






    
