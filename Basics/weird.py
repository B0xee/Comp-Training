#Task
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird

def main(n):
    if n%2==0:
        if n in range(6,21):        # Whats the significance between range(n,20) and (n,21)
            print("Weird")
            return
        print ("Not Weird")
    else:
        print("Weird")

if __name__ == '__main__':
    n = int(input().strip())
    main(n)