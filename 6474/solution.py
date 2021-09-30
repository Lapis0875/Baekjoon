mirror_map: dict[str, str] = {
    'A': 'A', 'B': '@', 'C': '@', 'D': '@', 'E': '3',
    'F': '@', 'G': '@', 'H': 'H', 'I': 'I', 'J': 'L',
    'K': '@', 'L': 'J', 'M': 'M', 'N': '@', 'O': 'O',
    'P': '@', 'Q': '@', 'R': '@', 'S': '2', 'T': 'T',
    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y',
    'Z': '5', '1': '1', '2': 'S', '3': 'E', '4': '@',
    '5': 'Z', '6': '@', '7': '@', '8': '8', '9': '@'
}


def is_mirror(text: str) -> bool:
    return text == ''.join(map(mirror_map.__getitem__, reversed(text)))


def is_palindrome(text: str) -> bool:
    return text == ''.join(reversed(text))


try:
    while text := input():
        p = is_palindrome(text)
        m = is_mirror(text)

        if m and p:
            print(f'{text} -- is a mirrored palindrome.\n')
        elif m and not p:
            print(f'{text} -- is a mirrored string.\n')
        elif p and not m:
            print(f'{text} -- is a palindrome.\n')
        else:
            print(f'{text} -- is not a palindrome.\n')
except EOFError:
    pass