import unittest
import count
from random import randint


class TestCount(unittest.TestCase):
    def test_deterministic(self):
        for L in range(20):
            for n in range(20):
                for k in range(20):
                    c1 = count.k_skip_n_grams_count_direct(L, n, k)
                    c2 = count.k_skip_n_grams_count(L, n, k)
                    self.assertEqual(c1, c2)
  
    def test_random(self):
        for _ in range(100):
            L, n, k = randint(20, 25), randint(20, 25), randint(20, 25),
            c1 = count.k_skip_n_grams_count_direct(L, n, k)
            c2 = count.k_skip_n_grams_count(L, n, k)
            self.assertEqual(c1, c2)


if __name__ == '__main__':
    unittest.main()
