import argparse
from typing import Iterable

from py import remove_help_tip
from kwengine import validate_kw_num, validate_court, calc_kwid_control_digit_inner


def kwnums(start: int, end: int) -> Iterable[int]:
    validate_kw_num(start, 'Start KW number')
    validate_kw_num(end, 'End KW number')
    for i in range(start, end + 1):
        yield i


def filter_kwnums(nums: Iterable[int], last_digit: int) -> Iterable[int]:
    for kwnum in nums:
        if kwnum % 10 == last_digit:
            yield kwnum


def yield_kwid_range(court: str, nums: Iterable[int]) -> Iterable[str]:
    validate_court(court)
    for kwnum in nums:
        control_digit = calc_kwid_control_digit_inner(court, kwnum)
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
