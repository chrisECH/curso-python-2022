def multiplicar(x, y):
    return x * y


result = multiplicar(2,5)
print(result)

import unittest

class pruebas(unittest.TestCase):
    def test(self):
        self.assertEquals(multiplicar(2,4),8)
        self.assertEquals(multiplicar(2,4),9)

if __name__ == '__main__':
    unittest.main()