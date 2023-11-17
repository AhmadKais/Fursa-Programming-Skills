def check_even_odd(element):
    result = element & 0b01
    if result == 1:
        return "odd"
    else:
        return "even"


def count_set_bits(num):
    count = 0
    while num != 0:
        count += (num & 1)
        num = num >> 1
    return count


if __name__ == "__main__":
    print(check_even_odd(1))
    print(check_even_odd(2))
    print(check_even_odd(3))
    print(check_even_odd(4))
    print(check_even_odd(5))

    # test second function
    print(count_set_bits(1))
    print(count_set_bits(2))
    print(count_set_bits(3))
    print(count_set_bits(16))
    print(count_set_bits(15))
