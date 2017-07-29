from pylru import *

def print_hello(key,val):
    print "ejected:",key, "val:",val

def test1():
    cac = lrucache(3,print_hello)
    cac[1]="ljt"
    cac[2]="zhu"
    cac[3]="wang"
    cac[4]="niu"

def test2():
    store = {}
    cac = WriteBackCacheManager(store,3)
    cac[1]="ljt"
    cac[2]="zhu"
    cac[3]="wang"
    cac[4]="niu"
    print "store:",str(store)
    cac.sync()
    print "store sync:",str(store)

def test3():
    store = {}
    cac = WriteThroughCacheManager(store,3)
    cac[1]="ljt"
    cac[2]="zhu"
    cac[3]="wang"
    cac[4]="niu"
    print "store:",str(store)

def test4():
    @lrudecorator(3)
    def cac(x):
        print "need calculate :",x
        return x**2
    cac(1)
    cac(2)
    cac(3)
    print "need not cac[1],due to in cache:",cac(1)
    cac(4)
    print "cache:",str([k for k in cac.cache.items()])
    cac(1)







if __name__ == "__main__":
    print "test1:"
    test1()
    print "test2"
    test2()
    print "test3"
    test3()
    print "test4"
    test4()
