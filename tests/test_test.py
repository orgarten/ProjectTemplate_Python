from pytest import approx
import unittest


class TestLinearIsotropicMaterial(unittest.TestCase):
    def setUp(self):
        self.zero = 0

    def test_zero(self):
        assert 0 == self.zero