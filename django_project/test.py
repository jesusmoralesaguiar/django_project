

def descending_order(n):
    s = sorted(str(n), reverse=True)
    return int("".join(s))


if __name__ == "__main__":
    result = descending_order(123456789)
    print(result)