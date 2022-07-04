#Task
#Given an integer n and array A, store A as a list and give the runner-up score

def main(n,arr):
    if len(arr)!=n:
        raise("Error")
    else:
        arr.sort()
        idx=arr.index(max(arr))
        print(arr[idx-1])

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    main(n,arr)