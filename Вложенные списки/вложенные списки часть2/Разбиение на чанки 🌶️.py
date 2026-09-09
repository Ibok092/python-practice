def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result

symbols = input().split()
n = int(input())

print(chunked(symbols, n))