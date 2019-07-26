#!/usr/bin/env python3

import re


def valid_pancake_case(case):
    regex = re.compile('^[-+]+$')

    case_length = len(case)
    if case_length < 1 or case_length > 100:
        print(f'Invalid: case length ({case_length}) must be between 1 and 100 pancakes')
        return False
    if not regex.match(case):
        print(f'Invalid character in case: {case}')
        return False

    return True

def calculate_flips(case):
    """
    Calculates number of flips required for an individual pancake case.

    case : str
        input string representing the pancake stack. Left being the top of stack
    """
    flip_count = 0

    flip_count += case.count('-+')
    flip_count += case.count('+-')
    if case.endswith('-'):
        flip_count += 1

    return flip_count


if __name__ == '__main__':
    raw_count = input('Number of cases: ')
    try:
        cases_count = int(raw_count)
    except ValueError:
        raise ValueError(
            f'Expected integer of number of pancake cases. Value recieved: {raw_count}')
    if cases_count < 1 or cases_count > 100:
        raise ValueError(f'Expected value 1 <= X <= 100. Value recieved: {raw_count}')

    results = []
    # only because count will be displayed later, use 1 based index insead of 0
    for i in range(1, cases_count + 1):
        input_case = input()

        if not valid_pancake_case(input_case):
            continue
        flip_count = calculate_flips(input_case)
        results.append(f'Case #{i}: {flip_count}')

    [print(result) for result in results]
