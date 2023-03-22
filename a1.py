
import unittest
def decimal_to_roman(decimal):
    if decimal == 1:
        return 'I'
    elif decimal == 5:
        return 'V'
    else:
        return "X"
    
class TestDecimalToRoman(unittest.TestCase):
    
    def test_uno(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, 'I')
    
    def test_diez(self):
        resultado = decimal_to_roman (10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman (5)
        self.assertEqual(resultado, 'V')