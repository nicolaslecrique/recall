from unittest import TestCase
from tools.uri_utils import generate_uri


class TestUriUtils(TestCase):
    def test_generate_uri(self):
        result: str = generate_uri("&é" "(-è_çà)=)     /:@&~*/56<>:!§AZ ERTYbl    abla")
        expected: str = "e-eca-56ssaz-ertybl-abla-d7f4d03ae488"
        self.assertEqual(expected, result)

    def test_generate_uri_short(self):
        result: str = generate_uri("short")
        expected: str = "short-588748a4b0b4"
        self.assertEqual(expected, result)

    def test_generate_uri_sha_uniqueness(self):
        res1 = generate_uri("test", [])
        res2 = generate_uri("test", ["1"])
        res3 = generate_uri("test", ["1", "1"])
        res4 = generate_uri("test", ["1", "2"])
        self.assertNotEqual(res1, res2)
        self.assertNotEqual(res2, res3)
        self.assertNotEqual(res3, res4)
