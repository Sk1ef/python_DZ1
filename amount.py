def create_new_list(first_list, second_list):
    new_list = []

    for i in range(min(len(first_list), len(second_list))):
        new_list.append(first_list[i] + second_list[i])

    if len(first_list) > len(second_list):
        new_list.extend(first_list[len(second_list):])
    else:
        new_list.extend(second_list[len(first_list):])

    return new_list


def main():
    first_list = [1, 2, 3]
    second_list = [1, 2, 3, 4, 5]

    print(create_new_list(first_list, second_list))


main()