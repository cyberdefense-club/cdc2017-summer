import unittest
import lessonbatch_02.meistergeist as meistergeist

# class ClockTest(unittest.TestCase):
#     # Test creating a new clock with an initial time.
#     def test_on_the_hour(self):
#         self.assertEqual('08:00', str(Clock(8, 0)))


class MeistergeistTest(unittest.TestCase):
    # TODO: (1/2) refactor meistergeist so that it can check for invididual
    # TODO: (2/2) feedback values.
    def test_correct_first_guess(self):
        self.assertEqual(
            meistergeist.main(
                4, '1234', 12,
                ['1234', '5678', '9090', '8787',
                 '1111', '2222', '4958', '1354',
                 '9433', '2831', '8754', '3289']),
            meistergeist.WIN)

    def test_fail_on_long_guess(self):
        self.assertEqual(
            meistergeist.main(1, '5', 1, ['5542']),
            meistergeist.LOSS
        )

    def test_fail_on_short_guess(self):
        self.assertEqual(
            meistergeist.main(4, '5542', 1, ['5']),
            meistergeist.LOSS
        )

    def test_succeed_on_one_guess(self):
        self.assertEqual(
            meistergeist.main(4, '5542', 1, ['5542']),
            meistergeist.WIN
        )

    def test_fail_on_one_guess_first_digit_wrong(self):
        self.assertEqual(
            meistergeist.main(4, '5542', 1, ['6542']),
            meistergeist.LOSS
        )


    def test_fail_on_one_guess_second_digit_wrong(self):
        self.assertEqual(
            meistergeist.main(4, '5542', 1, ['5442']),
            meistergeist.LOSS
        )

    def test_fail_on_one_guess_third_digit_wrong(self):
        self.assertEqual(
            meistergeist.main(4, '5542', 1, ['5592']),
            meistergeist.LOSS
        )


    def test_fail_on_one_guess_fourth_digit_wrong(self):
        self.assertEqual(
            meistergeist.main(4, '5542', 1, ['5540']),
            meistergeist.LOSS
        )

    def test_complex_case_01(self):
        self.assertEqual(
            meistergeist.main(10, '1122554403', 1, ['1020555407']),
            meistergeist.LOSS
        )

    def test_complex_case_02(self):
        self.assertEqual(
            meistergeist.main(10, '1122574103', 1, ['1020555407']),
            meistergeist.LOSS
        )


if __name__ == '__main__':
    unittest.main()
