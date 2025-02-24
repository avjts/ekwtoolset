# import logging
import unittest

from generate_kw import calc_kwid_control_digit, kwnums, yield_kwid_range, filter_kwid_range


# logging.basicConfig(level=logging.DEBUG)


class TestGenerateKw(unittest.TestCase):
    # logger = logging.getLogger(__name__)

    def test_calc_kwid_control_digit(self):
        self.assertEqual(calc_kwid_control_digit('NS1Z', 40549), 0)
        self.assertEqual(calc_kwid_control_digit('NS1Z', 40768), 1)
        self.assertEqual(calc_kwid_control_digit('NS1Z', 40181), 2)
        self.assertEqual(calc_kwid_control_digit('NS1Z', 40322), 3)
        self.assertEqual(calc_kwid_control_digit('NS1Z', 40626), 4)
        self.assertEqual(calc_kwid_control_digit('NS1Z', 40618), 5)
        self.assertEqual(calc_kwid_control_digit('NS1Z', 40785), 6)
        self.assertEqual(calc_kwid_control_digit('NS1Z', 40625), 7)
        self.assertEqual(calc_kwid_control_digit('NS1Z', 40587), 8)
        self.assertEqual(calc_kwid_control_digit('NS1Z', 40397), 9)

        with self.assertRaises(SystemExit) as ctx:
            calc_kwid_control_digit('NS10Z', 1)

        self.assertIn('"NS10Z"', str(ctx.exception))

        with self.assertRaises(SystemExit) as ctx:
            calc_kwid_control_digit('NŚ1Ż', 1)

        self.assertIn('"NŚ1Ż"', str(ctx.exception))

        with self.assertRaises(SystemExit) as ctx:
            calc_kwid_control_digit('NS1Z', -1)

        self.assertIn('"-1"', str(ctx.exception))

    def test_yield_kwid_range(self):
        self.assertEqual([], list(yield_kwid_range('NS1Z', range(1, 1))))

        self.assertEqual(['NS1Z/00000002/2'],
                         list(yield_kwid_range('NS1Z', kwnums(2, 2))))
        self.assertEqual(['NS1Z/00000009/1', 'NS1Z/00000010/1'],
                         list(yield_kwid_range('NS1Z', kwnums(9, 10))))

        with self.assertRaises(SystemExit) as ctx:
            list(yield_kwid_range('NS10Z', range(1, 100)))

        self.assertIn('"NS10Z"', str(ctx.exception))

        with self.assertRaises(SystemExit) as ctx:
            list(yield_kwid_range('NS1Z', kwnums(-1, 10)))

        self.assertIn('"-1"', str(ctx.exception))

        with self.assertRaises(SystemExit) as ctx:
            list(yield_kwid_range('NS1Z', kwnums(1, 1_000_000)))

    def test_yield_filtered_kwids(self):
        self.assertEqual(['NS1Z/00000006/0'],
                         list(filter_kwid_range(
                             yield_kwid_range('NS1Z', kwnums(1, 10)),
                             0)
                         )
                         )


if __name__ == '__main__':
    unittest.main(verbosity=2)
