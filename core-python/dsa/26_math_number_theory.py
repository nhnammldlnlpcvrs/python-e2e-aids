# ============================================
# 26. MATH & NUMBER THEORY - TOÁN & SỐ HỌC
# ============================================
# Các thuật toán toán học cơ bản dùng trong competitive programming.
# GCD/LCM, Số nguyên tố, Modular arithmetic, Tổ hợp.


# ==============================
# GCD & LCM
# ==============================

def gcd(a, b):
    """Ước chung lớn nhất (Euclidean algorithm) - O(log(min(a,b)))"""
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    """GCD đệ quy"""
    return a if b == 0 else gcd_recursive(b, a % b)


def lcm(a, b):
    """Bội chung nhỏ nhất"""
    return a * b // gcd(a, b) if a and b else 0


def extended_gcd(a, b):
    """Extended Euclidean: ax + by = gcd(a, b)
    Trả về (gcd, x, y)"""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


# ==============================
# MODULAR ARITHMETIC
# ==============================

def mod_add(a, b, mod):
    return (a + b) % mod


def mod_sub(a, b, mod):
    return (a - b + mod) % mod


def mod_mul(a, b, mod):
    return (a * b) % mod


def mod_pow(base, exp, mod):
    """Lũy thừa modulo nhanh (binary exponentiation) - O(log exp)"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result


def mod_inverse(a, mod):
    """Nghịch đảo modulo dùng Fermat's Little Theorem
    Yêu cầu: mod là số nguyên tố"""
    return mod_pow(a, mod - 2, mod)


def mod_inverse_extended(a, mod):
    """Nghịch đảo modulo dùng Extended Euclidean
    Hoạt động với mọi mod miễn là gcd(a, mod) = 1"""
    g, x, y = extended_gcd(a, mod)
    if g != 1:
        return None  # Không tồn tại nghịch đảo
    return (x % mod + mod) % mod


def mod_divide(a, b, mod):
    """Chia modulo: a / b % mod = a * b^(-1) % mod"""
    inv = mod_inverse(b, mod)
    return (a * inv) % mod


# ==============================
# PRIME NUMBERS
# ==============================

def is_prime_trial(n):
    """Kiểm tra nguyên tố - O(√n)"""
    if n < 2:
        return False
    if n < 4:  # 2, 3
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # 6k ± 1
    return True


def sieve_of_eratosthenes(n):
    """Sàng Eratosthenes: tìm mọi số nguyên tố <= n - O(n log log n)"""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


def prime_factorization(n):
    """Phân tích thừa số nguyên tố - O(√n)"""
    factors = []
    # Xử lý số 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Xử lý số lẻ
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors


def count_divisors(n):
    """Đếm số ước của n dùng prime factorization"""
    factors = prime_factorization(n)
    from collections import Counter
    freq = Counter(factors)
    result = 1
    for exp in freq.values():
        result *= (exp + 1)
    return result


def euler_totient(n):
    """Phi hàm Euler: số lượng số nguyên tố cùng nhau với n (1 <= k <= n)"""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


# ==============================
# COMBINATORICS (TỔ HỢP)
# ==============================

def factorial(n, mod=None):
    """Giai thừa, có thể tính modulo"""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod if mod else result * i
    return result


def nCr_precompute(n_max, mod):
    """Tính tất cả C(n, k) cho n <= n_max (Pascal's Triangle)"""
    C = [[0] * (n_max + 1) for _ in range(n_max + 1)]
    for i in range(n_max + 1):
        C[i][0] = C[i][i] = 1
        for j in range(1, i):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod
    return C


def nCr_factorial(n, r, mod):
    """Tính C(n, r) mod prime dùng factorial + modular inverse"""
    if r < 0 or r > n:
        return 0
    num = factorial(n, mod)
    den = (factorial(r, mod) * factorial(n - r, mod)) % mod
    return (num * mod_inverse(den, mod)) % mod


# ==============================
# Demo
# ==============================

print("=== GCD & LCM ===")
print(f"gcd(48, 18): {gcd(48, 18)}")
print(f"gcd_recursive(48, 18): {gcd_recursive(48, 18)}")
print(f"lcm(12, 18): {lcm(12, 18)}")
g, x, y = extended_gcd(48, 18)
print(f"extended_gcd(48, 18): gcd={g}, x={x}, y={y} -> {48}*{x} + {18}*{y} = {g}")

print("\n=== Modular Arithmetic ===")
mod = 10**9 + 7
print(f"mod = {mod}")
print(f"mod_pow(2, 10, mod): {mod_pow(2, 10, mod)}")
print(f"mod_pow(3, 100, 1000): {mod_pow(3, 100, 1000)}")
inv = mod_inverse(5, mod)
print(f"mod_inverse(5, mod): {inv}")
print(f"Verify: 5 * {inv} % mod = {(5 * inv) % mod}")

print("\n=== Prime Numbers ===")
primes_50 = sieve_of_eratosthenes(50)
print(f"Primes <= 50: {primes_50}")
print(f"Count primes <= 100: {len(sieve_of_eratosthenes(100))}")
print(f"is_prime(97): {is_prime_trial(97)}")
print(f"is_prime(100): {is_prime_trial(100)}")

print("\n=== Prime Factorization ===")
for n in [84, 100, 123456]:
    print(f"  {n} = {' × '.join(str(f) for f in prime_factorization(n))}")

print(f"\nDivisors of 36: {count_divisors(36)}")

print("\n=== Euler's Totient ===")
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]:
    print(f"  phi({n}) = {euler_totient(n)}")

print("\n=== Combinatorics ===")
print(f"5! = {factorial(5)}")
print(f"C(5, 2) from Pascal: {nCr_precompute(5, mod)[5][2]}")
print(f"C(5, 2) factorial: {nCr_factorial(5, 2, mod)}")

# ==============================
# Công thức tham khảo
# ==============================

print("\n=== Số học cơ bản ===")
print("""
GCD properties:
  gcd(a, b) = gcd(b, a % b)
  gcd(a, 0) = a
  lcm(a, b) * gcd(a, b) = a * b

Modular arithmetic:
  (a + b) % m = ((a % m) + (b % m)) % m
  (a * b) % m = ((a % m) * (b % m)) % m
  a^b % m    -> binary exponentiation O(log b)
  a / b % m  -> a * b^(m-2) % m  (Fermat, m nguyên tố)

Prime distribution:
  pi(n) ~ n / ln(n) (Prime Number Theorem)
  Số nguyên tố dạng 6k±1 (trừ 2, 3)

Combinatorics:
  C(n, k) = n! / (k! * (n-k)!)
  C(n, k) = C(n-1, k-1) + C(n-1, k)  (Pascal)
  sum(C(n, i)) = 2^n
""")
