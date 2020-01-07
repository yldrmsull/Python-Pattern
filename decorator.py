@hesapla
def topla(x,y):
    return x+y
def hesapla(func):
    def f(args,kargs):
        once=time()
        s=func(args,kargs)
        sonra=time()
        print("çalışma süresi "sonra-once)
        return s
    return f        