"""Quick helpers."""

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

if __name__ == "__main__":
    print(clamp(10, 0, 6))

# works for now
