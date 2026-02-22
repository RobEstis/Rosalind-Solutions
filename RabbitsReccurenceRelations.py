""" Problem
A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. Two examples are the finite sequence (π,−2–√,0,π)
 and the infinite sequence of odd numbers (1,3,5,7,9,…)
. We use the notation an
 to represent the n-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. As a result, if Fn
 represents the number of rabbit pairs alive after the n
-th month, then we obtain the Fibonacci sequence having terms Fn
 that are defined by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

When finding the n
-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n
 months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
 rabbit pairs (instead of only 1 pair)."""

from __future__ import annotations


def rabbits(n: int, k: int) -> int:
    """Return the number of rabbit pairs after n months with litter size k."""
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if k <= 0:
        raise ValueError("k must be a positive integer.")

    if n in (1, 2):
        return 1

    f_prev2 = 1  # F1
    f_prev1 = 1  # F2
    for _ in range(3, n + 1):
        f_curr = f_prev1 + k * f_prev2
        f_prev2, f_prev1 = f_prev1, f_curr

    return f_prev1


def parse_input(text: str) -> tuple[int, int]:
    parts = text.strip().split()
    if len(parts) != 2:
        raise ValueError("Expected exactly two integers: n k")
    n, k = map(int, parts)
    return n, k


def main() -> None:
    import sys

    data = sys.stdin.read()
    if not data.strip():
        raise SystemExit("No input provided. Expected: n k")

    n, k = parse_input(data)
    print(rabbits(n, k))


if __name__ == "__main__":
    main()
