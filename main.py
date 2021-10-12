import math


def is_prime(n: int) -> bool:
    if n <= 1 or n % 2 == 0 and n != 2:
        return False
    for index in range(3, int(math.sqrt(n) + 1), 2):
        if n % index == 0:
            return False
    return True


def get_div(n: int) -> int:
    count_div = 0
    for d in range(2, n):
        if n % d == 0:
            count_div += 1
    return count_div + 2


def creat_list():
    final_list = []
    initial_list = input("elementele din lista sunt ")
    for elem_list in initial_list.split(" "):
        elem = int(elem_list)
        final_list.append(elem)
    return final_list


def test_get_longest_all_primes():
    assert get_longest_all_primes([1, 2, 3, 4, 5]) == [2, 3]
    assert get_longest_all_primes([2, 3, 5, 7, 8]) == [2, 3, 5, 7]


def test_get_longest_same_div_count():
    assert get_longest_same_div_count([2, 2, 2, 6]) == [2, 2, 2]
    assert get_longest_same_div_count([6, 8, 2, 6, 6, 6, 8]) == [6, 6, 6, 8]


def get_longest_same_div_count(final_list) -> list[int]:
    verif = True
    maxim = -1
    list_longest_same_div = []
    first_final = 0
    last_final = last = 0
    for index in range(0, len(final_list) - 1):
        index_aux = index
        first = index_aux
        while get_div(final_list[index]) == get_div(final_list[index + 1]) and verif is True:
            last = index + 1
            if index < len(final_list) - 2:
                index += 1
            else:
                verif = False
        if last - first > maxim:
            maxim = last - first
            first_final = first
            last_final = last
    for index in range(first_final, last_final + 1):
        list_longest_same_div.append(final_list[index])
    return list_longest_same_div


def get_longest_all_primes(final_list) -> list[int]:
    maxim = -1
    list_longest_primes = []
    verif = True
    first_final = -2
    last_final = last = -2
    for index in range(0, len(final_list) - 1):
        if is_prime(final_list[index]) is True:
            index_aux = index
            first = index
            while is_prime(final_list[index_aux]) and verif is True:
                last = index_aux
                if index_aux < len(final_list) - 1:
                    index_aux += 1
                else:
                    verif = False
            if last - first > maxim:
                maxim = last - first
                first_final = first
                last_final = last
    for index in range(first_final, last_final + 1):
        list_longest_primes.append(final_list[index])
    return list_longest_primes


def main():
    my_list = []
    verif = True
    print("""""
        1 citeste elementele multimii
        2 afiseaza cel mai mare sir de numere prime
        3 afiseaza cel mai mare sir cu numere cu acelasi divizori
        4 iesi din program
    """)
    while verif is True:
        opt = input("selecteaza optiunea ")
        if opt == '1':
            my_list = creat_list()
        elif opt == "2":
            print(get_longest_all_primes(my_list))
        elif opt == "3":
            print(get_longest_same_div_count(my_list))
        elif opt == "4":
            print("Ati iesit din program")
            break
        else:
            print("Optiunea nu este valida")
            verif = False


if __name__ == '__main__':
    main()
