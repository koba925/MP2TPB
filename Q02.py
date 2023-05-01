# Q02.py

def reverse(s):
    return "".join(list(reversed(s)))

# ops = ["+", "-", "*", "//", ""]
ops = ["*", ""]

for n in range(1000, 10000):
    nstr = str(n)
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                expr = nstr[0] + op1 + nstr[1] + op2 + nstr[2] + op3 + nstr[3]
                if expr == nstr:
                    continue
                try:
                    val = eval(expr)
                except:
                    continue
                if str(n) == reverse(str(val)):
                    print(f"{n} = {expr}")
