
def create_list_comprehantion(old_list):
    return [i**2 for i in old_list if i > 0]

def main():
    old_list = [0, 1, 2, 3, 4, 5, 6]
    print('old_list: ', old_list)
    new_list = create_list_comprehantion(old_list)
    print('new_list: ', new_list)


if __name__ == '__main__':
    main()
