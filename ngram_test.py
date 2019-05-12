import ngram
import unittest


class TestGrams(unittest.TestCase):
    def test_arr_zero(self):
        # Empty array -> no skip-grams
        for (n, k) in [(2, 3), (1, 7), (6, 3), (5, 2)]:
            grams = list(ngram.k_skip_n_grams([], n, k))
            self.assertEqual(grams, [])

    def test_n_one(self):
        # The only 1-grams possible are actual values of the array
        tests = [
            ((1, 2, 3), 1),
            ((2, 3, 4, 5), 2),
        ]
        for (arr, k) in tests:
            grams = list(ngram.k_skip_n_grams(arr, 1, k))
            self.assertEqual(grams, list(arr))

    def test_no_skips(self):
        # Just ordinary n-grams: k = 0
        tests = [
            ((1, 2, 3), 2, [(1, 2), (2, 3)]),
            ((2, 3, 4, 5), 3, [(2, 3, 4), (3, 4, 5)]),
            ((2, 3, 4, 5), 4, [(2, 3, 4, 5)]),
        ]
        for (arr, n, res) in tests:
            grams = list(ngram.k_skip_n_grams(arr, n, 0))
            self.assertEqual(grams, res)

    def test_n_bigger_arr(self):
        # n is bigger than the length of arr -> no n-grams
        tests = [
            (list(range(4)), 5, 2),
            (list(range(5)), 6, 3),
            (list(range(40)), 41, 5),
            (list(range(4)), 15, 22),
        ]
        for (arr, n, k) in tests:
            grams = list(ngram.k_skip_n_grams(arr, n, k))
            self.assertEqual(grams, [])

    def test_general(self):
        # Just ordinary k-skip-n-grams without any special cases.
        tests = [
            ((1, 2, 3), 2, 2, [(1, 2), (2, 3), (1, 3)]),
            ((1, 2, 3, 4), 3, 1, [(1, 2, 3), (2, 3, 4), (1, 2, 4), (1, 3, 4)]),
            ((1, 2, 3, 4), 2, 2, [(1, 2), (2, 3), (3, 4), (1, 3), (2, 4), (1, 4)]),
        ]
        for (arr, n, k, res) in tests:
            grams = list(ngram.k_skip_n_grams(arr, n, k))
            self.assertEqual(grams, res)

    def test_big_k(self):
        # for each value of k > L - n + 1, the n-grams stay the same.
        tests = [
            ((1, 2, 3, 4), 2, 3, [(1, 2), (2, 3), (3, 4), (1, 3), (2, 4), (1, 4)]),
            ((1, 2, 3, 4), 3, 2, [(1, 2, 3), (2, 3, 4), (1, 2, 4), (1, 3, 4)]),
        ]
        for (arr, n, k_min, res) in tests[1:]:
            for k in range(k_min - 1, k_min + 10, 1):
                grams = list(ngram.k_skip_n_grams(arr, n, k))
                self.assertEqual(grams, res)


if __name__ == '__main__':
    unittest.main()

