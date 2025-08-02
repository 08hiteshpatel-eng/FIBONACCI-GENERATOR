def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example: Generate first 10 Fibonacci numbers
fibonacci_series(10)