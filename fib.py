# coding=utf-8

def fib(nr):
    k=[0,1]
    for l in range (2,nr):
       il = k[l-2]+k[l-1]
       k.append(il)
    return k

print fib(10)
