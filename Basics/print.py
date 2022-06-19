#Task
#Read n and print vals in the same line in that range

def lines(n):  
    n=range(1,n+1)
    print(*n,sep="")

if __name__ == '__main__':
    n = int(input())
    lines(n)