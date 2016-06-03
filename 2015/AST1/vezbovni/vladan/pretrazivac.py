x = [0.3, 0.9, 3, 0.11, 0.23, 50, 15]

def min(x):
    m = x[0]
    for i in range(1, len(x)):
        if m > x[i]:
            m = x[i]

    return m

def max(x):
    m = x[0]
    for i in range(1, len(x)):
        if m < x[i]:
            m = x[i]

    return m

print(x)
print('najmnji u x je', min(x))
print('najveci u x je', max(x))

