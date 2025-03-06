from functools import cache

from .courts import COURTS

# fmt: off
KWID_LETTERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X',  # X = 10
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',  # J = 20
                'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U',  # U = 30
                'W', 'Y', 'Z']  # Z = 33

KWID_WEIGHTS = 4 * [1, 3, 7]


# fmt: on


@cache
def _get_kwid_letter_value_map() -> dict[str, int]:
    return {letter: index for index, letter in enumerate(KWID_LETTERS, start=0)}


def validate_court(court: str) -> None:
    if not court in COURTS:
        raise SystemExit(f'Invalid court symbol "{court}" - it must have the form XX[1-9]X')


def validate_kw_num(kw_num: int, context: str) -> None:
    if kw_num <= 0 or kw_num >= 1_000_000:
        raise SystemExit(f'{context} "{kw_num}" is invalid')


def calc_kwid_control_digit_inner(court: str, kw_num: int) -> int:
    letter_value_map = _get_kwid_letter_value_map()
    court_letter_values = [letter_value_map[letter] for letter in court]
    kwnum_digits_values = [letter_value_map[digit] for digit in f'{kw_num:08}']
    twelve_values = court_letter_values + kwnum_digits_values

    control_sum = sum(weight * v for weight, v in zip(KWID_WEIGHTS, twelve_values))

    return control_sum % 10


def calc_kwid_control_digit(court: str, kw_num: int) -> int:
    validate_court(court)
    validate_kw_num(kw_num, 'KW number')
    return calc_kwid_control_digit_inner(court, kw_num)
