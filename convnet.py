from ad import dual, max

def convnet(x: list):

    w1 = dual(1.2, 1)
    w2 = dual(-0.2, 0)
    v = [dual(i, 0) for i in [-0.3, 0.6, 1.3, -1.5]]
    X = [dual(x[i], 0) for i in range(0, 5)]

    z = [max(dual(0, 0), dual.__add__(dual.__mul__(w1, X[i]), dual.__mul__(w2, X[i + 1]))) for i in range(0, 4)]

    S = dual(0, 0)
    for i in range(0, 4):
        S = dual.__add__(S, dual.__mul__(v[i], z[i]))

    y = max(dual(0, 0), S)

    return y, z


x=[0.3,-1.5,0.7,2.1,0.1]
y,z=convnet(x)
print(y,z)

