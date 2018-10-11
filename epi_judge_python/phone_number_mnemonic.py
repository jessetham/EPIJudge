from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):
    def generate_mnemonic(phone_number, mnemonic):
        if len(phone_number) == 0:
            result.append(mnemonic)
            return
        number = phone_number[-1]
        chars = num_char_map[number]
        for c in chars:
            generate_mnemonic(
                phone_number[:len(phone_number)-1],
                c + mnemonic
            )

    num_char_map = {
        '0': '0',
        '1': '1',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    result = []
    generate_mnemonic(phone_number, '')
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
