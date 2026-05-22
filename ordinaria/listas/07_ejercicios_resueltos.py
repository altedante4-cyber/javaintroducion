"""Ejercicios típicos resueltos con lo más pythonico"""

from collections import Counter
from itertools import groupby, zip_longest

# --- 1. Fusionar dos listas ordenadas (merge sort paso) ---
def merge(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    return res + a[i:] + b[j:]

# Pythonico con heapq
import heapq
def merge_heapq(a, b):
    return list(heapq.merge(a, b))

# --- 2. Anagramas: agrupar palabras que son anagramas ---
def group_anagrams(words):
    groups = {}
    for w in words:
        key = tuple(sorted(w))
        groups.setdefault(key, []).append(w)
    return list(groups.values())

def group_anagrams_pythonic(words):
    return [list(g) for _, g in groupby(sorted(words, key=sorted), key=sorted)]

# --- 3. Top K frecuentes ---
def top_k_frequent(nums, k):
    return [num for num, _ in Counter(nums).most_common(k)]

# --- 4. Intersección de dos listas (con duplicados) ---
def intersect(a, b):
    counts = Counter(a)
    res = []
    for x in b:
        if counts[x] > 0:
            res.append(x)
            counts[x] -= 1
    return res

# --- 5. Rotar lista a la derecha k veces ---
def rotate(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

# --- 6. Suma de dos dígitos que dan target (Two Sum) ---
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i

# --- 7. Producto de todos excepto sí mismo ---
def product_except_self(nums):
    n = len(nums)
    res = [1] * n
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res

# --- 8. Subarray de suma máxima (Kadane) ---
def max_subarray(nums):
    max_ending = max_so_far = nums[0]
    for x in nums[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far

# --- 9. Mover ceros al final sin copia extra ---
def move_zeros(nums):
    pos = 0
    for i, n in enumerate(nums):
        if n != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums

# Pythonico (con copia):
def move_zeros_pythonic(nums):
    return [x for x in nums if x != 0] + [0] * nums.count(0)

# --- 10. Aplanar lista anidada con profundidad arbitraria ---
def flatten(seq):
    for item in seq:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item

# --- 11. Obtener todos los subconjuntos (power set) ---
def power_set(nums):
    res = [[]]
    for n in nums:
        res += [subset + [n] for subset in res]
    return res

# --- 12. Comprimir string: "aabbbcc" -> "a2b3c2" ---
def compress(s):
    return "".join(f"{k}{len(list(g))}" for k, g in groupby(s))

# --- 13. Palíndromo check con listas ---
def is_palindrome(s):
    s = [c.lower() for c in s if c.isalnum()]
    return s == s[::-1]

# --- 14. Buscar elemento mayoritario (> n/2) ---
def majority_element(nums):
    return Counter(nums).most_common(1)[0][0]

# Boyer-Moore (O(1) espacio):
def majority_boyer(nums):
    count = candidate = 0
    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate

# --- 15. Transponer matriz irregular con zip_longest ---
def transpose_ragged(mat):
    return [list(filter(None, col)) for col in zip_longest(*mat, fillvalue=None)]
