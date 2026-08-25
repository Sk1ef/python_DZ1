def create_new_list(first_list, second_list):
    new_list = []

    for i in range(min(len(first_list), len(second_list))):
        new_list.append(first_list[i] + second_list[i])

    return new_list


def main():
    first_list = [1, 2, 3, 4, 5]
    second_list = [6, 7, 8, 9, 10]

    print(create_new_list(first_list, second_list))


main()