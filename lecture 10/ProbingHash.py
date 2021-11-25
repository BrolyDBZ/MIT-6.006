import random


def is_prime(n):
    testcase = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n in testcase:
        return True
    d = n - 1
    s = 0
    while not d & 1:
        d >>= 1
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


def div_hash(k, n):
    return k % n


random.seed(0)


class Hash:
    def __init__(self, n, hash_fn1):
        self.size = greater_Prime(n)
        self.table = [None for _ in range(self.size)]
        self.hash_fn1 = hash_fn1
        self.unv1 = random.randint(0, self.size - 1)
        self.unv2 = random.randint(0, self.size - 1)

    def hash_fn2(self, k):
        hash_value = (self.unv1 * k) + self.unv2
        return hash_value % self.size

    def insert(self, k):
        count = 0
        probe = (self.hash_fn1(k, self.size) + count * self.hash_fn2(k)) % self.size
        while self.table[probe] is not None and self.table[probe] != "Delete":
            count += 1
            probe = (self.hash_fn1(k, self.size) + count * self.hash_fn2(k)) % self.size
        self.table[probe] = k

    def delete(self, k):
        count = 0
        probe = (self.hash_fn1(k, self.size) + count * self.hash_fn2(k)) % self.size
        while self.table[probe] is not None and probe < self.size:
            if self.table[probe] == k:
                self.table[probe] = "Delete"
                return
            count += 1
            probe = (self.hash_fn1(k, self.size) + count * self.hash_fn2(k)) % self.size
        raise ValueError

    def search(self, k):
        count = 0
        probe = (self.hash_fn1(k, self.size) + count * self.hash_fn2(k)) % self.size
        while self.table[probe] is not None and probe < self.size:
            if self.table[probe] == k:
                return True
            count += 1
            probe = (self.hash_fn1(k, self.size) + count * self.hash_fn2(k)) % self.size
        return False
