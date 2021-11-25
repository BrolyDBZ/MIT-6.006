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


class Hash:
    def __init__(self, n, hash_fn):
        self.size = greater_Prime(n)
        self.table = [[] for _ in range(self.size)]
        self.has_fn = hash_fn

    def insert(self, k):
        probe = self.has_fn(k, self.size)
        self.table[probe].append(k)

    def delete(self, k):
        probe = self.has_fn(k, self.size)
        if k in self.table[probe]:
            self.table[probe].remove(k)
            return
        raise ValueError

    def search(self, k):
        probe = self.has_fn(k, self.size)
        if k in self.table[probe]:
            return True
        return False


def div_hash(k, n):
    return k % n
