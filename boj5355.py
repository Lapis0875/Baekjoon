from typing import Final, TextIO
stdin: TextIO = open(0)

T: Final[int] = int(stdin.readline())
for _ in range(T):
    line: str = stdin.readline()
    sep: int = line.find(" ")
    num: float = float(line[:sep])
    
    for op in line[sep+1:].split():
        match op:
            case "@":
                num *= 3
            case "%":
                num += 5
            case "#":
                num -= 7
    print(f"{num:.2f}")