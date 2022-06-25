x = 1
y = 1

def main(x,y):
    x=list(range(x+1))
    y=list(range(y+1))
    arr = [x,y]
    banana = [[row[i] for row in arr] for i in range(2)]
    print(banana)


arr = [list(range(x+1)),list(range(y+1))]
banana = [[i,j] for i in arr[0]
                for j in arr[1]]
print(banana)