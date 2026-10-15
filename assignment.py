def classify(v):
    if v < 148:
        return "Below range"
    elif 148 <= v <= 152:
        return "In range"
    else:
        return "Above range"
def calculate_average(t, c):
    return t / c
n = int(input("Enter the number of soap bars: "))
t = 0
b = 0
r = 0
a = 0
for _ in range(n):
    w = int(input("Enter the soap bar weight: "))
    c = classify(w)
    print(c)
    t += w
    if c == "Below range":
        b += 1
    elif c == "In range":
        r += 1
    else:
        a += 1
h = calculate_average(t, n)
print(f"Total weight: {t} g")
print(f"Average weight: {h:.1f} g")
print(f"Below range: {b}")
print(f"In range: {r}")
print(f"Above range: {a}")
