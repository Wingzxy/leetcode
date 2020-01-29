x=input()
x=x.split(' ')

def root(num, root):
    result = num**(1/root)
    result = round(result, 12)
    return result

result = root(float(x[0]),float(x[1]))
print(result)