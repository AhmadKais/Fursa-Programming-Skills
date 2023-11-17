def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)


def print_permutation(string,rest):
    if len(string) == 1:
        print(rest+string[0])
    else:
        for i in range(len(string)):
            current_char = string[i]
            concat = rest+current_char
            remaining_chars = string[:i] + string[i + 1:]
            print_permutation(remaining_chars,concat)


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(2))
    print(factorial(3))

    print_permutation("ah","")
    print_permutation("string","")
    print_permutation("ABC", "")
