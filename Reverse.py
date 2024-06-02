x = 123
x = str(x)
if(x[0] == "-"):
    x = x[1:]
    x = x[::-1]
    x = "-" + x
else:
    x = x[::-1]
        
x = int(x)
if(x<(-2**31) or x>2**31):
    print(0)
else:
    print(x)