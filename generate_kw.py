import argparse
import re
from functools import cache
from typing import Iterable

from helpers import remove_help_tip

# fmt: off
KWID_LETTERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X',  # X = 10
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',  # J = 20
                'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U',  # U = 30
                'W', 'Y', 'Z']  # Z = 33

KWID_WEIGHTS = 4 * [1, 3, 7]


# fmt: on

@cache
def get_kwid_letter_value_map() -> dict[str, int]:
    return {letter: index for index, letter in enumerate(KWID_LETTERS, start=0)}


def _validate_court(court: str) -> None:
    if not re.fullmatch(r'^[A-Z]{2}[1-9][A-Z]$', court):
        raise SystemExit(f'Invalid court symbol "{court}" - it must have the form XX[1-9]X')


def _validate_kw_num(kw_num: int, context: str) -> None:
    if kw_num <= 0 or kw_num >= 1_000_000:
        raise SystemExit(f'{context} "{kw_num}" is invalid')


def _calc_kwid_control_digit_inner(court: str, kw_num: int) -> int:
    letter_value_map = get_kwid_letter_value_map()
    court_letter_values = [letter_value_map[letter] for letter in court]
    kwnum_digits_values = [letter_value_map[digit] for digit in f'{kw_num:08}']
    twelve_values = court_letter_values + kwnum_digits_values

    control_sum = sum(weight * v for weight, v in zip(KWID_WEIGHTS, twelve_values))

    return control_sum % 10


def calc_kwid_control_digit(court: str, kw_num: int) -> int:
    _validate_court(court)
    _validate_kw_num(kw_num, 'KW number')
    return _calc_kwid_control_digit_inner(court, kw_num)


def kwnums(start: int, end: int) -> Iterable[int]:
    _validate_kw_num(start, 'Start KW number')
    _validate_kw_num(end, 'End KW number')
    for i in range(start, end + 1):
        yield i


def filter_kwnums(nums: Iterable[int], last_digit: int) -> Iterable[int]:
    for kwnum in nums:
        if kwnum % 10 == last_digit:
            yield kwnum


def yield_kwid_range(court: str, nums: Iterable[int]) -> Iterable[str]:
    _validate_court(court)
    for kwnum in nums:
        control_digit = _calc_kwid_control_digit_inner(court, kwnum)
        yield f'{court}/{kwnum:08}/{control_digit}'


def filter_kwid_range(kwids: Iterable[str], control_digit: int) -> Iterable[str]:
    if control_digit < 0 or control_digit > 9:
        raise SystemExit(f'Invalid control digit filter "{control_digit}"')

    control_char = str(control_digit)
    for kwid in kwids:
        if kwid[-1] == control_char:
            yield kwid


def main():
    parser = argparse.ArgumentParser(description="Generowanie numerów ksiąg wieczystych")
    remove_help_tip(parser)
    parser.add_argument("court", help="Oznaczenie sądu, np. NS1Z")
    parser.add_argument("start", type=int, help="od numeru")
    parser.add_argument("end", type=int, help="do numeru", nargs='?')
    parser.add_argument("--last-digit", type=int, choices=range(0, 10), metavar="[0-9]",
                        help="filtruj po ostatniej cyfrze numeru")
    parser.add_argument("--hash", type=int, choices=range(0, 10), metavar="[0-9]",
                        help="filtruj po cyfrze kontrolnej")
    args = parser.parse_args()

    nums: Iterable[int] = kwnums(args.start, args.end or args.start)

    if args.last_digit is not None:
        nums = filter_kwnums(nums, args.last_digit)

    kwids: Iterable[str] = yield_kwid_range(str.upper(args.court), nums)

    if args.hash is not None:
        kwids = filter_kwid_range(kwids, args.hash)

    for kwid in kwids:
        print(kwid)


if __name__ == "__main__":
    main()
