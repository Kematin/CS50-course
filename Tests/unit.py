from driven import is_prime
import unittest

# Containe all tests
class Tests(unittest.TestCase):
    def test_1(self):
        """Check that 1 is not prime."""
        self.assertFalse(is_prime(1))

    def test_8(self):
        """Check that 8 is prime."""
        self.assertTrue(is_prime(8))

    def test_28(self):
        """Check that 28 is not prime."""
        self.assertFalse(is_prime(28))


if __name__ == "__main__":
    # Call all tests from container (call only functions, which start test_)
    unittest.main()
