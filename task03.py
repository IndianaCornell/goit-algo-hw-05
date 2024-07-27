import timeit

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1
    skip = []
    for k in range(65536):
        skip.append(m)
    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip[ord(text[k])]
    return -1


def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1


with open('text1.txt', 'r', encoding='windows-1251') as f:
    article1 = f.read()

with open('text2.txt', 'r', encoding='windows-1251') as f:
    article2 = f.read()


existing_substring = 'копійок'   
nonexistent_substring = 'вигаданийтекст'   

def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=1000)


bm_existing_article1 = measure_time(boyer_moore, article1, existing_substring)
bm_nonexistent_article1 = measure_time(boyer_moore, article1, nonexistent_substring)
kmp_existing_article1 = measure_time(kmp_search, article1, existing_substring)
kmp_nonexistent_article1 = measure_time(kmp_search, article1, nonexistent_substring)
rk_existing_article1 = measure_time(rabin_karp, article1, existing_substring)
rk_nonexistent_article1 = measure_time(rabin_karp, article1, nonexistent_substring)

bm_existing_article2 = measure_time(boyer_moore, article2, existing_substring)
bm_nonexistent_article2 = measure_time(boyer_moore, article2, nonexistent_substring)
kmp_existing_article2 = measure_time(kmp_search, article2, existing_substring)
kmp_nonexistent_article2 = measure_time(kmp_search, article2, nonexistent_substring)
rk_existing_article2 = measure_time(rabin_karp, article2, existing_substring)
rk_nonexistent_article2 = measure_time(rabin_karp, article2, nonexistent_substring)


print("Article 1:")
print(f"Boyer-Moore (existing): {bm_existing_article1}")
print(f"Boyer-Moore (nonexistent): {bm_nonexistent_article1}")
print(f"KMP (existing): {kmp_existing_article1}")
print(f"KMP (nonexistent): {kmp_nonexistent_article1}")
print(f"Rabin-Karp (existing): {rk_existing_article1}")
print(f"Rabin-Karp (nonexistent): {rk_nonexistent_article1}")

print("\nArticle 2:")
print(f"Boyer-Moore (existing): {bm_existing_article2}")
print(f"Boyer-Moore (nonexistent): {bm_nonexistent_article2}")
print(f"KMP (existing): {kmp_existing_article2}")
print(f"KMP (nonexistent): {kmp_nonexistent_article2}")
print(f"Rabin-Karp (existing): {rk_existing_article2}")
print(f"Rabin-Karp (nonexistent): {rk_nonexistent_article2}")
