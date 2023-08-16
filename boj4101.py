from sys import stdin


while True:
    line: str = stdin.readline()
    if line == "0 0":
        break
    
    A, B = map(int, line.split(" "))
    print("Yes" if A > B else "No")