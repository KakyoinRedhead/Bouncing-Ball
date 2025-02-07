def fibo_fun(n):
    if n < 0:
        return "Index musí být nezáporné číslo."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Příklady použití
print(f"fibo_fun(0) = {fibo_fun(0)}")  # Výstup: 0
print(f"fibo_fun(1) = {fibo_fun(1)}")  # Výstup: 1
print(f"fibo_fun(10) = {fibo_fun(10)}")  # Výstup: 13

def sum_d_3_5(n):
    l = []
    total_sum = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)
            total_sum += i
    return l, total_sum     
        
    

print(f"sum_d_3{sum_d_3_5(10)}")
print(f"sum_d_3{sum_d_3_5(15)}")
print(f"sum_d_3{sum_d_3_5(-5)}")

def is_prem(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prem(7))
print(is_prem(1))
print(is_prem(10))
print(is_prem(2))
print(is_prem(3))
print(is_prem(20))
print(is_prem(11))

