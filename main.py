import sys
import os

import pyperclip

from compute import get_code_from_file

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python main.py <file_path> <num_monitors_wide> <num_monitors_tall>')
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f'File "{file_path}" does not exist!')
        sys.exit(1)

    if not sys.argv[2].isdigit() or not sys.argv[3].isdigit():
        print('Number of monitors wide and tall must be integers!')
        sys.exit(1)

    num_monitors_wide = int(sys.argv[2])
    num_monitors_tall = int(sys.argv[3])

    if not 1 <= num_monitors_wide <= 8:
        print('Number of monitors wide must be between 1 and 8!')
        sys.exit(1)

    if not 1 <= num_monitors_tall <= 6:
        print('Number of monitors tall must be between 1 and 6!')
        sys.exit(1)

    code = get_code_from_file(file_path, num_monitors_wide, num_monitors_tall)
    pyperclip.copy(code)
    print('Code copied to clipboard!')

    file_path = os.path.splitext(os.path.basename(file_path))[0] + '.lua'
    with open(file_path, 'w') as f:
        f.write(code)
    print(f'Code written to "{file_path}"!')
