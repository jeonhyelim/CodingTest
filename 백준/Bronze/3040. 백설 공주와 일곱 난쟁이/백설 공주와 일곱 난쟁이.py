n = [int(input()) for _ in range(9)]
tot = sum(n)

def solve():
    for i in range(8):
        for j in range(i+1,9):
            if tot - n[i] - n[j] == 100:
                for k in n:
                    if k != n[i] and k != n[j]:
                        print(k)

                return

solve()