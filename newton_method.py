def dx(x):
    return 4 * x**3 - 1
def fx(x):
    return x**4 - x - 10

x = 1.5
count = 0

while(abs(fx(x)) > 0.0001):
    print(count ," : ", x)
    x = x - fx(x)/ dx(x)
    count += 1
