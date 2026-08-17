def create_arr(arr1, arr2):
    new_arr = []

    for i in range(len(arr1)):
        new_arr.append(arr1[i] + arr2[i])

    return new_arr


def main():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8, 9, 10]

    print(create_arr(arr1, arr2))


main()