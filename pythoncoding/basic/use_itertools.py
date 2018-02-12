import itertools

def pi(N):
    n = itertools.count(1, 2)
    ns = itertools.takewhile(lambda x: x <= 2*N-1, n)
    n0 = list(ns)
    s = 0
    for i in range(N):
        if i%2 == 0:
            s = s + 4*1/n0[i]
        else:
            s = s + 4*(-1)/n0[i]
    return s
    
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')