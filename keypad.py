keys = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

def cc(digits):
    if len(digits) == 0:
        return 1
    return len(keys[digits[0]]) * cc(digits[1:])

input("cc (count combos) multiplies letter choices by each digit  -  3 letters oper step. press enter")
print("cc of    2 =",cc('2'))

n = input("enter  a number, prefferably 9 or below (if u do 9 or above it WONT work)")
print("count combos of it =", cc(n))
