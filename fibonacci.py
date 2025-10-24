def caching_fibonacci():
    # Cache will store already computed Fibonacci numbers
    cache = {}

    def fibonacci(n):
        # Base cases
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Check if result is already cached
        if n in cache:
            return cache[n]

        # Compute and store in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Return inner function (closure)
    return fibonacci


# Example usage:
fib = caching_fibonacci()
print(fib(10))  # → 55
print(fib(15))  # → 610
