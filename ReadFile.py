import csv


def search_values():
    """Search values of specific key
    return all(list) from 'login' column

    """
    with open("Data/users.csv", 'r') as f:
        l = list(csv.reader(f))
        my_dict = {i[0]:[x for x in i[1:]] for i in zip(*l)}    #MAKE DICT

        return my_dict.get('login')                         #GET VALUES OF KEY 'login'

def search_index():
    """Search of index
    return first index of value 'Adam123' from 'login' column

    """
    with open("Data/users.csv", 'r') as f:
        l = list(csv.reader(f))
        my_dict = {i[0]:[x for x in i[1:]] for i in zip(*l)}
        ind = my_dict['login'].index('Adam123')                 #GET INDEX OF VALUE 'Adam123'
        return ind                                              #FROM KEY 'login'

def search_value():
    """Search values of specific key and index
    return value from 'password' column from index of first 'Adamus123' from 'login' column.

    """
    with open("Data/users.csv", 'r') as f:
        l = list(csv.reader(f))
        my_dict = {i[0]:[x for x in i[1:]] for i in zip(*l)}
        ind = my_dict['login'].index('Adam123')
        return my_dict['password'][ind]                          #GET VALUE OF INDEX^ FROM KEY
        #                                                         #'password'
        # print('==================')

        # for x in my_dict:                                       #GET OBJECT OF INDEX^
        #     print(my_dict[x][ind])

        # print('_____________________')

        # indices = [i for i, x in enumerate(my_dict['login']) if x == "Adam123"] #<< WORKING
        # print(indices)                                        #GET INDEXYS OF 'Adam123'
                                                                #FROM 'login'
        # print('\n___________OptionA__________')

        # for x in my_dict:
        #     print('======================')
        #     y=0
        #     while y<len(indices):
        #         print(my_dict[x][indices[y]])
        #         y=y+1

        # print('\n+++++++++++OptionB+++++++++++++')

        # for y in range(0, len(indices)):
        #     print('======================')
        #     for x in my_dict:
        #         print(my_dict[x][indices[y]])

print(search_values())

# print(search_index())

# print(search_value())
