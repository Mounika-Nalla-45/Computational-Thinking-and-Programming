# def calculate(a, b):
#     result = a + b
#     print("Result:", result)

# calculate(10, 5)
def add_numbers(a: int, b: int) -> int:
    return a + b


def main():
    result = add_numbers(10, 5)
    print("Result:", result)


if __name__ == "__main__":
    main()