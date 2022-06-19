#Task
#The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print .

def sqr(n):
    for i in range(n):
        print(i**2)


if __name__ == '__main__':
    n = int(input())
    sqr(n)