import time


def slow_fibonacci(n):
    if n < 2:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


def count_primes(limit):
    count = 0
    for n in range(2, limit):
        if all(n % d != 0 for d in range(2, int(n**0.5) + 1)):
            count += 1
    return count


def build_strings(size):
    text = ""
    for i in range(size):
        text += str(i)
    return len(text)


def sleepy_io():
    time.sleep(1)


def main():
    start = time.perf_counter()

    print("fibonacci(32):", slow_fibonacci(32))
    print("primes below 1_000_000:", count_primes(1_000_000))
    print("string length:", build_strings(2_000_000))
    sleepy_io()

    print(f"done in {time.perf_counter() - start:.2f}s")


if __name__ == "__main__":
    main()
