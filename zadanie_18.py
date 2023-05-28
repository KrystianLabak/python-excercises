def funkcja(*argumenty):
    print(argumenty)
    for x in (argumenty):
        print(x)
    print()


# funkcja(20, 18, 200, "tekst", 123, [99, 21])
#
# funkcja(54, "asdas")
#
# funkcja()

def max(*argumenty):
    m = argumenty[0]
    for x in argumenty[1:]:
        if m < x:
            m=x
    return m
print(max(20, 25, 2000, 52))
max(20, 25, 2000, 52)
liczbamax = max(300, 72, 200, 22)
print(liczbamax)

