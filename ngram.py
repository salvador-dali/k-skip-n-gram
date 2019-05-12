from itertools import combinations


def _get_exact_k_skip_n_grams(arr, n, k):
    """Generates all the skip-n-grams with exactly k skips.

    Args:
      arr (list of anything): array from which the skip-n-grams
          will be generated.
      n (int): the size of n-grams
      k (int): the number of skips

    Yields:
      n-gram with exactly k skips (represented as a tuple)
    """
    for i in range(len(arr) - n - k + 1):
        part = arr[i:i+n+k]

        if k == 0:
            yield part
        else:
            for j in combinations(part[1:-1], n - 2):
                yield tuple([part[0]] + list(j) + [part[-1]])


def k_skip_n_grams(arr, n, k):
    """Generates all the k-skip-n-grams.

    Args:
      arr (list of anything): array from which the skip-n-grams
          will be generated.
      n (int): the size of n-grams
      k (int): the maximum number of skips

    Yields:
      k-skip-n-gram (represented as a tuple)
    """
    if n == 0:
        return

    if n == 1:
        for e in arr:
            yield e
        return

    for i in range(0, min(len(arr) - n, k) + 1):
        yield from _get_exact_k_skip_n_grams(arr, n, i)
