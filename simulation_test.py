import unittest


from simulation import getNFAStream, simulate

class MyTestCase(unittest.TestCase):
    def test_simulation(self):
        nfa = getNFAStream("./nfa")

        ans = simulate(nfa, "101")

        self.assertEqual(ans == True, True)

        self.assertEqual(simulate(nfa, "") == False, True)
        self.assertEqual(simulate(nfa, "1") == False, True)
        self.assertEqual(simulate(nfa, "10") == False, True)
        self.assertEqual(simulate(nfa, "1111111111111") == False, True)
        self.assertEqual(simulate(nfa, "00000000000") == False, True)
        self.assertEqual(simulate(nfa, "0000000000101") == True, True)
        self.assertEqual(simulate(nfa, "001101101100000101") == True, True)
        self.assertEqual(simulate(nfa, "001101101100000110") == False, True)
        self.assertEqual(simulate(nfa, "001101101100000011") == False, True)


if __name__ == '__main__':
    unittest.main()
