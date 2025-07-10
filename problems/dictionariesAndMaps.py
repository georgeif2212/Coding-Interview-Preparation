import sys


n = int(input())


phone_book = {}

# 3. Leer n líneas de entradas
for _ in range(n):
    entry = input().strip().split()
    name = entry[0]
    phone = entry[1]
    phone_book[name] = phone

# 4. Leer queries hasta EOF
for line in sys.stdin:
    query = line.strip()
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
