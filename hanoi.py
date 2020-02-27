def num_disk(n):
    count = 0
    A = []
    B = []
    C = []
    
    while count < n:
        A.insert(count, f'r_{n-count-1}')
        count += 1
        # return A


    
    while len(C)<n:
        
        if n % 2 == 0:
            a = min(A+B)
            if a in A:
                A.remove(a)
                B.append(a)
            else:
                B.remove(a)
                A.append(a)

            b = min(A+C)
            if b in A:
                A.remove(b)
                C.append(b)
            else:
                C.remove(b)
                A.append(b)

        else:

            b = min(A+C)
            if b in A:
                A.remove(b)
                C.append(b)
            else:
                C.remove(b)
                A.append(b)


            if A==[] and B ==[]:

                break
            a = min(A+B)
            if a in A:
                A.remove(a)
                B.append(a)
            else:
                B.remove(a)
                A.append(a)
            
        c = min(B+C)
        if c in B:
            B.remove(c)
            C.append(c)
        else:

            C.remove(c)
            B.append(c)

    return C



print(num_disk(5))

            


        
        



        

    
