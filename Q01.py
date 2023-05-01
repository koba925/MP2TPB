# Q01.py

def reverse(s):
    return "".join(list(reversed(s)))

def palindrome(s):
    return s == reverse(s)

n = 11
while True:
    str10 = str(n)
    str8 = oct(n)[2:]
    str2 = bin(n)[2:]
    if palindrome(str10) and palindrome(str8) and palindrome(str2):
        print(str10, str8, str2)
        break
    n += 2
