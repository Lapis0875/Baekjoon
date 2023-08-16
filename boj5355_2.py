from typing import Callable, Final, TextIO
stdin: TextIO = open(0)

OP_MAP: dict[str, Callable[[float], float]] = {
    "@": lambda x: x * 3,
    "%": lambda x: x + 5,
    "#": lambda x: x - 7
}

T: Final[int] = int(stdin.readline())
for _ in range(T):
    line: str = stdin.readline()
    sep: int = line.find(" ")
    num: float = float(line[:sep])
    
    for op in line[sep+1:].split():
        num = OP_MAP[op](num)
    print(f"{num:.2f}")