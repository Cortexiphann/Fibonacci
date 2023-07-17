#FurkanFilikci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    while len(fib_list) < n:
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)
    
    return fib_list

sayi = int(input("Fibonacci dizisinin ilk kaç elemanını yazdırmak istersiniz? "))
fibonacci_dizisi = fibonacci(sayi)
print(f"Fibonacci dizisinin ilk {sayi} elemanı: {fibonacci_dizisi}")

