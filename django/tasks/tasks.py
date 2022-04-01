from celery import shared_task


@shared_task(ignore_result=True)
def print_primes(x):
    primes = _gen_prime(x)
    print(f"Calculated primes({x}) = {primes}")


def _gen_prime(x):
    multiples = []
    results = []
    for i in range(2, x + 1):
        if i not in multiples:
            results.append(i)
            for j in range(i * i, x + 1, i):
                multiples.append(j)
    return results
