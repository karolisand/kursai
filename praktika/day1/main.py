def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Specify how many Fibonacci numbers you want to print
count = 12  # You can change this number
fibonacci(count)