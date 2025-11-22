# 1-vazifa
def kvadrat (x):
    natija=x**2
    return f"natijangiz {natija}"
print(kvadrat(34))

# 2-vazifa
def yigindi(*args):
    natija=0
    for x in args:
        natija+=x
    return f"yigindi {natija}"
print(yigindi(1,2,3,4,5))

# yoki
def yigindi(*args):
    return f"yigindi {sum(args)}"
print(yigindi(1,2,3,4,5))

# 3-vazifa
def info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")
info(name="Ali", age=20)
