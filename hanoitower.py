def hanoi(n):
    if n == 0:
        return 0
    return 2 * hanoi(n-1) + 1

input("hanoi counts the number of minimum moves to shift n disks  from peg A to peg C . press enter")
print("hanoi 1", hanoi(1))

n = int(input("enter a number of disks"))
print("number of moves to shifts disks to last peg =", hanoi(n))

