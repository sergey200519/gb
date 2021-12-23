import hashlib

def count_substring(s):
    hash_set = set()
    n = len(s)
    i = 0
    while i < n:
        j = i + 1
        while j <= n:
            if s[i:j] != s:
                hash_set.add(hashlib.sha256(s[i:j].encode()).hexdigest())
            j += 1
        i += 1
    return len(hash_set)

print(count_substring("papa"))