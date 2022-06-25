def main(x,y,z,n):
    x=list(range(x+1))
    y=list(range(y+1))
    z=list(range(z+1))
    
    comp = [[i,j,k] for i in x
                    for j in y
                    for k in z]
    
    Comp=[]
    for i in comp:
        if sum(i)!=n:
            Comp.append(i)
    print(Comp)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    main(x,y,z,n)
