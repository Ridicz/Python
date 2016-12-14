def solve1(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            print("Rownanie nieokreslone.")
            return
        else:
            print("Rownanie sprzeczne.")
            return
    if a == 0:
        print("Rozwiazenie to prosta: y = " + str(-float(c) / float(b)))
        return
    if b == 0:
        print("Rozwiazenie to prosta: x = " + str(-float(c) / float(a)))
        return

    result = "(" + str(float(-a) / float(b)) + ")x" + " + (" + str(float(-c) / float(b)) + ")"
    print("Rozwiazenie to prosta: y = " + result)

solve1(1, 2, 3)
solve1(0, 0, 0)
solve1(0, 0, 1)
solve1(0, 1, 1)
solve1(1, 0, 1)
