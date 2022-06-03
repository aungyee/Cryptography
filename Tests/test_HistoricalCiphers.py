import HistoricalCiphers.ShiftCipher as Sc
import HistoricalCiphers.AffineCipher as Ac


def test_shiftCipher():
    key = 123
    assert Sc.decrypt(Sc.encrypt("hello", key), key) == "hello"


def test_affineCipher():
    a = Ac.generate_a(26)
    b = 123
    assert Ac.decrypt(Ac.encrypt("hello", a, b), a, b) == "hello"
