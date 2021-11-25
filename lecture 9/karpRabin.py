def is_prime(n):
    testcase = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n in testcase:
        return True
    d = n - 1
    s = 0
    while not d & 1:
        d = d >> 1
        s += 1
    for a in testcase:
        result = False
        for r in range(s):
            if (a ** (d << r) % n) == n - 1 or (a ** d) % n == 1:
                result = True
                break
        if not result:
            return False
    return True


def greater_Prime(n):
    result = n + (1 if n % 2 == 0 else 2)
    while not is_prime(result):
        result += 2
    return result

class RollingHash:
    def __init__(self,len):
        self.base=256
        self.size=greater_Prime(self.base)
        self.num=0
        self.hash=1
        self.magic=self.base**(len-1)
    def append(self,k):
        self.num=self.num*self.base+ord(k)
        self.hash=self.num%self.base
    def skip(self,k):
        self.num=self.num-ord(k)*self.magic
        self.hash=self.num%self.base

def KarpRabin(s,t):
    window=len(s)
    rs=RollingHash(window)
    rt=RollingHash(window)
    for i in range(window):
        rs.append(s[i])
        rt.append(t[i])
    iter=len(t)
    if rt.hash == rs.hash:
        if rt.num == rs.num:
            return True
    for i in range(window,iter):
        rt.skip(t[i-window])
        rt.append(t[i])
        if rt.hash == rs.hash:
            if rt.num == rs.num:
                return True
    return False



