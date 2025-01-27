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

for i in range(3):
    print("test")