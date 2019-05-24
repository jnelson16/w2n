import unittest
from word2number import s2n, w2n


class TestW2N(unittest.TestCase):
    def test_positives(self):
        self.assertEqual(w2n.word_to_num("two million three thousand nine hundred and eighty four"), 2003984)
        self.assertEqual(w2n.word_to_num("nineteen"), 19)
        self.assertEqual(w2n.word_to_num("two thousand and nineteen"), 2019)
        self.assertEqual(w2n.word_to_num("two million three thousand and nineteen"), 2003019)
        self.assertEqual(w2n.word_to_num('three billion'), 3000000000)
        self.assertEqual(w2n.word_to_num('three million'), 3000000)
        self.assertEqual(w2n.word_to_num('one hundred twenty three million four hundred fifty six thousand seven hundred and eighty nine')
, 123456789)
        self.assertEqual(w2n.word_to_num('eleven'), 11)
        self.assertEqual(w2n.word_to_num('nineteen billion and nineteen'), 19000000019)
        self.assertEqual(w2n.word_to_num('one hundred and forty two'), 142)
        self.assertEqual(w2n.word_to_num('112'), 112)
        self.assertEqual(w2n.word_to_num('11211234'), 11211234)
        self.assertEqual(w2n.word_to_num('five'), 5)
        self.assertEqual(w2n.word_to_num('two million twenty three thousand and forty nine'), 2023049)
        self.assertEqual(w2n.word_to_num('two point three'), 2.3)
        self.assertEqual(w2n.word_to_num('two million twenty three thousand and forty nine point two three six nine'), 2023049.2369)
        self.assertEqual(w2n.word_to_num('one billion two million twenty three thousand and forty nine point two three six nine'), 1002023049.2369)
        self.assertEqual(w2n.word_to_num('point one'), 0.1)
        self.assertEqual(w2n.word_to_num('point'), 0)
        self.assertEqual(w2n.word_to_num('point nineteen'), 0)
        self.assertEqual(w2n.word_to_num('one hundred thirty-five'), 135)
        self.assertEqual(w2n.word_to_num('hundred'), 100)
        self.assertEqual(w2n.word_to_num('thousand'), 1000)
        self.assertEqual(w2n.word_to_num('million'), 1000000)
        self.assertEqual(w2n.word_to_num('billion'), 1000000000)
        self.assertEqual(w2n.word_to_num('nine point nine nine nine'), 9.999)
        self.assertEqual(w2n.word_to_num('seventh point nineteen'), 0)

    def test_negatives(self):
        self.assertRaises(ValueError, w2n.word_to_num, '112-')
        self.assertRaises(ValueError, w2n.word_to_num, '-')
        self.assertRaises(ValueError, w2n.word_to_num, 'on')
        self.assertRaises(ValueError, w2n.word_to_num, 'million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'three million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'million four million')
        self.assertRaises(ValueError, w2n.word_to_num, 'thousand million')
        self.assertRaises(ValueError, w2n.word_to_num, 'one billion point two million twenty three thousand and forty nine point two three six nine')
        self.assertRaises(ValueError, w2n.word_to_num, 112)


class TestS2N(unittest.TestCase):
    def test_positives(self):
        self.assertEqual(s2n.string_to_nums(
            "there are two million three thousand nine hundred and eighty four people living in this city"),
            "there are 2003984 people living in this city")
        self.assertEqual(s2n.string_to_nums("i am nineteen years old"), "i am 19 years old")
        self.assertEqual(s2n.string_to_nums('the number nine point nine nine nine is almost ten'), 'the number 9.999 is almost 10')
        self.assertEqual(s2n.string_to_nums('there are two men and two women standing in line'), 'there are 2 men and 2 women standing in line')
        # need to add support for separate numbers in sequence
        self.assertEqual(s2n.string_to_nums('one two three four five'), '1')

    def test_negatives(self):
        # potentially allow digits to return full string instead of raising ValueError
        self.assertRaises(ValueError, s2n.string_to_nums, 'this book is 112 pages long')


if __name__ == '__main__':
    unittest.main()
