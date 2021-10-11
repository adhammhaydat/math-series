
def fibonacci(n):
    n1 = 0
    n2=1
    count=0
    new_arr=[]
    while count <= n:
        print(n1)
        new_arr.append(n1)
        nth = n1+n2
        n1 = n2
        n2= nth
        count += 1
    return new_arr[-1]
              
def lucas(n):
    n1 = 2
    n2=1
    count=0
    new_arr=[]
    while count <= n:
        print(n1)
        new_arr.append(n1)
        nth = n1+n2
        n1 = n2
        n2= nth
        count += 1
    return new_arr[-1]

def sum_series(n,n1=0,n2=1):
    if n1 and n2:
        if {n1,n2}=={0,1}:

            return fibonacci(n)
            
        if {n1,n2}=={2,1}:
            return lucas(n)
            

    if {n1,n2} !={0,1} or {n1,n2} !={2,1}:
        count=0
        new_arr=[]
        while count <= n:
            print(n1)
            new_arr.append(n1)
            nth = n1+n2
            n1 = n2
            n2= nth
            count += 1
        return new_arr[-1]    

