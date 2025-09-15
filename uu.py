def swap(si, sj):
    return sj, si

def pr1(s, t):
    j = 0
    for i in range(256):
        j = (j + s[i] + t[i]) % 256
        s[i], s[j] = swap(s[i], s[j])
    print(s)

def pr2(s, le):
    k = []
    x = 0
    j = 0
    for i in range(le):
        x = (x + 1) % 256
        j = (j + s[x]) % 256
        s[x], s[j] = swap(s[x], s[j])
        t = (s[x] + s[j]) % 256
        k.append(s[t])
    return k

def keycr(k, le):
    s = list(range(256))
    t = [ord(k[i % len(k)]) for i in range(256)]
    s = pr1(s, t)
    key = pr2(s, le)
    return key