import ngram
from scipy.special import comb


def k_skip_n_grams_count(L, n, k):
    """The number of k_skip_n_grams using the formula.

    Args:
      L (int): the size of the corpus
      n (int): value of n-gram
      k (int): value of k-skip

    Returns:
      the number of k-skip-n-grams
    """
    if n == 0:
        return 0

    k = min(L - n + 1, k)
    z = comb(n - 1 + k, n - 1, exact=True)
    return z * (L*n + n + k - n**2 - k * n) // n


def k_skip_n_grams_count_direct(L, n, k):
    """Same as k_skip_n_grams_count, but the calculation is done via the
    function to generate all the n-grams.
    """
    return sum(1 for _ in ngram.k_skip_n_grams(range(L), n, k))
