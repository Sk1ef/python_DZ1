def create_arr(arr1, arr2):
    new_arr = []

    for i in range(min(len(arr1), len(arr2))):
        new_arr.append(arr1[i] + arr2[i])

    return new_arr


def main():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8]

    print(create_arr(arr1, arr2))


main()

